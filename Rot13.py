"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

"""

def rot13(message):
    cipher_limit = 13
    new_message = ""
    for i in message:
        if(not i.isalpha()):
            new_message += i
        elif(i.islower()):
            binary_range  = ord(i)+cipher_limit
            if(binary_range > 122):
                binary_range = 97 + (binary_range - 122) -1
                new_message += chr(binary_range)
            else:
                new_message += chr(binary_range)
        elif(i.isupper()):
            binary_range = ord(i) + cipher_limit
            if(binary_range > 90):
                binary_range = 65 + (binary_range - 90) -1
                new_message += chr(binary_range)
            else:
                new_message += chr(binary_range)
    return new_message
print(rot13("Test @ for Test in Charg!"))
