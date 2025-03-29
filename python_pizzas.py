print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").capitalize()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
while size == "":

    # bill = 0
    print("Please select the you wnat for the pizza.")
    size = input("What size pizza do you want? S, M or L: ").capitalize()


print("Let's continue with your order.")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()


if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1


elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1


elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1


drink_option = input("Would you like to have a drink?: 'Y' for yes, 'N' for no: ").upper()


if drink_option == "Y":

    drink_choice = input("Which drink would you like to have? Pepsi, Coca Cola, Fanta or Stoney: ").capitalize()
    while drink_choice == "":
        print("Please choose which drink you want.")
        drink_choice = input("Which drink would you like to have? Pepsi, Coca Cola, Fanta or Stoney: ").capitalize()

        if drink_choice == "Pepsi":
            print("Please pay $3")
            bill += 3
        elif drink_choice == "Fanta" or drink_choice == "Stoney":
            print("Please pay $5")
            bill += 5
        elif drink_choice == "Coca Cola":
            print("Please pay $7")


print(f"Your final bill is: ${bill}.")