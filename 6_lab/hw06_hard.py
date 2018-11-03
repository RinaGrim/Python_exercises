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
        self._name = self.worker[0]
        self._surname = self.worker[1]
        self._salary = int(self.worker[2])
        self._work_post = self.worker[3]
        self._hour_norm = int(self.worker[4])
        self._hours = int(self.worker[5])

    def salary(self):
        if self._hours > self._hour_norm:
            slr = self._salary + 2 * self._salary / self._hour_norm * \
                                       (self._hours - self._hour_norm)
        elif self._hours == self._hour_norm:
            slr = self._salary
        elif self._hours >= 0:
            slr = self._salary * self._hours / self._hour_norm
        else:
            print("Salary can't be less than zero")
        return f"{self._name} {self._surname} received following salary: {slr}"


def main():
    with open("data\\workers", 'r', encoding='utf-8') as f:
        workers = f.read().split('\n')
    workers = [worker.split() for worker in workers]
    with open("data\\hours_of", 'r', encoding='utf-8') as f:
        hours = f.read().split('\n')
    hours = [hour.split() for hour in hours]
    for worker in workers:
        for hour in hours:
            if worker[1] == hour[1]:
                worker.append(hour[2])
    for index in range(1, 7):
        worker = Employee(workers[index])
        print(worker.salary())

if __name__ == '__main__':
    main()