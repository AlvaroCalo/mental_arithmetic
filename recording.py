

# Write the date, time, exercise tipe and the rate correct/incorrect

def write_record(date_input, time_input, exercise_input, rate_input, operation):
    if operation == "+":
        f = open("adding.csv", "a")
        line_to_write = date_input + ";" + time_input + ";" + exercise_input + ";" + rate_input + "\n"
        f.write(line_to_write)
        f.close()
    elif operation == "-":
        f = open("substrac.csv", "a")
        line_to_write = date_input + ";" + time_input + ";" + exercise_input + ";" + rate_input + "\n"
        f.write(line_to_write)
        f.close()
    elif operation == "*":
        f = open("multiplication.csv", "a")
        line_to_write = date_input + ";" + time_input + ";" + exercise_input + ";" + rate_input + "\n"
        f.write(line_to_write)
        f.close()
    elif operation == "/":
        f = open("division.csv", "a")
        line_to_write = date_input + ";" + time_input + ";" + exercise_input + ";" + rate_input + "\n"
        f.write(line_to_write)
        f.close()
