import string

# def cesar_cipher(text, key):
#     crypted_text = []
#     for char in text:
#         crypted_text += chr((ord(char) + key) % 1_114_112)
#     return crypted_text

# print(cesar_cipher("chocolat",53120000000))


def cesar_cipher(text, key):
    list_of_crypted_chars = []

    for char in text:
        list_of_crypted_chars.append(chr((ord(char) + key) % 1_114_112))




