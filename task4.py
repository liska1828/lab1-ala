import numpy as np
from drawing import drawing_3d_picture
from task3 import (building_rotation_xy_matrix, building_rotation_yz_matrix, building_rotation_xz_matrix)


def running_task_4(airplane):
    print('\n######## TASK 4 ########\n')

    # Три різні кути для трьох поворотів
    xy_matrix = building_rotation_xy_matrix(np.radians(30))
    yz_matrix = building_rotation_yz_matrix(np.radians(45))
    xz_matrix = building_rotation_xz_matrix(np.radians(60))

    # Порядок: спочатку yz, потім xz, потім xy.
    # Кожне наступне перетворення множимо зліва: total = xy * xz * yz
    total_matrix = np.eye(3)
    total_matrix = yz_matrix @ total_matrix
    total_matrix = xz_matrix @ total_matrix
    total_matrix = xy_matrix @ total_matrix

    new_airplane = total_matrix @ airplane.copy()

    drawing_3d_picture(airplane, new_airplane, total_matrix,
                       'Комбінація: yz (45) -> xz (60) -> xy (30)', 'task4_combination.png')