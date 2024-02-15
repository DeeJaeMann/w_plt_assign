#!/usr/bin/env python3.12

class Message :
    ASCII_START = ord('A')
    ASCII_END = ord('z')

    def __init__(self, message=None) :
        self._message = message

    @property
    def message(self) :
        return self._message
    
    @message.setter
    def message(self, string) :
        self._message = string

    def cipher_message(self, offset=0) :

        def convert_letters(offset, char_list) :
            result_list = []

            for char in char_list :
                if (ord(char) + offset) > Message.ASCII_END :
                    offset = Message.ASCII_END - (ord(char) + offset)
                    new_char = chr(Message.ASCII_START + offset - 1)
                    result_list.append(new_char)

                else :
                    new_char = chr(ord(char)+offset)
                    result_list.append(new_char)

            return result_list

        message = self._message

        new_message = list(message)
        new_message = convert_letters(offset, new_message)
        return "".join(new_message)

# msg = Message("Hello")

# cipher = msg.cipher_message(offset=5)

# print(cipher)

def caesar_cipher(string, shift_amount):
    msg = Message(string)

    cipher = msg.cipher_message(shift_amount)

    return cipher

# print(caesar_cipher("Boy! What a string!", -5))
# print(caesar_cipher("Hello zach168! Yes here.", 5))
# print(caesar_cipher("Hello Zach168! Yes here.", -5))

for i in range(ord('A'), ord('z')) :
    print(f"Code {i} ")