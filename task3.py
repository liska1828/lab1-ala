import numpy as np
from drawing import drawing_3d_picture


# ---------- Побудова 3D матриць (як в умові) ----------

def building_rotation_xy_matrix(theta):
    # поворот у площині xy (навколо осі z)
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])


def building_rotation_yz_matrix(theta):
    # поворот у площині yz (навколо осі x)
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])


def building_rotation_xz_matrix(theta):
    # поворот у площині xz (навколо осі y) - матриця саме така, як в умові лабораторної
    return np.array([[np.cos(theta), 0, -np.sin(theta)],
                     [0, 1, 0],
                     [np.sin(theta), 0, np.cos(theta)]])


# ---------- Самі перетворення ----------
# X - масив форми (3, N): рядки x, y, z.

def rotate_xy(X, theta):
    copy_of_X = X.copy()
    matrix = building_rotation_xy_matrix(theta)
    return matrix @ copy_of_X


def rotate_yz(X, theta):
    copy_of_X = X.copy()
    matrix = building_rotation_yz_matrix(theta)
    return matrix @ copy_of_X


def rotate_xz(X, theta):
    copy_of_X = X.copy()
    matrix = building_rotation_xz_matrix(theta)
    return matrix @ copy_of_X


# ---------- Запуск Task 3 ----------

def running_task_3(airplane):
    print('\n######## TASK 3 ########\n')

    theta = np.radians(45)

    new_airplane = rotate_yz(airplane, theta)
    drawing_3d_picture(airplane, new_airplane, building_rotation_yz_matrix(theta),
                       'Поворот 45 градусів навколо осі X (площина yz)', 'task3_rotation_yz.png')

    new_airplane = rotate_xz(airplane, theta)
    drawing_3d_picture(airplane, new_airplane, building_rotation_xz_matrix(theta),
                       'Поворот 45 градусів навколо осі Y (площина xz)', 'task3_rotation_xz.png')

    new_airplane = rotate_xy(airplane, theta)
    drawing_3d_picture(airplane, new_airplane, building_rotation_xy_matrix(theta),
                       'Поворот 45 градусів навколо осі Z (площина xy)', 'task3_rotation_xy.png')