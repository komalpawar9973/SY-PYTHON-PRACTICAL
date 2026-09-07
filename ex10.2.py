def inventory_search(products, item_name):
    if item_name in products:
        index = products.index(item_name)
        print(f"{item_name} is present in the inventory.")
        print(f"Index location: {index}")
    else:
        print(f"{item_name} is not present in the inventory.")

products = ["macbook", "laptop", "tablet", "keyboard", "mouse"]

item_name = input("Enter the product name to search: ")

inventory_search(products, item_name)