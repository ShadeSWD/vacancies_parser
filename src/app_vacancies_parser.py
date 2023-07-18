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

                self.__job_title = input("\nВведите должность для поиска: ")
                self.__amount_vacancy = int(input("Введите количество вакансий для поиска: "))

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

                while True:
                    print("""\n1. Сортировка по дате\n2. Сортировка по окладу""")
                    choice_sorted = input("Выберите сортировку: ")
                    if choice_sorted == "1":
                        # cls.sort_vacancies_for_date()
                        break
                    elif choice_sorted == "2":
                        # cls.sort_vacancies_for_salary()
                        break
                    else:
                        print("Ошибка ввода")

                self.search_vacancies()

            elif choice_menu == "2":
                pass
                # cls.display_vacancies()
            elif choice_menu == "3":
                if self.__vacancies:
                    # cls.save_vacancies_to_files()
                    print("\nВакансии сохранены в файл.")
                else:
                    print("\nНет доступных вакансий для сохранения.")
            elif choice_menu == "4":
                break
            else:
                print("Ошибка ввода")

    def search_vacancies(self):
        vacancies = self.__site_to_parse.search_vacancies(job_title=self.__job_title,
                                                          number_of_vacancies=self.__amount_vacancy)
        for vacancy in vacancies:
            print(repr(vacancy))
