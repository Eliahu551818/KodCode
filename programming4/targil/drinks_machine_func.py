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

def define_price(choice):
    if choice == "1": # water
        return WATER_PRICE
    elif choice == "2" or choice == "3":
        return JUICES_PRICES
    elif choice == "4" or choice == "5":
        return SODA_PRICES
    else:
        print(NOT_IN_MENU_MESSAGE)
        return False
    
# Prompt the user for input
choice = input(MENU_MESSAGE)

price = define_price(choice=choice)

if not price:
    exit()

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
else:
    
    c_shekel = 0
    c_shneikel = 0
    c_chamishiot = 0
    c_assiriot = 0

    # For each type of coin count the amount by reducing from the whoel (change) the value for each of the coins smaller than it
    c_assiriot = int((change - (1 * SHEKEL) - (1 * SHNEKEIL) - (1 * CHAMISHIOT )) / ASSIRIOT)

    c_chamishiot += int((change - (1 * SHEKEL) - ( 1 * SHNEKEIL) - (c_assiriot * ASSIRIOT)) / CHAMISHIOT)

    c_shneikel += int(((change - (1 * SHEKEL) - (c_assiriot * ASSIRIOT) - (c_chamishiot * CHAMISHIOT) )) / SHNEKEIL )

    c_shekel += int(change - (c_assiriot * ASSIRIOT) - (c_chamishiot * CHAMISHIOT) - (c_shneikel * SHNEKEIL))

    # simple change
    # c_shekel = change %10 %5 %2
    # c_shneikel = (change -c_shekel) %10 %5
    # c_chamishiot = (change -c_shekel -c_shneikel ) %10
    # c_assiriot = (change -c_shekel -c_shneikel ) //10

    # print("shekel", c_shekel, "shnekel", c_shneikel, "chamishiot", c_chamishiot, "assiriot", c_assiriot)
 
