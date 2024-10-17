from Store import Store  # Импортируем класс Store из файла Store.py


def main():
    # Создаем три магазина
    store1 = Store("Пятёрочка", "Краснодар, ул. Ленина, 1")
    store2 = Store("Магнит", "Краснодар, ул. Гоголя, 2")
    store3 = Store("Перекресток", "краснодар, ул. Красная, 3")

    # Добавляем пять разных товаров в каждый магазин
    store1.add_item("apples", 0.5)
    store1.add_item("bananas", 0.75)
    store1.add_item("oranges", 0.6)
    store1.add_item("grapes", 1.2)
    store1.add_item("pears", 0.8)

    store2.add_item("milk", 1.0)
    store2.add_item("bread", 1.5)
    store2.add_item("eggs", 2.0)
    store2.add_item("cheese", 3.0)
    store2.add_item("butter", 1.8)

    store3.add_item("cereal", 2.5)
    store3.add_item("rice", 1.0)
    store3.add_item("pasta", 0.9)
    store3.add_item("sugar", 0.4)
    store3.add_item("flour", 0.7)

    # Тестируем методы класса на первом магазине (store1)
    print("Тестируем методы на магазине:", store1.name)

    # Получаем цену товара
    print(f"Цена на яблоки: {store1.get_price('apples')}")

    # Обновляем цену товара
    store1.update_price("apples", 0.55)
    print(f"Новая цена на яблоки: {store1.get_price('apples')}")

    # Удаляем товар
    store1.remove_item("bananas")
    print(f"Цена на бананы: {store1.get_price('bananas')}")  # Должно вернуть None

    # Добавляем новый товар
    store1.add_item("kiwi", 1.5)

    # Проверяем наличие нового товара
    print(f"Цена на киви: {store1.get_price('kiwi')}")

    # Проверяем все товары в магазине
    print("Товары в магазине:")
    for item, price in store1.items.items():
        print(f"{item}: {price}")


if __name__ == "__main__":
    main()
