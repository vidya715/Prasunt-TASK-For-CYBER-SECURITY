import string

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    # Calculate score based on criteria
    score = length_criteria + digit_criteria + lowercase_criteria + uppercase_criteria + special_criteria

    # Determine strength
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

def main():
    # Get password input from user
    password = input("Enter your password: ")

    # Check password strength
    strength = check_password_strength(password)
    
    # Print the strength of the password
    print(f"The strength of '{password}' is: {strength}")

# Run the main function
if __name__ == "__main__":
    main()
