# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

s_pizza = 15
m_pizza = 20
l_pizza = 25
add_pepperoni_s = 2
add_pepperoni_ml = 3
extra_cheese_x = 1
bill = 0

if size == "S":
    bill = s_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_s
    if extra_cheese == "Y":
        bill += extra_cheese_x
    print(f"Your final bill is: ${bill}")
elif size == "M":
    bill = m_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_ml
    if extra_cheese == "Y":
        bill +=extra_cheese_x
    print(f"Your final bill is: ${bill}")
else:
    bill = l_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_ml
    if extra_cheese == "Y":
        bill += extra_cheese_x
    print(f"Your final bill is: ${bill}")