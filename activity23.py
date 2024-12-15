def factorial(number):
    fact = 1
    for x in range (number, 0, -1):
        fact *=x

    return fact

help("factorial")
help("print")