# 🔐 Concurrent Password Strength Checker

A simple Python program that checks the strength of multiple passwords concurrently using the `threading` module. Each password is evaluated based on length, uppercase letters, lowercase letters, digits, and special characters.

## Features
- Concurrent password checking using threads
- Classifies passwords as:
  - Strong
  - Medium
  - Weak
- Uses Python string methods (`isupper()`, `islower()`, `isdigit()`, `isalnum()`)

## Password Criteria
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

## Sample Output

```text
admin -> Weak
Admin123 -> Medium
Admin@123 -> Strong
123456 -> Weak
Hello@12 -> Strong
```
