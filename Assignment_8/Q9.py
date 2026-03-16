def check_palindrome(num):
    """
    Function to check if a number is a palindrome.
    It reverses the number and returns True if it matches the original.
    """
    original_num = num
    reversed_num = 0
    
    # Logic to reverse the number mathematically
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
        
    return original_num == reversed_num

# --- Main Program Execution ---
# Taking input from the user [cite: 22]
user_input = int(input("Enter a number to check if it is a palindrome: "))

# Calling the function and printing the result
if check_palindrome(user_input):
    print(f"Yes, {user_input} is a palindrome.")
else:
    print(f"No, {user_input} is not a palindrome.")