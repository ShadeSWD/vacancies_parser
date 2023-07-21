from src.vacancy import Vacancy
from src.api.hh_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI


class VacanciesParserApp:
    def __init__(self):
        self.__vacancies: list['Vacancy'] = []
        self.__job_title: str | None = None
        self.__amount_vacancy: int | None = None
        self.__available_sites = {'1': 'HeadHunter', '2': 'SuperJob'}
        self.__site_to_parse = None

    def interact_with_user(self):
        """ Взаимодействие с пользователем. """
        while True:
            print("""\n1. Поиск вакансий\n2. Отобразить вакансии\n3. Сохранить вакансии в файл\n4. Выход""")
            choice_menu = input("Выберите действие: ")

            if choice_menu == "1":
                self.search_vacancies()
                self.sort_vacancies()

            elif choice_menu == "2":
                self.display_vacancies()

            elif choice_menu == "3":
                self.save_vacancies_to_file()

            elif choice_menu == "4":
                break
            else:
                print("Ошибка ввода")

    def search_vacancies(self) -> None:
        """Собирает вакансии по выбранным критериям"""

        self.__job_title = input("\nВведите должность для поиска: ")
        self.__amount_vacancy = int(input("Введите количество вакансий для поиска: "))
        self.choose_platform()

        self.__vacancies = self.__site_to_parse.search_vacancies(job_title=self.__job_title,
                                                                 number_of_vacancies=self.__amount_vacancy)

    def choose_platform(self):
        """Выбор онлайн-платформы"""

        while True:
            print("\nДоступные платформы:")
            for number, site in self.__available_sites.items():
                print(f"{number}. {site}")
            site_to_parse = input("Выберите платформу: ")
            if site_to_parse == '1':
                self.__site_to_parse = HeadHunterAPI()
                break
            elif site_to_parse == '2':
                self.__site_to_parse = SuperJobAPI()
                break
            else:
                print("Ошибка ввода")

    def sort_vacancies(self) -> None:
        """Сортировка вакансий по выбранным критериям"""

        while True:
            print("""\n1. Сортировка по дате\n2. Сортировка по окладу""")
            choice_sorted = input("Выберите сортировку: ")
            if choice_sorted == "1":
                self.sort_vacancies_by_date()
                break
            elif choice_sorted == "2":
                self.sort_vacancies_by_salary()
                break
            else:
                print("Ошибка ввода")

    def filter_vacancies(self) -> None:
        """Фильтрация вакансий по названию профессии"""
        self.__vacancies = list(filter(lambda x: self.__job_title.lower() in x.title.lower() and x.salary is not None,
                                       self.__vacancies))

    def sort_vacancies_by_salary(self) -> None:
        """Сортировка вакансий по окладу."""
        self.__vacancies = sorted(self.__vacancies, key=lambda x: x.medium_salary, reverse=True)

    def sort_vacancies_by_date(self) -> None:
        """Сортировка вакансий по дате публикации."""
        self.__vacancies = sorted(self.__vacancies, key=lambda x: x.pub_date, reverse=True)[
                          :self.__amount_vacancy]

    def display_vacancies(self) -> None:
        """Отображение вакансий"""
        if self.__vacancies:
            for vacancy in self.__vacancies:
                print(repr(vacancy))
        else:
            print("\nНет доступных вакансий.")

    def save_vacancies_to_file(self):
        if self.__vacancies:
            print("\nВакансии сохранены в файл.")
        else:
            print("\nНет доступных вакансий для сохранения.")
