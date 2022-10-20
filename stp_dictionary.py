# Assume d may have any of the data of two structures
d = {"name": "RAVI", "email": "ravi@gmail.com"}
d1 = {"firstname": "BILL"}
match d:
    case {"name": user}:
        pass
    case {"firstname": user}:
        pass
    case _:
        user = "Unknown"
print(user)
