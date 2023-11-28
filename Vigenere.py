LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#mật mã vigenere 
#mã hóa: (y1, y2, .. , yn) = (x1, x2, .. xn) + (k1, k2, .., kn)
def vigenere_cipher(message:str, key: str, mode='MAHOA'):
    message = message.upper()
    key = key.upper()
    translated = ''
    keyIndex = 0

    for char in message:
        if char in LETTERS:
            charIndexLetter = LETTERS.find(char)
            keyIndexLetter = LETTERS.find(key[keyIndex % len(key)])
            if mode == 'MAHOA':
                translated += LETTERS[(charIndexLetter + keyIndexLetter) % len(LETTERS)]
            elif mode == 'GIAIMA':
                translated += LETTERS[(charIndexLetter - keyIndexLetter) % len(LETTERS)]
            keyIndex+=1
        else:
            translated += char
    return translated

#kiem tra key
def check_key(key: str):
    for char in key:
        if char in LETTERS:
            continue
        else:
            return False
    return True

#Main
def Main():
    print("1. Mã hóa\n2. Giải mã\ncòn lại. Thoát\n")
    chon = int(input('Vui lòng chọn: '))
    if chon == 1:
        inp = input('vui long nhập chuỗi cần mã hóa: ')
        key = input('vui lòng nhập key: ')
        if not check_key(key):
            print('key không hợp lệ')
            return
        print('Kết quả mã hóa: ', vigenere_cipher(inp, key))
    elif chon == 2:
        inp = input('vui long nhập chuỗi cần giải mã: ')
        key = input('vui lòng nhập key: ')
        if not check_key(key):
            print('key không hợp lệ')
            return
        print('Kết quả giải mã: ', vigenere_cipher(inp, key, 'GIAIMA'))
    else:
        return

if __name__ == '__main__':
    Main()
    print('DONE')