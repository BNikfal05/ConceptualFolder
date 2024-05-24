'''Welcome to a simple Caesar cipher made utilizing the index of numbers that python possesses instead of lists containing letters'''


def encode(x=list(input("What do you want to encode: ")), shift=int(input("By how much do you want to shift: "))):
    encoded = ''
    for i in range(len(x)):
        encoded += chr(((ord(x[i]) - ord('a') - shift) % 26) + ord('a'))

    return encoded


result = encode()
print(result)


def decode(x=list(input("What do you want to decode: ")), shift=int(input("By how much was the message shifted: "))):
    decoded = ''
    for i in range(len(x)):
        decoded += chr(((ord(x[i]) - ord('a') + shift) % 26) + ord('a'))

    return decoded


result = decode()
print(result)
