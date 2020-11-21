# Importing libraries
import random
import time
from datetime import datetime
from datetime import date
import recording
import math


# Creating random numbers
def random_number(condition):
    amount_digits = str(condition)
    amount_digits = len(amount_digits)
    if amount_digits == 1:
        number = random.randint(1, 9)
    elif amount_digits == 2:
        number = random.randint(10, 99)
    elif amount_digits == 3:
        number = random.randint(100, 999)
    elif amount_digits == 4:
        number = random.randint(1000, 9999)
    return number


# Giving a name to the exercise according to the digits
def exercise_naming(operation, first_number, second_number):
    first_length = str(first_number)
    first_length = len(first_length)
    first_number_output = ""
    second_length = str(second_number)
    second_length = len(second_length)
    second_number_output = ""

    for _ in range(first_length):
        first_number_output += "0"

    for _ in range(second_length):
        second_number_output += "0"

    returning_string = first_number_output + " " + operation + " " + second_number_output

    return returning_string


# Divisions
def doing_division(first_number, second_number):
    result = first_number / second_number
    module = first_number % second_number
    integer_part = math.trunc(result)
    final_result = str(integer_part) + " " + str(module) + "/" + str(second_number)
    return final_result


# Adding single digit function
def arithmetic_operation(operation_tipe, amount_exercises, first_addend, second_addend):
    loop_counter = 1
    wrong_answer = 0
    right_answer = 0
    start_time = time.time()
    while loop_counter <= amount_exercises:
        first_number = random_number(first_addend)
        second_number = random_number(second_addend)
        if loop_counter % 10 == 0:
            print("Exercise number: ", loop_counter)
        print("Calculate:", first_number, operation_tipe, second_number)
        user_answer = (input())
        if operation_tipe == "+":
            calculated_answer = str(first_number + second_number)
        elif operation_tipe == "-":
            calculated_answer = str(first_number +- second_number)
        elif operation_tipe == "*":
            calculated_answer = str(first_number * second_number)
        elif operation_tipe == "/":
            calculated_answer = doing_division(first_number, second_number)

        if user_answer == calculated_answer:
            right_answer += 1
        else:
            print("Your answer was wrong, the answer is:",
                  calculated_answer, " go on!")
            wrong_answer += 1
        loop_counter += 1
    print("Right answers: ", right_answer)
    print("Wrong answers: ", wrong_answer)
    time_elapsed = (time.time() - start_time)
    seconds = round(time_elapsed)
    if seconds > 60:
        calculated_minutes = round(seconds / 60)
        calculated_seconds = seconds % 60
        calculated_minutes = str(calculated_minutes)
        if len(calculated_minutes) == 1:
            calculated_minutes = "0" + calculated_minutes
        timestamp = "00:" + str(calculated_minutes) + ":" + str(calculated_seconds)
        print("Your time is ", calculated_minutes, ":",
              calculated_seconds, " minutes ", sep="")
    else:
        print("Your time is", seconds, "seconds")
        timestamp = str(seconds)
        timestamp = "00:" + timestamp
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")
    rate = str(right_answer) + "/" + str(wrong_answer)
    exercise_name = exercise_naming(operation_tipe, first_addend, second_addend)
    recording.write_record(today, timestamp, exercise_name, rate, operation_tipe)
