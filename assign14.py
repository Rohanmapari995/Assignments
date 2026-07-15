import threading

def check_password(password):
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(not c.isalnum() for c in password)

    score = 0

    if len(password) >= 8:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    if score == 5:
        print(password, "-> Strong")
    elif score >= 3:
        print(password, "-> Medium")
    else:
        print(password, "-> Weak")


password = ["rohan", "Rohan@122", "Rohan123", "123456", "ROHAN@12"]


threads = []

for pwd in password:
    t = threading.Thread(target=check_password, args=(pwd,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()