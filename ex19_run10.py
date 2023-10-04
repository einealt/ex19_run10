# Exercise 19 Study Drill 3.
# Write at least one more function of your own design, and run it 10 different ways.

def travel_plan(destination, duration):
    print(f"Destination is {destination}.")
    print(f"The journey takes {duration} days.\n")

print("1.")
travel_plan("Sweden", 10)

print("2.")
Where_to_go = "Germany"
For_how_long = 15

travel_plan(Where_to_go, For_how_long)

print("3.")
travel_plan("Chile", 6 + 20)

print("4.")
travel_plan("Latvia", For_how_long + 100)

print("5.")
travel_plan(input("Where do you go: "), input("For how many days: "))

print("6.")
destination = input("Where do you go? ")
by_bike = int(input("How many days do you travel by bike? "))
by_train = int(input("How many days do you travel by train? "))

travel_plan(destination, by_bike + by_train)

print("7.")
prompt = '> '
print("Where do you go?")
destination = input(prompt)

print("For how many days?")
duration = input(prompt)

travel_plan(destination, duration)

print("8.")
def travel_plan(destination, duration):
    print(f"Destination is {destination}.")
    print(f"The journey takes {duration} days.\n")

print("Name three cities you'll visit: ")
input1 = (input("> "))
input2 = (input("> "))
input3 = (input("> "))

print("How many days you'll stay in each: ")

print(f"{input1}: ")
input4 = (int(input("> ")))
print(f"{input2}: ")
input5 = (int(input("> ")))
print(f"{input3}: ")
input6 = (int(input("> ")))

destination = input1 + ", " + input2 + " " + "and" + " " + input3
duration = input4 + input5 + input6

travel_plan(destination, duration)

print("9.")
def travel_plan(destination, duration):
    print(f"Destination is {destination}.")
    print(f"The journey takes {duration} days.\n")

print("There's autumn in Finland.")
print("There's summer in Italy.")
print("Would you prefer autumn or summer: ")

autumn_or_summer = input("> ")

if autumn_or_summer == "autumn":
    destination = "Finland"
else: 
    destination = "Italy"

duration = 10

travel_plan(destination, duration)

print("10.")
def journey(destination, duration):
    def travel_plan():
        print(f"Destination is {destination}.")
        print(f"The journey takes {duration} days.\n")
    travel_plan()

journey("Paris", 10)
