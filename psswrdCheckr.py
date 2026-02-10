import random

pswdCheck = input("Enter password: ")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+"

has_letter = any(c in letters for c in pswdCheck)
has_number = any(c in numbers for c in pswdCheck)
has_symbol = any(c in symbols for c in pswdCheck)

if has_letter and has_number and has_symbol and len(pswdCheck) >= 6:
    print("Strong password ✅")
else:
    print("Weak password ❌")
