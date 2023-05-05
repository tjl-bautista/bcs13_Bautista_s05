'''
PROGRAM: SHOPPING CART

Create a program that allows a user to add items to their shopping cart. The user should be able to add items and their respective prices. 
The program should also display the total cost of the items in the shopping cart.

Instructions:

	Create an empty dictionary called shopping_cart to hold the items and their respective prices.
	Use a while loop to allow the user to add items to the shopping cart.
	Inside the while loop, use the input() function to ask the user for the item name and price. The item name should be a string, and the price should be a float.
	Add the item and price to the shopping_cart dictionary.
	After the user adds an item, display a message to confirm that the item was added to the shopping cart.
	Ask the user if they want to add another item. If they do, continue the while loop. If they do not, exit the while loop.
	After the user is finished adding items, display the total cost of the items in the shopping cart.
'''

shopping_cart = {}
while True:

	add_cart_item = input("\nChoose an item to add to your cart : ")
	add_cart_price = float(input(f"What is the price of \"{add_cart_item}\"($) : "))

	shopping_cart[add_cart_item] = add_cart_price

	print("\nYour Shopping Cart:")
	for item in shopping_cart:
		print (f"{item} : ${shopping_cart[item]}")

	another_item = input("\nDo you want to add another item? (yes,no) : ").lower()
	
	if another_item == "no":
		break

sum = 0
for price in shopping_cart:
	sum += shopping_cart[price]

print(f"\nThe total price of your items is ${sum} ")