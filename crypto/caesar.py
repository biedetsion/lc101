from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ""
    for i in list(text):
        encrypted += rotate_character(i, rot)
    return encrypted

def main():
    message = input("Type a message:")
    rotate = input("Rotate by:")
    print(encrypt(message,int(rotate)))

if __name__ == "__main__":
    main()


