if __name__ == "__main__":
    from typing import List


    class EducationalInstitution:
        """
        Базовый класс для учебных заведений.
        Определяет общие свойства и методы для всех учебных заведений.
        """

        def __init__(self, name: str, location: str, students_count: int) -> None:
            self.name = name
            self.location = location
            self._students_count = students_count  # Инкапсулируем, чтобы контролировать изменение

        def __str__(self) -> str:
            return f"{self.name} ({self.location}) - {self._students_count} студентов"

        def __repr__(self) -> str:
            return f"EducationalInstitution(name={self.name}, location={self.location}, students_count={self._students_count})"

        def get_students_count(self) -> int:
            """Возвращает текущее количество студентов."""
            return self._students_count

        def enroll_student(self) -> None:
            """Зачисляет нового студента."""
            self._students_count += 1


    class School(EducationalInstitution):
        """
        Дочерний класс, представляющий школу.
        """

        def __init__(self, name: str, location: str, students_count: int, school_type: str) -> None:
            super().__init__(name, location, students_count)
            self.school_type = school_type

        def __str__(self) -> str:
            return f"Школа {self.name} ({self.school_type}, {self.location}) - {self._students_count} учеников"

        def enroll_student(self, age: int) -> None:
            """
            Перегруженный метод зачисления студента.
            В школах можно зачислять только учеников определенного возраста.
            """
            if 6 <= age <= 18:
                self._students_count += 1
            else:
                raise ValueError("Возраст ученика должен быть от 6 до 18 лет.")


    class University(EducationalInstitution):
        """
        Дочерний класс, представляющий университет.
        """

        def __init__(self, name: str, location: str, students_count: int, faculties: List[str]) -> None:
            super().__init__(name, location, students_count)
            self.faculties = faculties

        def __str__(self) -> str:
            return f"Университет {self.name} ({self.location}) - {self._students_count} студентов, факультеты: {', '.join(self.faculties)}"

        def enroll_student(self, entrance_exam_passed: bool) -> None:
            """
            Перегруженный метод зачисления студента.
            В университет можно поступить только при успешной сдаче экзамена.
            """
            if entrance_exam_passed:
                self._students_count += 1
            else:
                raise ValueError("Поступление невозможно без успешной сдачи экзаменов.")


    pass
