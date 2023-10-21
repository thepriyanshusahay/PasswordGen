import string
import random

if __name__ == "__main__":
    # taking lowercase letters
    s1 = string.ascii_lowercase
    # taking uppercase letters
    s2 = string.ascii_uppercase
    # taking numbers letters
    s3 = string.digits
    # taking characters
    s4 = string.punctuation
    # taking inputs by user
    plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    # Merging all strings in list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your password is: ")
    print("".join(random.sample(s, plen)))

