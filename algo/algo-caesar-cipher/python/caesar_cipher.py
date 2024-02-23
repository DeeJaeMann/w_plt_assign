#!/usr/bin/env python3
import re

class Message :
    UPPER_START = ord('A')
    UPPER_END = ord('Z')
    LOWER_START = ord('a')
    LOWER_END = ord('z')

    def __init__(self, message=None) :
        self._message = message

    @property
    def message(self) :
        return self._message
    
    @message.setter
    def message(self, string) :
        self._message = string

    def convert_letters(self, offset, char_list) :
        result_list = []

        for char in char_list :

            # Check uppercase letters
            if re.match(r'[A-Z]', char) :
                max_number = Message.UPPER_END
                min_number = Message.UPPER_START

            # Check lowercase letters
            elif re.match(r'[a-z]', char) :
                max_number = Message.LOWER_END
                min_number = Message.LOWER_START

            # Char is not a letter
            else :
                result_list.append(char)
                continue

            # Check if the character ASCII value is greater than our highest allowed value
            if (ord(char) + offset) > max_number and offset > 0:

                # Calculate the remainder after our highest value
                new_offset = (ord(char) + offset) - max_number
                # Add that value to our start value 
                new_char = chr(min_number + new_offset)
                result_list.append(new_char)
            
            elif (ord(char) + offset) < min_number:

                # Calculate how far before our lowest value
                new_offset = min_number - (ord(char) + offset)
                new_char = chr(max_number - new_offset)
                result_list.append(new_char)

            else :

                new_char = chr(ord(char)+offset)
                result_list.append(new_char)

        return result_list

    def cipher_message(self, offset=0) :

        new_message = re.findall(r'.', self.message)
        new_message = self.convert_letters(offset, new_message)
        return "".join(new_message)

def caesar_cipher(string, shift_amount):
    msg = Message(string)

    cipher = msg.cipher_message(shift_amount)

    return cipher

print(caesar_cipher("Boy! What a string!", -5))
print(caesar_cipher("Boy! What a string!", 5))
print(caesar_cipher("Hello zach168! Yes here.", 5))
print(caesar_cipher("Hello Zach168! Yes here.", -5))
