import pytest
from src.vacancy import Vacancy


@pytest.fixture()
def test_vacancy_1():
    vacancy = Vacancy(title="Тестовая вакансия один", url="https://www.google.com/",
                      salary={'min': 1000, 'max': 10000, 'currency': "rub"}, pub_date="2023-05-28", requirements="git")
    return vacancy


@pytest.fixture()
def test_vacancy_2():
    vacancy = Vacancy(title="Тестовая вакансия два", url="https://www.google.com/",
                      salary={'min': 100, 'max': 5000, 'currency': "rub"}, pub_date="2023-05-28", requirements="git")
    return vacancy


@pytest.fixture()
def test_vacancy_3():
    vacancy = Vacancy(title="Тестовая вакансия три", url="https://www.google.com/",
                      salary={'min': 100, 'max': 5000, 'currency': "rub"}, pub_date="2023-05-28", requirements="git")
    return vacancy


def test_vacancy_init(test_vacancy_1):
    assert test_vacancy_1.title == "Тестовая вакансия один"
    assert test_vacancy_1.url == "https://www.google.com/"
    assert test_vacancy_1.salary == {'min': 1000, 'max': 10000, 'currency': "rub"}
    assert test_vacancy_1.pub_date == "2023-05-28"
    assert test_vacancy_1.requirements == "git"


def test_vacancy_str(test_vacancy_1):
    assert str(test_vacancy_1) == 'Вакансия "Тестовая вакансия один" от 2023-05-28, зарплата от 1000 до 10000 rub'


def test_vacancy_repr(test_vacancy_1):
    assert repr(test_vacancy_1) == "Vacancy({'title': 'Тестовая вакансия один', 'url': 'https://www.google.com/', " \
                                   "'salary': {'min': 1000, 'max': 10000, 'currency': 'rub'}, 'pub_date': " \
                                   "'2023-05-28', 'requirements': 'git'})"


def test_salary_medium_salary(test_vacancy_1):
    assert test_vacancy_1.medium_salary == 5500


def test_vacancy_eq(test_vacancy_1, test_vacancy_2, test_vacancy_3):
    assert not test_vacancy_1 == test_vacancy_2
    assert test_vacancy_2 == test_vacancy_3


def test_salary_lt(test_vacancy_1, test_vacancy_2, test_vacancy_3):
    assert not test_vacancy_1 < test_vacancy_2
    assert not test_vacancy_2 < test_vacancy_3
    assert test_vacancy_2 < test_vacancy_1


def test_salary_gt(test_vacancy_1, test_vacancy_2, test_vacancy_3):
    assert test_vacancy_1 > test_vacancy_2
    assert not test_vacancy_2 > test_vacancy_3
