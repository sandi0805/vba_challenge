pie_purchases = [0,0,0,0,0,0,0,0,0,0]

print("Welcome to the House of Pies!  Here are our pies:")
pies = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
print(pies)
pie_cart = []
x = input("Which pie would you like to try? Choose 0-9. ")
print(f"Great! We will have your {x} right out for you!")
pies.count(x)
print(f"Thank you for purchasing {x} pies today!")

pie_purchases[int(x)-1] = pie_purchases[int(x)-1] +1

shopping=input("Would you like to make another purchase? Y or N ")

Print = ("You purchased: ")

for pie_index in range(len(pies)):
    
    print(str(pie_purchases[pie_index])+" " + str(pies[pie_index]))