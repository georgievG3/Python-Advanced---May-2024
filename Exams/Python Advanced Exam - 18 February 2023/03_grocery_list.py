def shop_from_grocery_list(budget, grocery_list, *args):
    grocery_list_check = grocery_list
    purchased_product = []

    for product, price in args:

        if product not in purchased_product and product in grocery_list:

            if budget >= price:
                grocery_list_check.remove(product)
                purchased_product.append(product)
                budget -= price

            else:
                break

    if not grocery_list_check:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list_check)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
