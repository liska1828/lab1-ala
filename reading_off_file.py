import numpy as np


def reading_off_file(filename: str):
    # Читає .off файл (формат ModelNet40).
    # Повертає: вершини (масив N x 3) і список граней.
    with open(filename, 'r') as f:
        first_line = f.readline().strip()

        # Буває, що перший рядок "OFF", а буває, що "OFF1234 5678 0" (без переносу).
        if not first_line.startswith('OFF'):
            raise ValueError('Це не OFF файл')

        rest_of_first_line = first_line[3:].strip()
        if rest_of_first_line != '':
            numbers_line = rest_of_first_line
        else:
            numbers_line = f.readline().strip()

        number_of_vertices, number_of_faces, _ = map(int, numbers_line.split())

        vertices = []
        for _ in range(number_of_vertices):
            vertices.append(list(map(float, f.readline().strip().split())))

        faces = []
        for _ in range(number_of_faces):
            # перше число в рядку - кількість вершин грані, його пропускаємо
            faces.append(list(map(int, f.readline().strip().split()[1:])))

    return np.array(vertices), faces


def getting_3d_points_from_off(filename: str):
    # Повертає точки у вигляді (3, N): рядки x, y, z - так, як треба для множення матриці на дані.
    vertices, faces = reading_off_file(filename)
    return vertices.T.copy()