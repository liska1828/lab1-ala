# import os
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Якщо не хочеш щоб вікна з графіками відкривались - постав False (картинки все одно збережуться).
# show_windows = True
#
# results_folder = 'results'
#
#
# def saving_picture(figure, filename):
#     os.makedirs(results_folder, exist_ok=True)
#     figure.savefig(os.path.join(results_folder, filename), dpi=120, bbox_inches='tight')
#
#
# def printing_matrix(title, matrix):
#     print('=' * 50)
#     print(title)
#     print('Матриця перетворення:')
#     print(np.round(matrix, 4))
#     print()
#
#
# def drawing_2d_picture(original_points, new_points, matrix, title, filename):
#     # original_points і new_points мають форму (2, N)
#     printing_matrix(title, matrix)
#
#     figure, axis = plt.subplots(figsize=(7, 7))
#
#     axis.fill(original_points[0], original_points[1], color='gray', alpha=0.4, label='Оригінал')
#     axis.fill(new_points[0], new_points[1], color='blue', alpha=0.4, label='Після перетворення')
#
#     axis.axhline(0, color='black', linewidth=0.5)
#     axis.axvline(0, color='black', linewidth=0.5)
#     axis.set_aspect('equal')
#     axis.grid(True, alpha=0.3)
#     axis.set_title(title)
#     axis.legend()
#
#     saving_picture(figure, filename)
#     if show_windows:
#         plt.show()
#     plt.close(figure)
#
#
# def drawing_3d_picture(original_points, new_points, matrix, title, filename):
#     # original_points і new_points мають форму (3, N)
#     printing_matrix(title, matrix)
#
#     figure = plt.figure(figsize=(12, 6))
#
#     # Щоб не малювати сотні тисяч точок - беремо кожну n-ту
#     step = max(1, original_points.shape[1] // 20000)
#
#     # Однакові межі для обох графіків, щоб було видно, що модель реально повернулась
#     biggest = max(np.abs(original_points).max(), np.abs(new_points).max())
#
#     for number, (points, name) in enumerate([(original_points, 'Оригінал'), (new_points, 'Після перетворення')]):
#         axis = figure.add_subplot(1, 2, number + 1, projection='3d')
#         axis.scatter(points[0, ::step], points[1, ::step], points[2, ::step],
#                      c=points[2, ::step], cmap='viridis', s=2)
#         axis.set_xlim(-biggest, biggest)
#         axis.set_ylim(-biggest, biggest)
#         axis.set_zlim(-biggest, biggest)
#         axis.set_xlabel('X')
#         axis.set_ylabel('Y')
#         axis.set_zlabel('Z')
#         axis.set_title(name)
#
#     figure.suptitle(title)
#
#     saving_picture(figure, filename)
#     if show_windows:
#         plt.show()
#     plt.close(figure)

import os
import numpy as np
import matplotlib.pyplot as plt

# Якщо не хочеш щоб вікна з графіками відкривались - постав False (картинки все одно збережуться).
show_windows = True

results_folder = 'results'


def saving_picture(figure, filename):
    os.makedirs(results_folder, exist_ok=True)
    figure.savefig(os.path.join(results_folder, filename), dpi=120, bbox_inches='tight')


def matrix_to_text(matrix):
    # Перетворює матрицю у гарний текст для підпису на картинці.
    # Кожен рядок матриці - окремий рядок тексту, числа з 3 знаками після коми.
    lines = []
    for row in matrix:
        lines.append('[ ' + '  '.join(f'{number:8.3f}' for number in row) + ' ]')
    return 'Матриця перетворення:\n' + '\n'.join(lines)


def printing_matrix(title, matrix):
    print('=' * 50)
    print(title)
    print('Матриця перетворення:')
    print(np.round(matrix, 4))
    print()


def drawing_2d_picture(original_points, new_points, matrix, title, filename):
    # original_points і new_points мають форму (2, N)
    printing_matrix(title, matrix)

    figure, axis = plt.subplots(figsize=(7, 8))
    figure.subplots_adjust(bottom=0.22)   # місце знизу під матрицю

    axis.fill(original_points[0], original_points[1], color='gray', alpha=0.4, label='Оригінал')
    axis.fill(new_points[0], new_points[1], color='blue', alpha=0.4, label='Після перетворення')

    axis.axhline(0, color='black', linewidth=0.5)
    axis.axvline(0, color='black', linewidth=0.5)
    axis.set_aspect('equal')
    axis.grid(True, alpha=0.3)
    axis.set_title(title)
    axis.legend()

    # Матриця прямо на картинці
    figure.text(0.5, 0.03, matrix_to_text(matrix), ha='center', va='bottom',
                family='monospace', fontsize=11)

    saving_picture(figure, filename)
    if show_windows:
        plt.show()
    plt.close(figure)


def drawing_3d_picture(original_points, new_points, matrix, title, filename):
    # original_points і new_points мають форму (3, N)
    printing_matrix(title, matrix)

    figure = plt.figure(figsize=(12, 7.5))
    figure.subplots_adjust(bottom=0.2)   # місце знизу під матрицю

    # Щоб не малювати сотні тисяч точок - беремо кожну n-ту
    step = max(1, original_points.shape[1] // 20000)

    # Однакові межі для обох графіків, щоб було видно, що модель реально повернулась
    biggest = max(np.abs(original_points).max(), np.abs(new_points).max())

    for number, (points, name) in enumerate([(original_points, 'Оригінал'), (new_points, 'Після перетворення')]):
        axis = figure.add_subplot(1, 2, number + 1, projection='3d')
        axis.scatter(points[0, ::step], points[1, ::step], points[2, ::step],
                     c=points[2, ::step], cmap='viridis', s=2)
        axis.set_xlim(-biggest, biggest)
        axis.set_ylim(-biggest, biggest)
        axis.set_zlim(-biggest, biggest)
        axis.set_xlabel('X')
        axis.set_ylabel('Y')
        axis.set_zlabel('Z')
        axis.set_title(name)

    figure.suptitle(title)

    # Матриця прямо на картинці
    figure.text(0.5, 0.02, matrix_to_text(matrix), ha='center', va='bottom',
                family='monospace', fontsize=11)

    saving_picture(figure, filename)
    if show_windows:
        plt.show()
    plt.close(figure)