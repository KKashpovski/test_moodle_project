[![Build Status](https://app.travis-ci.com/KKashpovski/test_moodle_project.svg?token=JREwhsNjey9LCigDtVj6&branch=master)](https://app.travis-ci.com/KKashpovski/test_moodle_project)

# Тестирование самой популярной в мире системы управления обучением - Moodle.
![moodle_logo_small](https://user-images.githubusercontent.com/87300748/131994134-bdfd8bf2-db44-469c-8a73-7a5493cabf6e.png)

## Статус компонента
***
CREATED — микросервис создан, но в производстве нет версий. Пока не планируется запускать его в производство. Никаких ограничений не предусмотрено.

## Владелец компонента
***
Кашапова Ксения

## Описание компонентов
***
В рамках компонента будет проведено тестирование следующих задач:
* Позитивные и негативные тесты на авторизацию пользователя
* Обновление личных данных
* Добавление личных данных
* Добавление нового курса
***
Этот компонент разработан для автоматизированного UI тестирования сайта:
https://qacoursemoodle.innopolis.university/

## Описание функциональности
***
Разработанный компонент минимизирует трудозатраты человека на ручное тестирование путем написанных автоматизированных тестов для проведения позитивных и негативных сценариев ввода данных

## Инструкция по использованию, сборке и развертыванию
***
Для применения разработанного компонента потребуется
1. Установка программ:
* PyCharm
* Browser
2. Установка Tools:
* Allure
***
Для сборки и развертывания потребуется выполнить следующее:
1. Открыть PyCharm

Use python 3.9 +
Create and activate virtual environments

```
python -m venv venv
venv\Scripts\activate.bat
```

2. Клонировать проект на локальный ПК с удаленного репозитория

```
git clone https://github.com/KKashpovski/test_moodle_project.git
```

3. Установить Allure. Для этого нужно выполнить все инструкции, указанные в https://docs.qameta.io/allure/

```
pip install allure-pytest
```

```
py.test --alluredir=allure_result_folder ./tests
```

4. Установить все зависимости:

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

5. Запустить pytest:

Запуск тестов 
```
pytest tests/
```

или выполнить запуск тестов с выводом отчетов allure
```
allure serve allure_result_folder
```

## Ссылки на документацию
***
Ссылка, где можно скачать всю документацию:
https://github.com/KKashpovski/test_moodle_project
