from typing import List


class EducationalInstitution:
    """
    Базовый класс для учебных заведений.
    Определяет общие свойства и методы для всех учебных заведений.
    """

    def __init__(self, name: str, location: str, students_count: int) -> None:
        """
        Инициализирует учебное заведение.

        :param name: Название учебного заведения.
        :param location: Местоположение учебного заведения.
        :param students_count: Количество студентов.
        """
        self.name = name
        self.location = location
        self._students_count = students_count  # Инкапсулированное поле

    def __str__(self) -> str:
        return f"{self.name} ({self.location}) - {self._students_count} студентов"

    def __repr__(self) -> str:
        return f"EducationalInstitution(name={self.name}, location={self.location}, students_count={self._students_count})"

    @property
    def students_count(self) -> int:
        """Возвращает текущее количество студентов."""
        return self._students_count

    @students_count.setter
    def students_count(self, count: int) -> None:
        """Устанавливает количество студентов, если значение не отрицательное."""
        if count < 0:
            raise ValueError("Количество студентов не может быть отрицательным.")
        self._students_count = count

    def enroll_student(self) -> None:
        """Зачисляет нового студента."""
        self._students_count += 1


class School(EducationalInstitution):
    """
    Класс, представляющий школу.
    """

    def __init__(self, name: str, location: str, students_count: int, school_type: str) -> None:
        """
        Инициализирует школу.

        :param name: Название школы.
        :param location: Местоположение школы.
        :param students_count: Количество учеников.
        :param school_type: Тип школы (например, средняя, начальная и т. д.).
        """
        super().__init__(name, location, students_count)
        self.school_type = school_type

    def __str__(self) -> str:
        return f"Школа {self.name} ({self.school_type}, {self.location}) - {self._students_count} учеников"

    def enroll_student(self, age: int) -> None:
        """
        Перегруженный метод зачисления ученика.
        В школы принимают только учеников в возрасте от 6 до 18 лет.

        :param age: Возраст ученика.
        :raises ValueError: Если возраст не находится в диапазоне 6-18 лет.
        """
        if 6 <= age <= 18:
            self._students_count += 1
        else:
            raise ValueError("Возраст ученика должен быть от 6 до 18 лет.")


class University(EducationalInstitution):
    """
    Класс, представляющий университет.
    """

    def __init__(self, name: str, location: str, students_count: int, faculties: List[str]) -> None:
        """
        Инициализирует университет.

        :param name: Название университета.
        :param location: Местоположение университета.
        :param students_count: Количество студентов.
        :param faculties: Список факультетов университета.
        """
        super().__init__(name, location, students_count)
        self.faculties = faculties

    def __str__(self) -> str:
        return f"Университет {self.name} ({self.location}) - {self._students_count} студентов, факультеты: {', '.join(self.faculties)}"

    def enroll_student(self, entrance_exam_passed: bool) -> None:
        """
        Перегруженный метод зачисления студента.
        В университет можно поступить только при успешной сдаче экзамена.

        :param entrance_exam_passed: Результат сдачи вступительного экзамена.
        :raises ValueError: Если экзамен не был сдан.
        """
        if entrance_exam_passed:
            self._students_count += 1
        else:
            raise ValueError("Поступление невозможно без успешной сдачи экзаменов.")
