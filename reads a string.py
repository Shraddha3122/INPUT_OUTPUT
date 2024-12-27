# Write a program that reads a string from input and validates that it only contains certain characters.

def is_valid_string(input_string):
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    for char in input_string:
        if char not in allowed_characters:
            return False
    return True

def main():
    user_input = input("Enter a string: ")
    if is_valid_string(user_input):
        print("The string is valid.")
    else:
        print("The string contains invalid characters.")

if __name__ == "__main__":
    main()