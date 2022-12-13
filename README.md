# Задание 2 Паралелно търсене

## Условие на задачата
В директорията `src/` има 3 файла с класове:
* result.py - Запазва резултата от търсене
* parallel_single_file_search.py - Паралелно търсене в един файл
* parallel_multiple_files_search.py - Паралелно търсене в множество файлове
Препоръчваме имплементирането им в тази последователност.

Всеки метод/клас/функция имат допълнително описание как трябва да работят.

## Работа със заданието
Препоръчваме използвамето на [Gitpod](https://www.gitpod.io/), за който има автоматична конфигурация на средата.

В противен случай препоръчваме работа UNIX машина (или linux subsystem for windows)

Тези 2 инструмента улесняват работата по задачата (ако не ги ползвате ще трябва да създадете ръчно virtualenv и да пускате тестовете с `python -m pytest`):
- [just](https://github.com/casey/just)
- [direnv](https://direnv.net/)

### Използване на direnv:
В директорията на проекта трябва да включите direnv
```
$ direnv allow
```

### Използване на just
В директорията на проекта може да използвате:

```
$ just test # run all tests
```

```
$ just coverage # generate coverage information for the code
```

```
$ just coverage-html # generate coverage information in a html page (highlighting (un)covered lines)
```

