"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
class MoneyWorker():
    def __init__(self):
        self.history = []
        self.money = 0
    def add_to_account(self):
        money = input('Введите сумму для пополнения: ')
        while True:
            try:
                self.money += int(money)
                break
            except Exception as err:
                money = input('Введите сумму для пополнения: ')
    def buy_smt(self,):
        ammount_of_purchase = input('Введите сумму покупки: ')
        while True:
            try:
                ammount_of_purchase = int(ammount_of_purchase)
                if ammount_of_purchase > self.money:
                    print('Денег для покупки не хватает')
                    return
                self.__purchase_maker(ammount_of_purchase)
            except Exception as err:
                ammount_of_purchase = input('Введите сумму покупки: ')
    def __purchase_maker(self, money):
        name_of_item = input().strip()
        while name_of_item == "":
            name_of_item = input().strip()
        self.money -= money
        self.history.append([name_of_item, money])
    def get_history(self):
        return json.loads(json.dumps(self.history))
money_worker = MoneyWorker()
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        money_worker.add_to_account()
    elif choice == '2':
        money_worker.buy_smt()
    elif choice == '3':
        history = money_worker.get_history()
        for name, ammount in history:
            print(name, ammount)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
