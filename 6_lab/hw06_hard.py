# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Employee(object):
    def __init__(self, worker):
        self.worker = worker
    def zarplata(self):
        if self.worker[4] > self.worker[5]:
            zp = int(self.worker[2]) + 2 * int(self.worker[2]) / int(self.worker[4]) * \
                                       (int(self.worker[5]) - int(self.worker[4]))
        elif self.worker[4] == self.worker[5]:
            zp = int(self.worker[2])
        else:
            zp = int(self.worker[2]) * int(self.worker[5]) / int(self.worker[4])
        return f"{self.worker[0]} {self.worker[1]} получил следующую зарплату: {zp}"


def main():
    with open("data\\workers", 'r', encoding='utf-8') as file:
        text = file.read().split('\n')
    text = [list.split() for list in text]
    with open("data\\hours_of", 'r', encoding='utf-8') as file:
        hours = file.read().split('\n')
    hours = [list.split() for list in hours]
    for list in text:
        for spisok in hours:
            if spisok[0] == list[0]:
                list.append(spisok[2])
    for i in range(1, 7):
        worker = Employee(text[i])
        worker.zarplata()
    # print(text[3])

if __name__ == '__main__':
    main()