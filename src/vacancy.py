class Vacancy:
    """Класс, представляющий информацию о вакансии"""

    def __init__(self, title: str, url: str, salary: str, pub_date: str):
        """
        Инициализация объекта Vacancy.

        :param title: Название вакансии.
        :param url: Ссылка на вакансию.
        :param salary: Зарплата.
        :param pub_date: Дата размещения вакансии.
        """
        self.__title = title
        self.__url = url
        self.__salary = salary
        self.__pub_date = pub_date

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def pub_date(self):
        return self.__pub_date

    def __str__(self) -> str:
        """
        Возвращает строковое представление вакансии.

        :return: Строковое представление вакансии.
        """
        return f'Вакансия "{self.title} от {self.__pub_date}"'

    def __repr__(self) -> str:
        """
        Возвращает представление вакансии в виде строки.

        :return: Представление вакансии в виде строки.
        """
        return f"Vacancy(title={self.title}, url={self.url}, salary={self.salary}, pub_date={self.pub_date})"

    def __eq__(self, other: 'Vacancy') -> bool:
        """
        Проверяет, равны ли две вакансии по зарплате.

        :param other: Другая вакансия для сравнения.
        :return: True, если зарплаты равны, иначе False.
        """
        return self.salary == other.salary

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        Определяет порядок сортировки вакансий по зарплате.

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет меньшую зарплату, иначе False.
        """
        return self.salary < other.salary

    def __gt__(self, other: 'Vacancy') -> bool:
        """
        Определяет порядок сортировки вакансий по зарплате.

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет большую зарплату, иначе False.
        """
        return self.salary > other.salary

    @salary.setter
    def salary(self, value: int | float | str) -> None:
        """
        Устанавливает зарплату вакансии.

        :param value: Значение зарплаты.
        """
        self.__salary = round(float(value), 2)

    def validate_salary(self) -> bool:
        """
        Проверяет, является ли зарплата валидной.

        :return: True, если зарплата валидна, иначе False.
        """
        if isinstance(self.salary, (int, float)):
            return True
        elif isinstance(self.salary, str):
            salary_parts = self.salary.split('-')
            if len(salary_parts) == 2:
                min_salary, max_salary = salary_parts
                if min_salary.isdigit() and max_salary.isdigit():
                    return True
        return False

    def validate_data(self) -> bool:
        """
        Проверяет, являются ли все данные вакансии валидными.

        :return: True, если все данные валидны, иначе False.
        """
        if not all([self.title, self.url, self.salary, self.pub_date]):
            return False
        return True
