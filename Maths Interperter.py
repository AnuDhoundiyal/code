expression = input("expression: ").strip()

x,y,z = expression.split(" ")

if y =="+":
    result=float(x) + float(z)
    print(f"{result:.1f}")
if y=="-":
    result=float(x) - float(z)
    print(f"{result:.1f}")
if y=="%":
    result=float(x) % float(z)
    print(f"{result:.1f}")
if y=="/":
    result=float(x) / float(z)
    print(f"{result:.1f}")
if y=="*":
    result=float(x) * float(z)
    print(f"{result:.1f}")
else:
    print("Enter the valid expression")