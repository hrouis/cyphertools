def main():
    myMessage = 'Common sense is not so common.'
    myKey = 18
    ciphertext = encrypt_message(myKey, myMessage)
    print(ciphertext + '|')


def encrypt_message(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()