import numpy as np
from drawing import drawing_2d_picture


# ---------- Побудова матриць ----------

def building_stretch_matrix(a, b):
    # Розтяг: діагональна матриця. a - по осі x, b - по осі y.
    return np.array([[a, 0],
                     [0, b]])


def building_shear_matrix(a, b):
    # Зсув: a нахиляє по горизонталі, b - по вертикалі.
    return np.array([[1, a],
                     [b, 1]])


def building_reflection_matrix(a, b):
    # Відображення відносно прямої, що проходить через початок координат
    # і задана вектором (a, b).
    return (1 / (a ** 2 + b ** 2)) * np.array([[a ** 2 - b ** 2, 2 * a * b],
                                               [2 * a * b, b ** 2 - a ** 2]])


def building_rotation_matrix(theta):
    # Поворот проти годинникової стрілки на theta радіан.
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])


# ---------- Самі перетворення ----------
# X - масив форми (2, N): перший рядок x, другий рядок y.
# Спочатку робимо копію, потім множимо матрицю на дані.

def stretch(X, a, b):
    copy_of_X = X.copy()
    matrix = building_stretch_matrix(a, b)
    return matrix @ copy_of_X


def shear(X, a, b):
    copy_of_X = X.copy()
    matrix = building_shear_matrix(a, b)
    return matrix @ copy_of_X


def reflection(X, a, b):
    copy_of_X = X.copy()
    matrix = building_reflection_matrix(a, b)
    return matrix @ copy_of_X


def rotation(X, theta):
    copy_of_X = X.copy()
    matrix = building_rotation_matrix(theta)
    return matrix @ copy_of_X


# ---------- Запуск Task 1 ----------

def running_task_1(lynx):
    print('\n######## TASK 1 ########\n')

    # --- Розтяг ---
    # a, b > 1 - збільшення, 0 < a, b < 1 - стиснення, від'ємне - ще й відображення.
    for a, b in [(1.5, 0.7), (2, 2), (0.5, 1), (-1, 1)]:
        new_lynx = stretch(lynx, a, b)
        drawing_2d_picture(lynx, new_lynx, building_stretch_matrix(a, b),
                           f'Stretch ({a}, {b})', f'task1_stretch_{a}_{b}.png')

    # --- Зсув ---
    # (a, 0) - тільки горизонтальний, (0, b) - тільки вертикальний.
    for a, b in [(0.5, 0), (0, 0.5), (0.5, 0.5), (-0.5, 0)]:
        new_lynx = shear(lynx, a, b)
        drawing_2d_picture(lynx, new_lynx, building_shear_matrix(a, b),
                           f'Shear ({a}, {b})', f'task1_shear_{a}_{b}.png')

    # --- Відображення ---
    # (1, 0) - відносно осі x, (0, 1) - відносно осі y, (1, 1) - відносно прямої y = x.
    for a, b in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        new_lynx = reflection(lynx, a, b)
        drawing_2d_picture(lynx, new_lynx, building_reflection_matrix(a, b),
                           f'Reflection ({a}, {b})', f'task1_reflection_{a}_{b}.png')

    # --- Поворот ---
    for degrees in [45, 90, 180, -45]:
        theta = np.radians(degrees)
        new_lynx = rotation(lynx, theta)
        drawing_2d_picture(lynx, new_lynx, building_rotation_matrix(theta),
                           f'Rotation ({degrees} градусів)', f'task1_rotation_{degrees}.png')