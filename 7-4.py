question = "enter a series of pizza toppings or hit 'quit' to leave"
toppings = []
while True:
    topping = input(question)
    if topping == "quit": 
        break
    toppings.append(topping)
    print(f"your toppings are  {toppings}" )
