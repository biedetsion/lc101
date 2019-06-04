def alphabet_position(char):
    if char.isupper():
        return ord(char) - 65
    else:
        return ord(char)-97

def char_from_position(char_number, upper):
    character = chr(char_number + 65)
    if upper:
        return character
    else:
        return character.lower()

def rotate_character(char, rot):
    if not(char.isalpha()):
        return char
    
    char_position = (alphabet_position(char) + rot) % 26  
     
    if char.isupper():
        return char_from_position(char_position, True)
    else: 
        return char_from_position(char_position, False)

