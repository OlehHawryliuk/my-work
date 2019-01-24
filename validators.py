"""
    Написати валідатор номера
    Правило валідації
    АА_№_8 цифр
"""

import re

def getUserNumber():

    user_input = input('Enter you number:\n')

    if (re.match(r"^[A-Z]{2}\ \№\ \d{8}$", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор дисципліни
    Правило валідації
    Назва дисципліни не містить більше 10 літер перша з яких велика.
"""

def getClassName():
    user_input = input('Enter you class name:\n')

    if (re.match(r"^[A-Z]+[a-z]+ {1,10} $", user_input)):
        return user_input
    else:
        return False




"""
    Написати валідатор теми
    Правило валідації
    Теми це множина слів де усі літери маленькі.
"""


def getTopicsName():
    user_input = input('Enter you topic name:\n')

    if (re.match(r"^[a-z]+$", user_input)):
        return user_input
    else:
        return False
