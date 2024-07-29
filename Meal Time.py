""" def main():
5

def convert(time):
    ...


if __name__ == "__main__":
    main()

"""

"""def main(meal):
    meal= input("what's time is it?")

match cdmeal:
    case"7:00"|"7:30"|"8:00":
        print("breakfast time")
    case"12:00"|"12:30"|"13:00":
        print("lunch time")
    case"18:00"|"18:30"|"19:00":
        print("dinner time")
    case _:
        print("don't you dare to eat bitch!")

def convert(time):
    round(hour + minute/60)
    hours, minutes = time.split(":")


if __name__ == "__main__":
    main()
    """
def main():
        exp = input('What time is it? ').strip()
        t = convert(exp)
        if 7 <= t <= 8:
            print('breakfast time')
        elif 12 <= t <= 13:
            print('lunch time')
        elif 18 <= t <= 19:
            print('dinner time')
        else:
            print("Not yet, don't you dare to eat bitch!")
    
    
    
def convert(time):
    
            h, m = time.split(':')
            h = int(h)
            m = int(m)
    
            return h + m / 60
    
    
    
if __name__ == "__main__":
        main()
