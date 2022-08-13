import random

famous = {'А.П.Чехов': '29.01.1860', 'П.И.Чайковский': '07.05.1840', 'Д.И.Менделеев': '08.02.1834',
          'А.Н.Толстой': '09.09.1828', 'Ф.М.Достоевский': '11.11.1821', 'Н.И.Пирогов': '25.11.1810',
          'А.С.Пушкин': '26.05.1799', 'В.И.Вернадский': '28.02.1863', 'В.И.Ленин': '22.04.1870',
          'И.В.Сталин': '06.12.1878'}


def add_separators(f):
    def inner():
        print('#' * 10, 'НАЧАЛО', '#' * 10)
        result = f()
        print('#' * 10, 'КОНЕЦ', '#' * 10)
        return result

    return inner


@add_separators
def game():
    total = 10
    score = 0
    while total > 0:
        answer = input('Дата рождения ' + random.choice(list(famous.keys())) + ':')
        if total == 6:
            break
        total -= 1
        for i, j in famous.items():
            if answer == j:
                score += 1
    print('Количество правильных ответов :', score)
    print('Плохой результат , подготовься и приходи снова .' if score <= 2 else 'Хорошо, попробуй еще раз ')
    if score == 5:
        print('Отличный результат !!!')


game()