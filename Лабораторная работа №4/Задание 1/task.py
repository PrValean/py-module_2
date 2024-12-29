class ScourgeCharacter:
    """
    Базовый класс для персонажей армии плети:

    Attributes:
        name (str): Имя персонажа
        level (int): Уровень персонажа
        health (int): Здоровье персонажа
        reagents (int): Кол-во реагентов
        quests (list): Список квестов, выполненных персонажем
    """

    def __init__(self, name: str, level: int, health: int, reagents: int) -> None:
        self.name = name
        self.level = level
        self.health = health
        self.reagents = reagents
        self.quests = []

    def raise_dead(self) -> str:
        """Воскрешает друга"""
        return f"{self.name} прибыл на помощь!"

    def complete_quest(self, quest_name: str) -> str:
        """Выполняет квест и добавляет его в список выполненных"""
        self.quests.append(quest_name)
        return f"{self.name} выполнил квест '{quest_name}'!"

    def __str__(self) -> str:
        """Возвращает строковое представление персонажа"""
        return (
            f"Персонаж: {self.name}, Уровень: {self.level}, "
            f"Здоровье: {self.health}, Кол-во реагентов: {self.reagents}, "
            f"Выполненные квесты: {self.quests}"
        )

    def __repr__(self) -> str:
        """Возвращает неформальное строковое представление персонажа"""
        return (
            f"ScourgeCharacter(name={self.name}, level={self.level}, "
            f"health={self.health}, reagents={self.reagents}, "
            f"quests={self.quests})"
        )
        

class DeathKnight(ScourgeCharacter):
    """
    Дочерний класс Scourge для дк:

    Attributes:
        runic_power (int): руны дк
    """

    def __init__(self, name: str, level: int, health: int, runic_power: int, reagents: int) -> None:
        super().__init__(name, level, health, reagents)
        self.runic_power = runic_power

    def raise_dead(self) -> str:
        """Призывает друга с учетом кол-ва реагентов"""
        if self.reagents >= 1:
            self.reagents -= 1
            return f"{self.name} пришел на помощь, повелитель!"
        else:
            return f"{self.name} не хватает реагентов для призыва!"

    def death_coil(self) -> str:
        """Использование лика (способности) дк-а"""
        if self.runic_power >= 40:
            self.runic_power -= 40
            return f"Успешно применено"
        else:
            return f"Недостаточно рун"

    def __str__(self) -> str:
        """Возвращает строковое представление рыцаря с учетом рун"""
        base_str = super().__str__()
        return f"{base_str}, Руны: {self.runic_power}"

    def __repr__(self) -> str:
        """Возвращает неформальное строковое представление рыцаря с учетом рун"""
        base_str = super().__str__()
        return f"ScourgeCharacter({base_str}, runic_power={self.runic_power})"
