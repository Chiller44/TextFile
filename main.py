from datetime import datetime
from idlelib.iomenu import encoding


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.file = self.name + '_transactions.txt'

    def get_now(self):
        return datetime.now().strftime('[%B %d %Y, %H:%M:%S]')

    def deposit(self):
        try:
            dep = int(input(f'{self.name}, введіть суму депозиту: '))
            if dep > 0:
                self.balance += dep
                with open(self.file, 'a', encoding='utf-8') as file:
                    file.write(f'\n{self.get_now()} Депозит на суму {dep}')
                print(f'Депозіт успішний! На Вашому рахунку {self.balance}')
            else:
                print('Сума поповнення повинна бути більше 0')
        except ValueError:
            print('Введіть число')

    def withdraw(self):
        try:
            withdr = int(input(f'{self.name}, введіть сумму для зняття: '))
            if withdr > 0:
                if withdr <= self.balance:
                    self.balance -= withdr
                    with open(self.file, 'a', encoding='utf-8') as file:
                        file.write(f'\n{self.get_now()} Зняття {withdr}')
                    print(f'Зняття успішне! На Вашому рахунку {self.balance}')
                else:
                    print('Недостатньо коштів для зняття')
            else:
                print('Сума для зняття повинна бути більше 0')
        except ValueError:
            print('Введіть число')

    def transfer(self, to_account):
        try:
            transf = int(input(f'{self.name}, введіть сумму для переказу коштів: '))
            if transf >0:
                if transf <= self.balance:
                    self.balance -= transf
                    to_account.balance += transf
                    with open(self.file, 'a', encoding='utf-8') as file, open(to_account.name + '_transactions.txt', 'a', encoding='utf-8') as file1:
                        file.write(f'\n{self.get_now()} Переказ {transf} для {to_account.name}')
                        file1.write(f'\n{self.get_now()} Поповнення {transf} від {self.name}')
                    print(f'Переказ успішний! На Вашому рахунку {self.balance}')
                else:
                    print('Недостатньо коштів для зняття')
            else:
                print('Сума для переказу повинна бути більше 0')

        except ValueError:
            print('Введіть число')

    def info(self, month, year):
        try:
            with (open(self.name + '_transactions.txt', 'r', encoding='utf-8') as readfile,
                  open(self.name + '_info.txt', 'w', encoding='utf-8') as infofile):
                reading = readfile.readlines()
                for line in reading:
                    if month.lower() in line.lower() and year in line:
                        infofile.write(line)
        except FileNotFoundError:
            print('Файл транзакцій не знайдено')






andrii = BankAccount('Andrii')
oleh = BankAccount('Oleh')
nadiia = BankAccount('Nadiia')
ihor = BankAccount('Ihor')
andrii.deposit()
andrii.withdraw()
andrii.transfer(oleh)
andrii.transfer(nadiia)
nadiia.transfer(andrii)
andrii.info('june', '2024')







