import matplotlib.pyplot as plt
import math


def draw_triangle(side1, side2, side3):
    A = (0, 0)
    B = (side1, 0)
    angle = math.acos((side2**2 + side3**2 - side1 ** 2) / (2 * side2 * side3))

    Cx = side2 * math.cos(angle)
    Cy = side2 * math.sin(angle)

    C = (Cx, Cy)
    triangle = plt.Polygon([A, B, C], closed=True, edgecolor='black', facecolor='lightgrey')

    plt.gca().add_patch(triangle)

    # Настройка осей и отображение результата
    plt.axis('equal')

    plt.show()
