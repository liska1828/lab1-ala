from lynx_data import getting_lynx_points
from reading_off_file import getting_3d_points_from_off
from task1 import running_task_1
from task2 import running_task_2
from task3 import running_task_3
from task4 import running_task_4

# Шлях до .off файлу з датасету ModelNet40 (див. інструкцію: скачати з Kaggle і розпакувати).
# Поклади папку ModelNet40 поруч з main.py - тоді шлях буде саме такий:
off_file_path = 'ModelNet40/airplane/test/airplane_0627.off'

# Постав False, якщо якусь частину запускати не треба
run_part_1 = True
run_part_2 = True

if __name__ == '__main__':
    if run_part_1:
        lynx = getting_lynx_points()  # форма (2, N)
        running_task_1(lynx)
        running_task_2(lynx)

    if run_part_2:
        airplane = getting_3d_points_from_off(off_file_path)  # форма (3, N)
        running_task_3(airplane)
        running_task_4(airplane)