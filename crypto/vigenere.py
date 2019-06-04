from helpers import alphabet_position, rotate_character

def encrypt(message, keyword):
    scrambled_text = ''
    letter = 0
    for i in range(len(message)):
        if message[i].isalpha():
            scrambled_text += rotate_character(message[i], alphabet_position(keyword[letter % len(keyword)]))
            letter += 1
        else:
            scrambled_text += message[i]
    return scrambled_text

def main():
    a_message = input("Type a message: ")
    a_keyword = input("Type a keyword: ")
    print(encrypt(a_message, a_keyword))

if __name__ == '__main__':
    main()