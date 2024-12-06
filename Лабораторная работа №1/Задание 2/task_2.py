from task_1 import GameMetric, Truck, Book

if __name__ == "__main__":
    player = GameMetric("Alice", 100, 10)
    truck = Truck("Volvo FH", 2020, 20)
    book = Book("1984", "George Orwell", 328)

    try:
        player.update_score(-50)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        truck.load(25)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        book.read(400)
    except ValueError:
        print('Ошибка: неправильные данные')
