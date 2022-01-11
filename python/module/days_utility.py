from validation_exception import ValidationException

num_hours_in_day = 24
name_of_unit = 'hours'


def days_to_hours(num_of_days):
    return f'{num_of_days} days are {num_of_days * num_hours_in_day} {name_of_unit}'


def validate_input(number_of_days):
    # user_input is global so we don't need to pass a parameter
    if number_of_days.isdigit():
        user_input_number = int(number_of_days)
        if user_input_number == 0:
            raise ValidationException(f'You entered a 0, please enter a valid positive value.')
        return user_input_number
    else:
        raise ValidationException(f'{number_of_days} is not a valid value for this program.')


input_string = 'Please enter a number of days and I will convert it to hours!\n'
