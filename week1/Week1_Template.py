import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16


class mohr():
    def __init__(self):
        pass

    def plot_mohr3d(self, S):
        # This helper function was used to calculate eigen values of the Stress tensor and stores them in increasing order.
        def eigen(Stress):
            s = np.linalg.eigvalsh(Stress)
            s1 = np.amax(s)
            s3 = np.amin(s)
            for i in s:
                if i != s1 and i != s3:
                    s2 = i
            return s3, s2, s1

        def Radius(s3, s2, s1):
            c1 = (s1 + s3) / 2
            c2 = (s1 + s2) / 2
            c3 = (s2 + s3) / 2
            r1 = (s1 - s3) / 2
            r2 = (s1 - s2) / 2
            r3 = (s2 - s3) / 2
            cent_maj = c1  # Major radius
            R_maj = r1  # Centre of the major circle
            R_min = r3
            cent_min = c3
            R_mid = r2
            cent_mid = r2
            # FIGURE of Mohr circle
            figure, axes = plt.subplots()
            circle1 = plt.Circle((c1, 0), r1, fill=False)
            circle2 = plt.Circle((c2, 0), r2, fill=False)
            circle3 = plt.Circle((c3, 0), r3, fill=False)
            plt.plot(c1, 0, 'ro')
            plt.plot(c2, 0, 'ro')
            plt.plot(c3, 0, 'ro')
            plt.xlim(c1 - 6 * (r1) / 5, c1 + 6 * (r1) / 5)
            plt.ylim(-(6 * r1 / 5), 6 * (r1) / 5)
            axes.set_aspect(1)
            axes.add_artist(circle1)
            axes.add_artist(circle2)
            axes.add_artist(circle3)
            plt.grid()
            plt.savefig('Mohr.png')
            return R_maj, R_min, R_mid

        s3, s2, s1 = eigen(S)
        R_maj, R_min, R_mid = Radius(s3, s2, s1)
        return R_maj, R_min, R_mid


Stress = np.array([[90,0,95],[0,96,0],[95,0,-50]])
mohr1 = mohr()
print(mohr1.plot_mohr3d(Stress))