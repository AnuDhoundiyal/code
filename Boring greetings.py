"""Greeting = input("Greeting: ")

if Greeting == "HELLO":
    print("$0")
elif Greeting =="HEY":
    print("$20")
elif Greeting == "HOW":
    print("$30")
else:
    print("$100")"""\
    


x = input("Greeting: ").lower().strip()
# conditions for not greeting with hello ....
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")