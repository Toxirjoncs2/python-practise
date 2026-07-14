import random as r
import string as s
def generate_password(length):
    characters=s.ascii_letters+s.digits
    password=""
    for _ in range(length):
        password+=r.choice(characters)
    return password
