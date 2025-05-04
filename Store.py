class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Пример использования
store1 = Store("Магазин А", "ул. Ленина, 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин Б", "ул. Пушкина, 2")
store2.add_item("хлеб", 0.3)
store2.add_item("молоко", 0.8)

store3 = Store("Магазин В", "ул. Горького, 3")
store3.add_item("мясо", 2.5)
store3.add_item("рыба", 3.0)

# Тестирование методов на store1
print(store1)
store1.add_item("груши", 0.6)
print("Цена груш:", store1.get_item_price("груши"))
store1.update_item_price("груши", 0.65)
print("Обновленная цена груш:", store1.get_item_price("груши"))
store1.remove_item("груши")
print("Цена груш после удаления:", store1.get_item_price("груши"))
print(store1)

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Пример использования
store1 = Store("Магазин А", "ул. Ленина, 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин Б", "ул. Пушкина, 2")
store2.add_item("хлеб", 0.3)
store2.add_item("молоко", 0.8)

store3 = Store("Магазин В", "ул. Горького, 3")
store3.add_item("мясо", 2.5)
store3.add_item("рыба", 3.0)

# Тестирование методов на store1
print(store1)
store1.add_item("груши", 0.6)
print("Цена груш:", store1.get_item_price("груши"))
store1.update_item_price("груши", 0.65)
print("Обновленная цена груш:", store1.get_item_price("груши"))
store1.remove_item("груши")
print("Цена груш после удаления:", store1.get_item_price("груши"))
print(store1)

