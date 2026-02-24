def is_string_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_s = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
print(is_string_palindrome("A man a plan a canal Panama"))
print(is_string_palindrome("Hello World"))
print(is_string_palindrome("Madam In Eden Im Adam"))
print(is_string_palindrome("Not a palindrome"))