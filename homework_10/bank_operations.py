# # Wykorzystując paradygmant programowania obiektowego zamodeluj klasę(y) potrzebne do operacji bankowych:
# #
# #     Możliwość utworzenia nowego konta, które przechowuje informacje dotyczące klienta, stanu konta, oraz waluty w jakiej przechowywane są środki.
# #     Wpłaty środków.
# #     Wypłaty środków.
# #     Ustalanie limitów wypłat.
# #     Przelew z konta A na konto B.
# #     Dodatkowo dla chętnych: historia transakcji tj. wpłaty, wypłaty, przelewy przychodzące i wychodzące w formie raportu do pliku lub podsumowania na ekranie
#
#

class Client:
    def __init__(self, id_no, firstname, lastname, phone_number, balance, currency, withdrawal_limit):
        self.id_no = id_no
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone_number
        self.balance = balance
        self.currency = currency
        self.withdrawal_limit = withdrawal_limit

    def __str__(self):
        return f'{self.id_no} {self.firstname} {self.lastname} {self.phone} {self.balance} {self.currency} {self.withdrawal_limit}'

class BankAccount:
    def __init__(self):
        self.accounts = dict()

    def add_account(self, client):
        self.accounts[client.id_no] = client

    def display_all(self):
        for client_id, client in self.accounts.items():
            print(client)

    def withdraw_money(self, id_no, amount,):
        client = self.accounts[id_no]
        if client.balance > amount:
            if amount < client.withdrawal_limit:
                client.balance = client.balance - amount
            else:
                print('Withdrawal limit exceeded')
        else:
            print('Not enough funds. Operation terminated.')

    def transfer(self, id_no_from, id_no_to, amount):
        from_account = self.accounts[id_no_from]
        to_account = self.accounts[id_no_to]
        if from_account.balance >= amount:
            from_account.balance = from_account.balance - amount
            to_account.balance = to_account.balance + amount
        else:
            print('Not enough funds. Operation terminated.')






if __name__ == '__main__':
    client_1 = Client('120','Jan', 'Pajton', 800800800, 45000, 'PLN', 1000)
    client_2 = Client('223','Anna', 'Siszarp', 454656787, 32000, 'PLN', 2000)
    client_3 = Client('453','Robert', 'Cedwaplusy', 222321908, 99000, 'PLN', 3000)
    client_4 = Client('641','Maria', 'Eskuel', 777867956, 67000, 'PLN', 4000)
    # print(client_1)
    # print(client_2)
    # print(client_3)
    # print(client_4)
    Va_Bank = BankAccount()
    Va_Bank.add_account(client_1)
    Va_Bank.add_account(client_2)
    Va_Bank.add_account(client_3)
    Va_Bank.add_account(client_4)
    Va_Bank.withdraw_money('453',2999)
    Va_Bank.transfer('120','641', 1499)

    client_data = Va_Bank.display_all()
    print(client_data)
    print('-' * 25)

    # print(Va_Bank.display_all())
