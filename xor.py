def XOR (input1, input2):   #function to produce the XOR combination
    result = b'' #initialization of the xor value

    for byte1, byte2 in zip(input1, input2):
        result += bytes([byte1 ^ byte2])
    return result

def main():
    string1 = bytes.fromhex('1c0111001f010100061a024b53535009181c');
    string2 = bytes.fromhex('686974207468652062756c6c277320657965');
    print(XOR(string1, string2).hex())

if __name__ == '__main__':
    main()
