MENU_MESSAGE = '''
-------------------------------------
|                                   |
|  We offer:                        |
|  1. Water                         |
|  2. Orange Juice                  |
|  3. Apple Juice                   |
|  4. Sprite                        |
|  5. Coke                          |
|                                   |
|  Enter the number of the drink    |
|  you would like to order:         |
|                                   |
-------------------------------------
'''

NOT_IN_MENU_MESSAGE = '''
 ________________________________
|                                |
|   Your choice is out of range. |
|                                |
|   Bye bye!                     |
|________________________________|
'''

PRICE_MESSAGE = '''
---------------------------------------
|                                     |
|  The price for your drink is:       |
|            {} ₪                     |
|                                     |
---------------------------------------
'''

ENTER_COINS_MESSAGE = '''
-----------------------------------
| Your total is {} ₪              |
|                                 |
|  Enter the coins for the        |
|          payment:               |
|                                 |
|  Shekel = 1, Shneikel = 2,      |
|  Chamishiot = 5, Assiriot = 10  |
|                                 |
-----------------------------------
'''

ENTRER_AMOUNT_MESSAGE = '''
---------------------------------
|                               |
|  Please specify the quantity  |
|    of drinks you'd like to    |
|            order:             |
|                               |
---------------------------------
'''

SUCCESS_MESSAGE = '''
    ________________________________
| You entered: {} ₪.              |
| The order's total is {} ₪.      |
| Your change is {} ₪.            |
|                                |
| You're getting:                |
| {} shekel coins.                |
| {} shnekel coins.               |
| {} chamishiot coins.            |
| {} assiriot coins.              |
|                                |
|   Thank you for your order!    |
|   Enjoy your drink.            |
|                                |
|   Have a great day!            |
|________________________________|
    
'''

SHEKEL = 1
SHNEKEIL = 2
CHAMISHIOT = 5
ASSIRIOT = 10

WATER_PRICE = 9
JUICES_PRICES = 8
SODA_PRICES = 4

# Prompt the user for input
choice = input(MENU_MESSAGE)

price = 0
# Defines the price for the drink:
if choice == "1": # water
    price = WATER_PRICE
elif choice == "2" or choice == "3":
    price = JUICES_PRICES
elif choice == "4" or choice == "5":
    price = SODA_PRICES
else:
    print(NOT_IN_MENU_MESSAGE)

if price == 0:
    exit()

print(PRICE_MESSAGE.format(price))

amount = int(input(ENTRER_AMOUNT_MESSAGE))
if amount > 1:
    price*=amount

# Ask for the coins types he wants
print(ENTER_COINS_MESSAGE)

shekel = int(input("Shekel coins: "))
shnekel = int(input("Shnekel coins: "))
chamishiot = int(input("Chamishiot coins: "))
assiriot = int(input("Assiriot coins: "))

amount_entered = (shekel * SHEKEL) + (shnekel * SHNEKEIL) + (chamishiot * CHAMISHIOT) + (assiriot * ASSIRIOT)

change = amount_entered - price

if change < 0:
    print("\n\nThe price is: ", price, "and you entered only: ", amount_entered, "You do not have enough money!")
elif change > 0:
    
    c_shekel = 0
    c_shneikel = 0
    c_chamishiot = 0
    c_assiriot = 0

    c_assiriot = int((change - (1 * SHEKEL) - (1 * SHNEKEIL) - (1 * CHAMISHIOT )) / ASSIRIOT)

    c_chamishiot += int((change - (1 * SHEKEL) - ( 1 * SHNEKEIL) - (c_assiriot * ASSIRIOT)) / CHAMISHIOT)

    c_shneikel += int(((change - (1 * SHEKEL) - (c_assiriot * ASSIRIOT) - (c_chamishiot * CHAMISHIOT) )) / SHNEKEIL )

    c_shekel += int(change - (c_assiriot * ASSIRIOT) - (c_chamishiot * CHAMISHIOT) - (c_shneikel * SHNEKEIL))

    # simple change
    # s = change%10%5%2
    # ds = (change-s)%10%5
    # fs = (change-s-ds)%10
    # gs = (change-s-ds)//10

    # print("shekel", s, "shnekel", ds, "chamishiot", fs, "assiriot", gs)
    
print(SUCCESS_MESSAGE.format(amount_entered, price, change, c_shekel, c_shneikel, c_chamishiot, c_assiriot))