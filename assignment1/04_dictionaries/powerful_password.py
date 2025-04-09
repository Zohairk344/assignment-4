from hashlib import sha256

def login(email, Saved_logins, GivenPassword):

    if Saved_logins[email] == hash_password(GivenPassword):
        return True
    
    return False

def hash_password(password):

    return sha256(password.encode()).hexdigest()

def main():
    Saved_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", Saved_logins, "word"))
    print(login("example@gmail.com", Saved_logins, "password"))
    
    print(login("code_in_placer@cip.org", Saved_logins, "Karel"))
    print(login("code_in_placer@cip.org", Saved_logins, "karel"))
    
    print(login("student@stanford.edu", Saved_logins, "password"))
    print(login("student@stanford.edu", Saved_logins, "123!456?789"))


if __name__ == '__main__':
    main()