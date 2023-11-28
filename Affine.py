LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#tìm ucln
def ucln(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#tìm module của a (a*i ≡ 1 mod m hay tìm i sao cho a * i chia cho m dư 1)
def module(a, m=26):
    if ucln(a, m) != 1:
        return None
    i = 1
    while True:
        if a * i % m == 1:
            return i
        if i > 1000:
            return None
        i+=1

#cho khóa là (a,b) với ucln(a, m) =1 và 0 <= b <= m
#mã hóa: y = (a * x + b) mod m
#giải mã: x = a^-1 *(y - b) mod m
#ở đây m = 26 
#mật mã affine 
def affine(message:str, mode='MAHOA', key = (5, 7)):
    message = message.upper()
    translated = '' 
    for char in message:
        #nếu là chữ cái
        if char in LETTERS:
            charIndex = LETTERS.find(char)
            if mode == 'MAHOA':
                translated += LETTERS[(key[0] * charIndex + key[1]) % len(LETTERS)]
            elif mode == 'GIAIMA':
                translated += LETTERS[(module(key[0]) * (charIndex - key[1])) % len(LETTERS)]
        else:
            translated += char
    return translated

def NhapKey():
    a = int(input('vui lòng nhập key (a, b)\n a = '))
    b = int(input(' b = '))
    if module(a) == None or b > len(LETTERS):
        print('key không hợp lệ\nDone\n')
        return None
    key = (a, b)
    return key

def MaHoa_GiaiMa(mode:str):
    chedo = ''
    if mode == 'MAHOA':
        chedo = 'mã hóa'
    elif mode == 'GIAIMA':
        chedo = 'giải mã'
    inp = input(f'vui lòng nhập chuỗi để {chedo}: ')
    key = NhapKey()
    if key == None:
        return
    print(f'Kết quả {chedo} là: ', affine(inp, mode, key))

#main
def Main():
    print('1. Mã hóa\n2. Giải mã\ncòn lại. Thoát\n')
    chon = int(input('vui lòng chọn: '))
    if chon == 1:
        MaHoa_GiaiMa('MAHOA')
    elif chon == 2:
        MaHoa_GiaiMa('GIAIMA')

if __name__ == '__main__':
    Main()
