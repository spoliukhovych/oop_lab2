# Алгоритм пошуку мінімального елементу з використанням паттерну Builder
class MinElementBuilder:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def find_min_element(self):
        min_element = min(self.data)
        # print(f"Найменший елемент: {min_element}") #консоль
        return min_element

# Клас, що використовується для створення та використання об'єкта пошуку найменшого елемента
class MinElementDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, data):
        self.builder.set_data(data)
        # self.builder.find_min_element()   # консоль
        return self.builder.find_min_element()

if __name__ == '__main__':
    builder = MinElementBuilder()
    director = MinElementDirector(builder)
    data = input("Введите элементы списка (через запятую): ")
    data = data.split(",")
    data = [int(x) for x in data]
    # data = [593, 234, 23, 67, 43, 56]
    # director.construct(data)    # консоль
    print(director.construct(data))