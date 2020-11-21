import calculate

print("Welcome to the mental arithmetic practice application!")
looping = True
option  = 0
while looping:
    print("What kind of operation do you want to practice?")
    operation = input()
    print("How many exercises do you want to do?")
    amount_exercises = int(input())
    print("How many digits has to have the first term?")
    first_term = int(input())
    print("How many digits has to have the second term?")
    second_term = int(input())
    
    calculate.arithmetic_operation(operation, amount_exercises, first_term, second_term)

    print("Do you want to do more exercises? If yes ->1, else 0")
    option = int(input())
    if option == 0:
        looping = False
        print("Bye!")
