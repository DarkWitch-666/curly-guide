import random

from colorama import Fore, Style

from generators.address import Address
from generators.coordinate import Coordinate
from generators.creditcard import CreditCard
from generators.dateofbrith import DateOfBrith
from generators.email import Email
from generators.name import Name
from generators.password import Password
from generators.username import UserName
from generators.phone import Phone

def color():
    return random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA])

def ru_generator(col):
    for i in range(col):
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print(f'''
{color()}ФИО: {Style.RESET_ALL}{Name.ru_name()};
{color()}Дата рождения: {Style.RESET_ALL}{DateOfBrith.dateofbrith()};
{color()}Адрес: {Style.RESET_ALL}{Address.ru_address()};
{color()}Номер телефона: {Style.RESET_ALL}{Phone.ru_phone()};
{color()}UserName: {Style.RESET_ALL}{UserName.username()};
{color()}Email: {Style.RESET_ALL}{Email.ru_email()};
{color()}Пароль: {Style.RESET_ALL}{Password.password()};
{color()}Кординаты: {Style.RESET_ALL}{Coordinate.ru_coordinate()};
{color()}Кредитная карта: {Style.RESET_ALL}{CreditCard.ru_creditcard()}.
        ''')
def en_generator(col):
    for _ in range(col):
        print ('''
~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print(f'''
{color()}Name: {Style.RESET_ALL}{Name.en_name()};
\n{color()}Date of birth: {Style.RESET_ALL}{DateOfBrith.dateofbrith()};
\n{color()}Address: {Style.RESET_ALL}{Address.en_address()};
\n{color()}Phone: {Style.RESET_ALL}{Phone.ru_phone()};
\n{color()}UserName: {Style.RESET_ALL}{UserName.username()};
\n{color()}Email: {Style.RESET_ALL}{Email.ru_email()};
\n{color()}Password: {Style.RESET_ALL}{Password.password()};
\n{color()}Coordinate: {Style.RESET_ALL}{Coordinate.ru_coordinate()};
\n{color()}Credit Card: {Style.RESET_ALL}
{CreditCard.en_creditcard()}.
        ''')
print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~
''')