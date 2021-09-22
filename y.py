grocery_list = []

def groceries():
    valid = False
    while not valid:
        food = input("Please enter what you need to get from the grocery store: ")

        if food == "done":
            valid = True

        else:
            grocery_list.append(food)
            print(grocery_list)
            

    
    
def prices():
    valid = False
    while not valid:
        price = input("Please enter the cost of your items: ")

        if price == "done":
            valid = True

        else:
            grocery_list.append(price)
            print(grocery_list)



def main():
    groceries()
    prices()
Information = ("This program will have a list groceries followed by their prices.\nAfter giving each item, the item will then be put in a list until the user states he or she is done.\nThe user will then provide the price of each item going in order from left to right")
print(Information)


main()
















    
    
