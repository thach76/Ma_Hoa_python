import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXY'

#nhập key (key ngẫu nhiên từ 1 đến n, key từ 1 đến n)
def NhapKey(n=7, chon = 3):
    
    key = []
    if chon == 1:
        for i in range(1, n+1):
            key.append(i)
        random.shuffle(key)
    elif chon == 2:
        index = 1
        while len(key) < n:
            number = int(input(f'Nhập Key[{index}]: '))
            if number in range(1, n+1) and not number in key:
                key.append(number)
                index+=1
            else:
                print('Vui lòng nhập key hợp lệ')
    else:
        for i in range(1, n+1):
            key.append(i)
    return key

#mã hóa 
def HoanViCipher(message:str, key, mode='MAHOA'):
    message = message.upper()
    while len(message) % len(key) != 0:
        message += 'X'


    translated = ''
    array = [[] for _ in range(len(key))]
    indexArray = 0
    for char in message:
        if char in LETTERS:
            # charIndexLetters = LETTERS.find(char)
            if mode == 'MAHOA':
                array[indexArray].append(char)
                indexArray = (indexArray + 1) % len(key)
            elif mode == 'GIAIMA':
                lenMessageSub = int(len(message) / len(key))
                if key != range(1, len(key) + 1): #nếu key không là liên tiếp
                    messageSub = ["" for _ in range(len(key))]
                    for i in range(len(key)):
                        messageSub[key[i] - 1] = message[i * lenMessageSub : (i+1) * lenMessageSub]
                    message += ''.join([sub] for sub in messageSub)
                if len(array[indexArray]) < lenMessageSub:
                    array[indexArray].append(char)

            else:
                return
        # else:
        #     translated += char
    if mode == 'MAHOA':
        for i in range(len(key)):
            translated += ''.join(array[key[i] - 1])
    return translated

#main
def Main():
    print('1. Ngẫu nhiên key từ 1 đến n (nhập n)')
    print('2. Nhập key có n phần tử (nhập n và key)')
    print('còn lại. Lấy key từ 1 đến n (nhập n)')
    # chon = int(input('Vui lòng chọn: '))
    # n = int(input('Nhập n: '))
    key = NhapKey(chon=2)
    print(key)
    message = 'TOIYEUCOAY'
    message2 = 'TUXIOXEYOCXYAX'
    translated = HoanViCipher(message, key)
    translated2 = HoanViCipher(message2, key)
    print(translated)
    print(translated2)

if __name__ == '__main__':
    Main()