import doctest


class GameMetric:
    def __init__(self, player_name: str, score: int, level: int):
        """
        Инициализация данных игрока.

        :param player_name: Имя игрока
        :param score: Очки игрока (должны быть неотрицательными)
        :param level: Уровень игрока (должен быть неотрицательным и не выше 80)
        """
        if score < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        if level <= 0:
            raise ValueError("Уровень должен быть положительным числом.")
        if level > 80:
            raise ValueError("Уровень не может превышать 80.")

        self.player_name = player_name
        self.score = score
        self.level = level

    def update_score(self, points: int == 0) -> str:
        """
        Обновление очков игрока.

        :param points: Количество очков для добавления (должно быть неотрицательным)
        :return: Сообщение о новом счете
        """
        if points < 0:
            raise ValueError("Количество очков для добавления не может быть отрицательным.")

        self.score += points
        return f'Новый счет игрока {self.player_name}: {self.score}.'

    def level_up(self) -> str:
        """
        Повышение уровня игрока.

        :return: Сообщение о повышении лвл или об ошибке
        """
        if self.level < 80:
            self.level += 1
            return f'Поздравляем, {self.player_name}! Вы апнулись до {self.level}.'
        else:
            return f'{self.player_name}, вы уже на макс уровне (80), пора в ЦЛК, хватит сидеть в Вайтране!'


class Truck:
    def __init__(self, model: str, year: int, capacity: float):
        """
        Инициализация грузовика.

        :param model: Модель грузовика
        :param year: Год выпуска (должен быть не позже текущего года)
        :param capacity: Грузоподъемность в тоннах (должна быть положительной)
        """
        from datetime import datetime
        current_year = datetime.now().year

        if year > current_year:
            raise ValueError("Год выпуска не может быть позже текущего года.")
        if capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительной.")

        self.model = model
        self.year = year
        self.capacity = capacity

    def load(self, weight: float) -> str:
        """
        Загрузка груза в грузовик.

        :param weight: Вес груза в тоннах (должен быть положительным)
        :return: Сообщение о загрузке груза
        """
        if weight <= 0:
            raise ValueError("Вес груза должен быть положительным.")
        if weight > self.capacity:
            raise ValueError("Вес груза превышает грузоподъемность грузовика.")

        return f'Груз успешно загружен в {self.model}.'

    def upgrade_capacity(self, additional_capacity: float) -> str:
        """
        Обновление грузоподъемности грузовика в рамках модернизации.

        :param additional_capacity: Дополнительная грузоподъемность в тоннах (должна быть положительной)
        :return: Сообщение об обновлении грузоподъемности
        """
        if additional_capacity <= 0:
            raise ValueError("Дополнительная грузоподъемность должна быть положительной.")

        self.capacity += additional_capacity
        return f'Грузоподъемность грузовика {self.model} обновлена до {self.capacity} тонн.'


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц (должно быть положительным числом)
        :raises ValueError: Если количество страниц не положительное
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Кол-во страниц, которые надо еще прочитать.

        :param pages_read: Количество страниц уже прочитанных (должно быть положительным числом)
        :return: Сообщение о том, сколько страниц осталось
        """
        if pages_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")
        if pages_read > self.pages:
            raise ValueError("Количество прочитанных страниц больше, чем самих страниц книги")
        unread_pages = self.pages - pages_read
        return f'Вам осталось прочитать {unread_pages}'

    def show_author(self) -> str:
        """
        Возвращает читателю имя автора

        :return: self.author
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.show_author()
        'George Orwell'
        """
        return self.author


if __name__ == "__main__":
    doctest.testmod()
