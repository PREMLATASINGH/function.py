def valide_email(email):
    if "@" in email and "." in email:
        return "Valid email address"
    else:
        return "Invalid email address"
print(valide_email("example@example.com"))
print(valide_email("invalidemail.com"))
print(valide_email("another@example"))
print(valide_email("    @example.com"))
print(valide_email("example@.com"))