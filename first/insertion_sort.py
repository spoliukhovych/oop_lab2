# Алгоритм cортування вставкою з використанням патернів Strategy та Factory Method
class InsertionSort:
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

# Factory, що використовується для створення об'єктів алгоритмів сортування
class SortingAlgorithmFactory:
    def create_algorithm(self, algorithm_type):
        if algorithm_type == 'insertion':
            return InsertionSort()

# Клас, який використовує обраний алгоритм сортування
class SortingClient:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def sort_data(self, data):
        self.algorithm.sort(data)

if __name__ == '__main__':
    data = input("Введите элементы списка (через запятую): ")
    data = data.split(",")
    data = [int(x) for x in data]
    # data = [5, 2, 7, 1, 8]
    algorithm_factory = SortingAlgorithmFactory()
    algorithm = algorithm_factory.create_algorithm('insertion')
    client = SortingClient(algorithm)
    # data = [325345, 343, 3232, 3233, 5546, 23]
    client.sort_data(data)
    print(data)

