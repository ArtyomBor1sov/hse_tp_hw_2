import matplotlib.pyplot as plt
from HW_2 import _sum
from time import time

def draw_plot(x, y, plot_title, x_label):
    plt.gcf().canvas.set_window_title('График времени работы программы')
    plt.grid(True)
    plt.plot(x, y, color = 'black')
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel('Время работы программы (c)')
    plt.show()

if __name__ == '__main__':
    amount_of_nums = []
    running_time = []
    for i in range(1, 9):
        file = open(f'text_files/nums_{i}.txt', 'r')
        data = [int(x) for x in file.readline().split()]
        file.close()
        if i < 4:
            k = 1000
        elif i < 5:
            k = 100
        elif i < 7:
            k = 10
        else:
            k = 1
        start_time = time()
        for i in range(k):
            _sum(data)
        end_time = time()
        curr_amount_of_nums = len(data)
        curr_running_time = (end_time - start_time) / k
        print(f'Время вычисления суммы для {curr_amount_of_nums} чисел: {curr_running_time} c.')
        amount_of_nums.append(curr_amount_of_nums)
        running_time.append(curr_running_time)
    draw_plot(amount_of_nums, running_time,
              'Зависимость времени работы программы от количества чисел',
              'Количество чисел')
    power_of_two = [0]
    running_time = [curr_running_time]
    step = 25
    for k in range(step, 501, step):
        for i in range(len(data)):
            data[i] *= 2 ** step
        start_time = time()
        _sum(data)
        end_time = time()
        curr_running_time = (end_time - start_time)
        power_of_two.append(k)
        running_time.append(curr_running_time)
        print(f'Время вычисления суммы для {curr_amount_of_nums} чисел (каждое умножено на 2^{k}): {curr_running_time} c.')
    draw_plot(power_of_two, running_time,
              'Зависимость времени работы программы от увеличения разрядности',
              'Степень двойки')
