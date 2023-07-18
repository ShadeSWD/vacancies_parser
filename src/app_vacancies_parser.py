from src.vacancy import Vacancy


class VacanciesParserApp:
    __vacancies: list['Vacancy'] = []
    __job_title: str | None = None
    __amount_vacancy: int | None = None

    @classmethod
    def interact_with_user(cls) -> None:
        """ Взаимодействие с пользователем. """
        while True:
            print("""\n1. Поиск вакансий\n2. Отобразить вакансии\n3. Сохранить вакансии в файл\n4. Выход""")
            choice_menu = input("Выберите действие: ")

            if choice_menu == "1":
                cls.__job_title = input("\nВведите должность для поиска: ")
                # cls.search_vacancies()
                cls.__amount_vacancy = int(input("Введите количество вакансий для поиска: "))

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

            elif choice_menu == "2":
                pass
                # cls.display_vacancies()
            elif choice_menu == "3":
                if cls.__vacancies:
                    # cls.save_vacancies_to_files()
                    print("\nВакансии сохранены в файл.")
                else:
                    print("\nНет доступных вакансий для сохранения.")
            elif choice_menu == "4":
                break
            else:
                print("Ошибка ввода")
