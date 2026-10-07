import numpy as np
from itertools import permutations
from drawing import drawing_2d_picture
from task1 import (building_stretch_matrix, building_shear_matrix, building_rotation_matrix)


def running_task_2(lynx):
    print('\n######## TASK 2 ########\n')

    # Три перетворення, які будемо комбінувати
    stretch_matrix = building_stretch_matrix(1.5, 0.7)
    shear_matrix = building_shear_matrix(0.5, 0)
    rotation_matrix = building_rotation_matrix(np.radians(45))

    all_transformations = {
        'Stretch': stretch_matrix,
        'Shear': shear_matrix,
        'Rotation': rotation_matrix,
    }

    # Усі 6 можливих порядків (3! = 6), а в умові треба мінімум 3
    all_orders = list(permutations(all_transformations.keys()))

    final_matrices = []

    for order in all_orders:
        # Накопичуємо загальну матрицю: кожне наступне перетворення множимо ЗЛІВА.
        # Якщо порядок Stretch -> Shear -> Rotation, то загальна матриця = Rotation * Shear * Stretch
        total_matrix = np.eye(2)
        for name in order:
            total_matrix = all_transformations[name] @ total_matrix

        new_lynx = total_matrix @ lynx.copy()
        final_matrices.append(total_matrix)

        order_text = ' -> '.join(order)
        drawing_2d_picture(lynx, new_lynx, total_matrix,
                           f'Порядок: {order_text}',
                           f'task2_{"_".join(order)}.png')

    # Перевіряємо чи всі результати однакові
    print('=' * 50)
    print('Чи залежить результат від порядку?')
    all_same = all(np.allclose(final_matrices[0], matrix) for matrix in final_matrices)
    if all_same:
        print('Ні, усі матриці однакові.')
    else:
        print('Так, залежить: матриці для різних порядків різні.')
        print('Причина: множення матриць не комутативне, тобто AB != BA (у загальному випадку).')