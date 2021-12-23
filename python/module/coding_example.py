from days_utility import days_to_hours, validate_input, input_string
import validation_exception

user_input = ""
while user_input != 'Q':
    user_input = input(input_string)
    try:
        for input_number_of_days in set(user_input.split(",")):
            calculated_value = days_to_hours(validate_input())
            print(calculated_value)
    except validation_exception as ex:
        print(ex)
