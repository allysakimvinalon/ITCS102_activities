def calculator():
    x =int(input("Enter first number: "))
    y =int(input("Enter second number: "))
    yy = x + y
    z = print(f"The sum of {x} and {y} is {yy}.")
    print()

def hello_world():
    print("Hello World!")
    print("print('Hello World!')")
    print()
    print("Output: Hello World!")
    print()

def temp():
    print("<<<<<<temperature conversion>>>>>") 
    x =int(input("would you like to convert degrees to fahrenheit(yes\no)"))
    if x == "yes":
        a = int(input("enter a temperature in degrees: "))
        if a >= 0:
            b = (a -32)*5/9
            print(f"the conversion of {a} is {b}")
def main():
    while True:
        print("enter a command based on categories")
        print("commands (1-10)")
        x = input("enter a command: ")
        if x == "exit":
            print("program terminated")
            break
        elif x != "exit":
            if x == 1:
                calculator()
            elif x == 2:
                hello_world()
            elif x == 3:
                temp()
                print()
            elif x == 4:
                pass
            elif x == 5:
                pass
            elif x == 6:
                pass
            elif x == 7:
                pass
            elif x == 8:
                pass
main()            