import random 
destinations={
    "beaches":["goa","maldives","andaman and nicobar"],
    "mountains":["himalayas","alps","rocky mountains"],
    "cities":["paris","tokyo","venice"]
              }
jokes=[
    "why dont programmers like nature? too many bugs!",
    "why did the computer go to the doctor? it had a virus!",
    "If your computer isn't working properly and you don't understand why... ...just hit it a bunch of times with a hammer. It still won't work properly, but at least you'll understand why."]
def recommend():
    choice= input("beaches,mountains or cities?").lower()
    if choice in destinations:
        place=random.choice(destinations[choice])
        like=input(f"try{place}! do you like it?(yes/no):").lower()

        if like=="yes":
            print(f"enjoy your trip to {place}!")
        else:
            recommend()
    else:
        print("invalid choice!")
        recommend()
def packing():
    place= input("where are you going?")
    days= input("how many days?")
    print(f"pack clothes,charger and weather essentials for {days} days in {place}.")

def chat():
    name = input("Your name: ")
    print(f"Hello {name}! Type: recommend, packing, joke, help, exit")

    while True:
        msg = input("You: ").lower()

        if "recommend" in msg:
            recommend()
        elif "packing" in msg:
            packing()
        elif "joke" in msg:
            print(random.choice(jokes))
        elif "help" in msg:
            print("recommend | packing | joke | exit")
        elif "exit" in msg or "bye" in msg:
            print("Safe travels! Goodbye!")
            break
        else:
            print("I didn't understand.")

chat()