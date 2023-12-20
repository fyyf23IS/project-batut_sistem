class Manager:
    def __init__(self):
        self.clients = []

    def add_client(self, name):
        self.clients.append(name)
        print("Клиент успешно добавлен.")

    def print_clients(self):
        print("Список клиентов:")
        for client in self.clients:
            print(client)

    def interact_with_clients(self):
        while True:
            print("1. Взаимодействовать с клиентом")
            print("0. Вернуться в главное меню")

            choice = input("Введите номер операции: ")

            if choice == "1":
                self.interact_with_client()
            elif choice == "0":
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

    def interact_with_client(self):
        client_name = input("Введите имя клиента: ")
        if client_name in self.clients:
            print(f"Вы взаимодействуете с клиентом {client_name}.")
            # здесь можно добавить логику взаимодействия с клиентом
        else:
            print("Клиент не найден.")


class Trade:
    def __init__(self):
        self.manager = Manager()
        self.loyalty = []
        self.abonements = []
        self.history = []
        self.instructors = []

    def main_menu(self):
        while True:
            print("1. Добавить клиента")
            print("2. Добавить лояльность")
            print("3. Добавить абонемент")
            print("4. Добавить историю")
            print("5. Добавить инструктора")
            print("6. Вывести информацию")
            print("7. Взаимодействовать с клиентами")
            print("0. Выход")

            choice = input("Введите номер операции: ")

            if choice == "1":
                client_name = input("Введите имя клиента: ")
                self.manager.add_client(client_name)
            elif choice == "2":
                loyalty_points = input("Введите количество лояльных баллов: ")
                self.loyalty.append(loyalty_points)
                print("Лояльность успешно добавлена.")
            elif choice == "3":
                abonement_type = input("Введите тип абонемента: ")
                self.abonements.append(abonement_type)
                print("Абонемент успешно добавлен.")
            elif choice == "4":
                history_details = input("Введите детали истории: ")
                self.history.append(history_details)
                print("История успешно добавлена.")
            elif choice == "5":
                instructor_name = input("Введите имя инструктора: ")
                self.instructors.append(instructor_name)
                print("Инструктор успешно добавлен.")
            elif choice == "6":
                self.manager.print_clients()
                self.print_info()
            elif choice == "7":
                self.manager.interact_with_clients()
            elif choice == "0":
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

    def print_info(self):
        print("Список лояльности:")
        for loyalty in self.loyalty:
            print(loyalty)

        print("Список абонементов:")
        for abonement in self.abonements:
            print(abonement)

        print("Список истории:")
        for history in self.history:
            print(history)

        print("Список инструкторов:")
        for instructor in self.instructors:
            print(instructor)


trade = Trade()
trade.main_menu()