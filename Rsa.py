# Chọn p và q là 2 số nguyên tố: p = 11, q = 13
# n = p * q = 11 * 13 = 143
# Ɵ(n) = (p-1) * (q-1) = 10 * 12 = 120
# Chọn ngẫu nhiên số e = 37 (37 với 120 có UCLN = 1)
# Nhẩm ra số d = 13 vì 13 * 37 = 481 mod 120 = 1. Nếu không nhẩm được thì ta dùng thuật toán Eulid mở rộng
# ---> Khóa công khai (37, 143)
# ---> Khóa riêng (13, 11, 13)
import math

LETTERS = ''

#kiểm tra số nguyên tố
def isSoNguyenTo(n):
    '''kiểm tra số nguyên tố'''
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

#số nguyên tố sẽ được lấy trong khoang các số lớn hơn n
def getSoNguyenToNgauNhien(n=911):
    '''số nguyên tố sẽ được lấy trong khoảng các số lớn hơn n'''
    if n % 2 == 0:
        n+=1
    
    while True:
        if isSoNguyenTo(n):
            return n
        n+=2
            
#tìm ucln của 2 số a,b
def ucln(a, b):
    '''tìm ucln của 2 số a,b'''
    while b:
        a,b = b, a%b
    return a

#tính tính i với n * i mod m = 1
def eulid(n, m):
    '''tính tính i với n * i mod m = 1'''
    if ucln(n,m) != 1:
        return None
    i = 1
    while n * i % m != 1:
        i+=1
    return i

#lấy ngẫu nhiên số nguyên tố  p q
#đầu vào là 1 số gần p và 1 số gần q
def getPQ(p=11, q=13):
    '''lấy ngẫu nhiên số nguyên tố  p q

    đầu vào là 1 số gần p và 1 số gần q'''
    P = getSoNguyenToNgauNhien(p)
    Q = getSoNguyenToNgauNhien(q)
    return [P, Q]

#số ngẫu nhiên e với ucln(e, n) = 1
def getE(On, e=13):
    '''số ngẫu nhiên e với ucln(e, n) = 1'''
    while ucln(e, On) != 1:
        e+=1
    return e

#return d sao cho e * d mod n = 1
def getD(e, On):
    '''return d sao cho e * d mod n = 1'''
    return eulid(e, On)

#Khóa công khai (e, n)
def getKey():
    '''Khóa công khai (e, n)\n
    Khóa riêng (d, p, q)'''
    #lấy ngẫu nhiên 2 số nguyên tố p,q
    p, q = getPQ()
    n = q * p
    #On (p-1)*(q-1) = On
    On = (p-1) * (q-1)
    #chọn ngãu nhiên số e
    e = getE(On)
    #lấy d với d * e mod On = 1
    d = getD(e, On)
    publicKey = [e, n]
    privateKey = [d, p, q]
    return [publicKey, privateKey]

# Mã hóa:
# (2 ^ 37) mod 143 = 106
# Giải mã:
# (106 ^ 13) mod 143 = 2
def rsaCiper(message, key, mode='MAHOA'):
    translated = []
    for c in message:
        if mode == 'MAHOA':
            translated.append(pow(c, key[0][0], key[0][1]))
        elif mode == 'GIAIMA':
            translated.append(pow(c, key[1][0], key[1][1] * key[1][2]))
    return translated
def main():
    key = getKey()
    #nếu các phần từ được mã hóa là phải nhỏ hơn p * q 
    # để đảm bảo tính chính xác của thuật toán vì thế chọn p và q càng lớn thì các 
    #phần tử được mã hóa sẽ càng lớn
    message = '2 6 9 11 5 34 75 112'
    #message = input('Vui lòng nhập chuỗi đầu vào: ')
    input = [int(x) for x in message.split() if x.isdigit()]
    print('chuỗi ban đầu là: ', ' '.join(map(str, input)))
    mahoa = rsaCiper(input, key)
    giaima = rsaCiper(mahoa, key, 'GIAIMA')
    print('Key ' , key)
    print('Kết quả mã hóa là: ', ' '.join(map(str, mahoa)))
    print('kết quả giải mã là: ', ' '.join(map(str, giaima)))

if __name__ == '__main__':
    main()



