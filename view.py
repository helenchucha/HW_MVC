'''
View - візуальний інтерфейс для взаємодії з користувачем через консоль.

Цей модуль відповідає за відображення інформації та отримання відповідей від дкористувача.
Всі операції відбуваються через стандартний потік вводу/виводу.

Основні функції:
- display_menu (виводить список меню з назвами та цінами)
- get_user_choice (запитує у користувача ID товару та кількість для замовлення)
- show_order (виводить поточне замовлення з деталізацією та підсумковою сумою)
- show_message (виводить будь-яке повідомлення від програми)
- ask_continue (запитує користувача, чи бажає він додати ще один товар)

Особливості:
- Взаємодіє з моделлю для отримання даних про меню та замовлення.
- Обробляє введення користувача з перевіркою на некоректні дані.
- Виводить повідомлення та підтвердження для користувача.
'''

class ConsoleView:
    def __init__(self, model):
        self.model = model

    def display_menu(self):
        menu = self.model.get_menu()
        print("Меню:")
        for id, item in menu.items():
            print(f"{id}. {item['name']} - {item['price']} грн")
        print()

    def get_user_choice(self):
        try:
            item_id = int(input("Введіть ID товару для додавання до кошика: "))
            quantity = int(input("Введіть кількість: "))
            return item_id, quantity
        except ValueError:
            print("Некоректне введення, спробуйте ще раз.")
            return self.get_user_choice()

    def show_order(self):
        order = self.model.get_order()
        menu = self.model.get_menu()
        print("\nВаше замовлення:")
        total = 0
        for item in order:
            item_info = menu[item['id']]
            subtotal = item_info['price'] * item['quantity']
            total += subtotal
            print(f"{item_info['name']} x {item['quantity']} = {subtotal} грн")
        print(f"Загальна сума: {total} грн\n")

    def show_message(self, message):
        print(message)

    def ask_continue(self):
        return input("Додати ще? (так/ні): ").strip().lower()