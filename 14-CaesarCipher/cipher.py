# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute-force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')


def getMessage():
    print('Enter your message:')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % MAX_KEY_SIZE)
        key = int(input())
        if (1 <= key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # Symbol not found in SYMBOLS.
            # Just add this symbol without any change.
            translated += symbol
        else:
            # Encrypt or decrypt.
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


if __name__ == '__main__':
    mode = getMode()
    message = getMessage()
    if mode[0] != 'b':
        key = getKey()
        print('Your translated text is:')
        print(getTranslatedMessage(mode, message, key))
    else:
        print('Your translated text is:')
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, getTranslatedMessage('decrypt', message, key))
