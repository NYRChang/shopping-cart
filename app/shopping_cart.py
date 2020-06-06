# shopping_cart.py

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71




# TODO: write some Python code here to produce the desired output

#Shopper Input
scanned_items = []
subtotal = 0
valid_id = [i["id"] for i in products]

while True:
    item_id = input("Please input your product ID (1 to 20) or 'DONE' to checkout): ")
    if (item_id == "DONE" or item_id =='done'):
         break
    elif(item_id in str(valid_id)):
        scanned_items.append(item_id)
    else:
        print("   * Product ID is not valid *")
        

#Header
print("---------------------------------")
print("Glober Market")
print("8233 Broadway")
print("Elmhurst, NY 11373")
print("www.globermarket.com")
print("---------------------------------")
now = datetime.datetime.now()
print("Checkout at:" , now.strftime("%Y-%m-%d %H:%M"))
print("---------------------------------")

#Printing Individual Product List and Prices
print("Selected Products:")
for i in scanned_items:
    matching_products = [p for p in products if str(p["id"]) == str(i)]
    matching_id = matching_products[0]
    subtotal = subtotal + matching_id['price']              #adding item prices to subtotal
    price_usd = "${0:.2f}".format(matching_id['price'])
    print(f" ++ {matching_id['name']} ({str(price_usd)})")

print("---------------------------------")

#Calculating Subtotal
subtotal_usd = "${0:.2f}".format(subtotal)
print("Subtotal =", subtotal_usd)

#Calculating Tax
tax = subtotal * .08875
tax_usd = "${0:.2f}".format(tax)
print("Tax (8.875%) =", tax_usd)

#Calculating Total Purchase
total_purchase = subtotal + tax
total_usd = "${0:.2f}".format(total_purchase)
print("Total =", total_usd)

#Footer
print("---------------------------------")
print("Thank you for Shopping at Glober Market!")
print("Please come again!")
print("---------------------------------")

#(shopping-env)  --->> python shopping_cart.py
# Please input a product identifier: 1
# Please input a product identifier: 2
# Please input a product identifier: 3
# Please input a product identifier: 2
# Please input a product identifier: 1
# Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2020-02-07 03:54 PM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------
#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------