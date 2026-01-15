import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    """desc"""
    while True:
        print("\n\tStore Menu\n\t----------")
        print("1.\tList all products in store")
        print("2.\tShow total amount in store")
        print("3.\tMake an order")
        print("4.\tQuit\n")
        user_choice = input("Enter your choice (1-4): ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue
        if user_choice < 1 or user_choice > 4:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue
        if user_choice == 1:
            print("\t------")
            for index, product in enumerate(store.get_all_products(), start=1):
                print(f"{index}.\t", end="")
                product.show()
            print("\t------")

        elif user_choice == 2:
            print(f"\nTotal of {store.get_total_quantity()} items in store")

        elif user_choice == 3:
            products = store.get_all_products()
            print("\t------")
            for index, product in enumerate(store.get_all_products(), start=1):
                print(f"{index}.\t", end="")
                product.show()
            print("\t------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []

            while True:
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break

                try:
                    product_index = int(product_choice) - 1
                    if product_index < 0 or product_index >= len(products):
                        print("Invalid product number.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                quantity_choice = input("What amount do you want? ")
                try:
                    quantity = int(quantity_choice)
                    if quantity <= 0:
                        print("Quantity must be positive.")
                        continue
                except ValueError:
                    print("Please enter a valid quantity.")
                    continue

                shopping_list.append((products[product_index], quantity))
                print("Product added to list!\n")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Order made! Total payment: ${total_price}")
                except Exception as e:
                    print(f"Error while ordering: {e}")

        elif user_choice == 4:
            break


if __name__ == "__main__":
    start(best_buy)