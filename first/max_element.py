# Алгоритм пошуку максимального елементу з використанням паттерну Observer
class MaxElementObserver:
    def update(self, data):
        max_element = max(data)
        # print(f"Максимальний елемент: {max_element}")   # консоль
        return max_element

class MaxElementFinder:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def find_max_element(self, data):
        max_element = max(data)
        observer_= 0
        for observer in self.observers:
            # observer.update(data)   # консоль
            observer_ = observer.update(data)
        return observer_

if __name__ == '__main__':
    finder = MaxElementFinder()
    observer1 = MaxElementObserver()
    observer2 = MaxElementObserver()
    finder.attach(observer1)
    finder.attach(observer2)
    data = input("Введите первый набор данных (через запятую): ")
    data = data.split(",")
    data = [int(x) for x in data]
    # data = [35, 56, 234, 46, 1, 9]
    # finder.find_max_element(data)   # консоль
    print(finder.find_max_element(data))
    finder.detach(observer2)
    data = input("Введите второй набор данных (через запятую): ")
    data = data.split(",")
    data = [int(x) for x in data]
    # data = [5, 2, 7, 1, 8]
    # finder.find_max_element(data)   # консоль
    print(finder.find_max_element(data))
