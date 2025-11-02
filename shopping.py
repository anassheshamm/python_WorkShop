# cart = {}

# def add_item(cart):
#     name = input("Enter the item name: ")
#     price = float(input("Enter the item price: "))
#     quantity = int(input("Enter the item quantity: "))
#     cart[name]= {'price': price, 'quantity': quantity}
#     print(f"Added {quantity} of {name} for ${price} each to the cart")

# def remove_item(cart):
#     name = input("Enter the item name to remove: ")
#     if name in cart:
#         del cart[name]
#         print(f"Removed {name} from the cart")
#     else:
#         print(f"{name} not found in the cart")

# def update_item(cart):
#     name = input("Enter the item name to update: ")
#     if name in cart:
#         quantity = int(input("Enter the new quantity: "))
#         cart[name]['quantity'] = quantity
#         print(f"Updated {name} quantity to {quantity}")
#     else:
#         print(f"{name} not found in the cart")

# def view_cart(cart):
#     if not cart:
#         print("\nYour cart is empty.")
#         return
#     total = 0
#     print("-" * 20)
#     print("\nYour Shopping Cart:")
#     for name, info in cart.items():
#         item_total = info['price'] * info['quantity']
#         total += item_total
#         print(f"{name}: ${info['price']} \nQuantity: {info ['quantity']} \nTotal = ${item_total}")
#     print(f"Total Amount: ${total}")

# def main():
#     while True:
#         print("\nShopping cart options:")
#         print("1.Add item")
#         print("2.Remove item")
#         print("3.Update item quantity")
#         print("4.View cart")
#         print("5.Exit")
#         choise = input("Choose an option (1-5): ")
#         if choise == '1':
#             add_item(cart)
#         elif choise == '2':
#             remove_item(cart)
#         elif choise == '3':
#             update_item(cart)
#         elif choise == '4':
#             view_cart(cart)
#         elif choise == '5':
#             print("\nyour cart is done")
#             break
#         else:
#             print("invalid choice.please try again.")

# if __name__ == "__main__":
#     main()

def add_item(cart, name , price, quanitity):
    name = input("Enter the item name: ")
    price = float(input("Enter the item price :"))
    quanitity = int(input("Enter the item quantity:"))
    cart[name] = {'price': price, 'quanitity': quanitity}
    print (f"added {quanitity} of {name} for ${price} each to the cart")
    return cart
cart = {}
add_item(cart, 'apple', 0.5, 3)
print(cart)
























