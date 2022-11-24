from svgpathtools import svg2paths
import numpy as np


def svg_reader(filename):
    paths, attributes = svg2paths(filename)

    points = []
    for pa in paths:
        for l in pa:
            p0 = [l.start.real, l.start.imag]
            p1 = [l.end.real, l.end.imag]
            points.append([p0, p1])

    points *= np.array([1, -1]).reshape(1, 1, 2)
    return np.array(points)


if __name__ == '__main__':
    filename = "files/output.svg"
    print(svg_reader(filename=filename))