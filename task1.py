from typing import Union


class Car:
    """
    Класс описывает модель машины.
    """
    def __init__(self, max_speed: Union[int, float], weight: Union[int, float], brand: str):
        """
        Инициализация экземпляра класса.

        :param max_speed: Максимальная скорость машины.
        :param weight: Вес машины.
        :param brand: Название марки машины.

        Example:
        >>> car = Car(250, 2.6, "Lada")
        """
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("max_speed должен быть положительным числом (int или float).")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("weight должен быть положительным числом (int или float).")
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой.")

        self.max_speed = max_speed
        self.weight = weight
        self.brand = brand

    def start(self, flag: bool) -> bool:
        """
        Метод начинает движение машины.

        :param flag: True - начать движение, False - не двигаться.
        :return: Флаг начала движения.

        Example:
        >>> car = Car(250, 2.6, "Lada")
        >>> car.start(True)
        True
        """
        return flag

    def stop(self, flag: bool) -> bool:
        """
        Метод останавливает движение машины.

        :param flag: True - остановиться, False - продолжить движение.
        :return: Флаг остановки.

        Example:
        >>> car = Car(250, 2.6, "Lada")
        >>> car.stop(True)
        True
        """
        return flag


class Box:
    """
    Класс описывает модель коробки.
    """
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Инициализация экземпляра класса.

        :param capacity_volume: Вместимость коробки.
        :param occupied_volume: Объем уже занятых вещей.

        Example:
        >>> box = Box(5.0, 1.0)
        """
        if not isinstance(capacity_volume, (int, float)) or capacity_volume <= 0:
            raise ValueError("capacity_volume должен быть положительным числом.")
        if not isinstance(occupied_volume, (int, float)) or occupied_volume < 0:
            raise ValueError("occupied_volume должен быть неотрицательным числом.")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def put(self, weight_thing: Union[int, float]) -> float:
        """
        Добавляет вещь в коробку.

        :param weight_thing: Вес добавляемой вещи.
        :return: Оставшееся свободное место в коробке.

        Example:
        >>> box = Box(5.0, 1.0)
        >>> box.put(2.0)
        2.0
        """
        if weight_thing < 0:
            raise ValueError("Вес вещи должен быть положительным числом.")
        if self.occupied_volume + weight_thing > self.capacity_volume:
            raise ValueError("Вещь не помещается в коробку.")

        self.occupied_volume += weight_thing
        return self.capacity_volume - self.occupied_volume

    def get(self, weight_thing: Union[int, float]) -> float:
        """
        Извлекает вещь из коробки.

        :param weight_thing: Вес извлекаемой вещи.
        :return: Оставшееся свободное место в коробке.

        Example:
        >>> box = Box(5.0, 3.0)
        >>> box.get(1.0)
        3.0
        """
        if weight_thing < 0:
            raise ValueError("Вес вещи должен быть положительным числом.")
        if weight_thing > self.occupied_volume:
            raise ValueError("Нельзя извлечь больше, чем находится в коробке.")

        self.occupied_volume -= weight_thing
        return self.capacity_volume - self.occupied_volume


class Developer:
    """
    Класс описывает разработчика.
    """
    def __init__(self, desire_to_sleep: float, amount_of_money: int):
        """
        Инициализация экземпляра класса.

        :param desire_to_sleep: Желание спать (от 0.0 до 1.0).
        :param amount_of_money: Количество заработанных денег.

        Example:
        >>> dev = Developer(0.5, 5000)
        """
        if not 0.0 <= desire_to_sleep <= 1.0:
            raise ValueError("Желание спать должно быть от 0.0 до 1.0.")
        if amount_of_money < 0:
            raise ValueError("Количество денег должно быть неотрицательным.")

        self.desire_to_sleep = desire_to_sleep
        self.amount_of_money = amount_of_money

    def sleep(self, time_to_sleep: float, time_to_rise: float) -> float:
        """
        Рассчитывает количество часов сна.

        :param time_to_sleep: Время, когда разработчик ложится спать.
        :param time_to_rise: Время пробуждения.
        :return: Общее количество часов сна.

        Example:
        >>> dev = Developer(0.5, 5000)
        >>> dev.sleep(23.0, 7.0)
        8.0
        """
        return (24 + time_to_rise - time_to_sleep) % 24

    def develop(self, flag: bool) -> bool:
        """
        Метод определяет, будет ли разработчик работать.

        :param flag: True - работать, False - отдыхать.
        :return: Статус работы.

        Example:
        >>> dev = Developer(0.5, 5000)
        >>> dev.develop(True)
        True
        """
        return flag


if __name__ == "__main__":
    import doctest
    doctest.testmod()
