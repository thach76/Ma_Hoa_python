#Mã hóa thay thế

import random

BANGCHUCAI = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def KiemTraKey(key: str):
    """
    kiểm tra key có đúng định dạng chưa
    """
    listKey = list(key.upper())
    listBangChuCai = list(BANGCHUCAI)
    listKey.sort()
    listBangChuCai.sort()
    return listKey == listBangChuCai

def TaoKey():
    """
    Tạo một key ngẫu nhiên
    """
    key = list(BANGCHUCAI)
    random.shuffle(key)
    return ''.join(key)

def Cipher(message: str, mode: int, key: str):
    """
    Mã hóa thay thế

    message: chuỗi cần mã hóa hoặc giải mã
    mode:   1 mã hóa, 2: giải mã
    key: key để mã hóa
    """

    message.upper()
    output = ''
    charsA = BANGCHUCAI
    charsB = key

    if mode == 2:
        charsA, charsB = charsB, charsA
    if mode != 1 and mode != 2:
        return "Done"

    for char in message:
        if char.upper() in charsA:
            charIndex = charsA.find(char.upper())
            output += charsB[charIndex]
        else:
            output += char
    return output

def Main():
    message = input('Vui lòng nhâp vào 1 chuỗi: ')
    print('1. Tạo key ngẫu nhiên')
    print('2. Nhập key')
    chon = int(input('Vui lòng chọn: '))
    key = TaoKey()
    if chon == 1:
        print("Key ngẫu nhiên: " + key)
    elif chon == 2:
        key = input('Vui lòng nhập key: ')
        key = key.upper()
        if KiemTraKey(key):
            print("Key hợp lệ, Key của bạn: " + key)
        else:
            print("Key không hợp lệ! Vui lòng thử lại!")
            return

    print('1. Mã hóa')
    print('2. Giải mã')
    mode = int(input('Vui lòng chọn mã hóa hoặc giải mã: '))
    if mode == 1:
        print('Kết quả mã hóa là: ' + Cipher(message, mode, key))
    elif mode == 2:
        print('Kết quả giải mã là: ' + Cipher(message, mode, key))
    else:
        return



if __name__ == '__main__':
    Main()