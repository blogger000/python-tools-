import random

def generate_phone_numbers():
    # Define the prefix and remaining digits
    prefix = "030"
    remaining_digits = 7

    # Generate 100 phone numbers
    for _ in range(100):
        # Generate the remaining digits
        remaining_digits_string = ""
        for _ in range(remaining_digits):
            remaining_digits_string += str(random.randint(0, 9))

        # Combine the prefix and remaining digits
        phone_number = prefix + remaining_digits_string

        # Print the phone number
        print(phone_number)

# Generate phone numbers
generate_phone_numbers()
