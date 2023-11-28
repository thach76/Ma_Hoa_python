import math
import random
import time

#tìm ước chung lớn nhất của a và b
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

#số nguyên dương a gọi là căn nguyên thủy của n 
#khi và chỉ khi a và n nguyên tố cùng nhau (ucln(a,n) = 1), a < n
def isCanNguyenThuy(a, n):
    return ucln(a, n) == 1 and a < n

#kiểm tra số nguyên tố
def isSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def getRamdomBigInt():
    return random.randint(10000000000, 10000000000000)

#lấy ngẫu nhiên 1 số nguyên tố cực lớn
def getRandomBigSoNguyenTo():
    while True:
        n = getRamdomBigInt()
        if isSoNguyenTo(n):
            return n

def main():
    p, g = getRandomBigSoNguyenTo(), 5
    while not isSoNguyenTo(p):
        p = int(input('Vui lòng nhập số nguyên tố p: '))
    
    while not isCanNguyenThuy(g, p):
        g = int(input('Vui lòng nhập g (g là căn nguyên thủy mod p): '))
    
    print(f'Số dùng chung p, g là {p} và {g}')
    a, b = getRamdomBigInt(), getRamdomBigInt()
    # a = int(input('Nhập số nguyên bí mật của Alice: '))
    # b = int(input('Nhập số nguyên bí mật của Bob: '))

    A = pow(g, a, p)
    B = pow(g, b, p)
    #Bob gửi B cho Alice, Alice gửi A cho Bob
    sA = pow(B, a, p)
    sB = pow(A, b, p)
    
    if sA == sB:
        print('Số bí mật chung là: ', sA)
    else:
        print('Lỗi thuật toán!!')

    start_time = time.time()
    while True:
        r = getRamdomBigInt()
        # r = int(input('Chọn một số r (r là người quan sát): '))
        R = pow(g, r, p)
        sRA = pow(A, r, p)
        sRB = pow(B, r, p)
        print(f'Số s mà r tính được dựa vào (p, g, A, B) là: {sRA} và {sRB}, s là {sA}')
        if sRA == sA or sRB == sA:
            if sRA == sA:
                print('r đã lấy được số bí mật s', sRA)
            elif sRB == sA:
                print('r đã lấy được số bí mật s', sRB)
            break
        end_time = time.time()
        if end_time - start_time > 5:
            break
        #print('time = ', end_time - start_time)



if __name__ == '__main__':
    main()
    
    #print(pow(5, 8 * 19, 23))