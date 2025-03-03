menu = ["1) Taco", "2) Burrito", "3) Nachos", "4) Soft Drink", "5) Quit"]
prices = [1.00, 2.00, 3.00, 4.00]
print("Menu:")
for x in menu:
    print(x)

order = []
total_price = 0.0

while True:
    try:
        x = int(input("\nSelect an option (1-5): ")) - 1
        if x == 4:
            break
        elif 0 <= x < 4:
            print(f"You selected: {menu[x]}")
            order.append(menu[x])
            total_price += prices[x]
            print(f"Price: ${prices[x]:.2f}")
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")


print(f"Total Price: ${total_price:.2f}")



