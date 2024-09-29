def get_shoppinglist():
    get_shoppinglist = [] #it is ist that stores calues
    total_price = 0
    while True:
        item = input("Enter the name of the item(or type 'done to finish):")
        if item.lower() == 'done':
            break
        try:
            item_price = float(input(f"Enter the price of '{item}': "))
            get_shoppinglist.append((item,item_price))
            totaol_price += item_price

        except ValueError:
            print("Invalid input. pleace enter a numeric value for the price")
        
    return get_shoppinglist,total_price

def main():
    print("Welcome to the shopping list program")
    shoppingl_ist, total_price = get_shoppinglist()

    if not get_shoppinglist:
        print("No items were entered")
    else:
        print("\nshoppinhg list:")
        for item, price in get_shoppinglist:
            print(f"{item},${price:.2f}")
            print(f"\nTotal price: ${total_price:.2f}")

main()


