def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]


def xor_crypt(text, key):
    expanded_key = repeat_to_length(key, len(text))
    index = 0
    encrypted_string = ""
    for char in text:
        original_char_ascii = ord(char)
        key_char_ascii = ord(expanded_key[index:index+1])
        shifted_char = chr(original_char_ascii ^ key_char_ascii)
        encrypted_string += shifted_char
        index = index + 1

    return encrypted_string


def xor_encrypt(text, key):
    return xor_crypt(text, key)


def xor_decrypt(secret_text, key):
    return xor_crypt(secret_text, key)


print(xor_encrypt("01234", "asde"))  # QBVVU
print(xor_decrypt("QBVVU", "asde"))  # 01234