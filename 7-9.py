sandwich_orders = ["grilled chicken sandwich", "pastrami","fried chicken sandwich","pastrami", "pastrami", "bad boiled chicken sandwich", "deep fried chicken sandwich", "grilled cheese sandwich(with chicken)"]
finished_sandwiches = []
print("the deli has ran out of pastrami")

list86= "pastrami"

while list86 in sandwich_orders:
    sandwich_orders.remove(list86)

for sandwich in sandwich_orders:
    print(f" I have made your {sandwich}")
    finished_sandwiches.append(sandwich)
else: 
    print(f"all done the sandwhiches we made are {finished_sandwiches} ")