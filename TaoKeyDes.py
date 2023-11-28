BANG_THAP_LUC_PHAN = '0123456789ABCDEF'
BANG_HOAN_VI_PC1 = '57 49 41 33 25 17 9 1 58 50 42 34 26 18 10 2 59 51 43 35 27 19 11 3 60 52 44 36 63 55 47 39 31 23 15 7 62 54 46 38 30 22 14 6 61 53 45 37 29 21 13 5 28 20 12 4'
BANG_HOAN_VI_PC2 = '14 17 11 24 1 5 3 28 15 6 21 10 23 19 12 4 26 8 16 7 27 20 13 2 41 52 31 37 47 55 30 40 51 45 33 48 44 49 39 56 34 53 46 42 50 36 29 32'
BANG_DICH_CHUYEN_TRAI = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
BANG_HOAN_VI_IP = '58 50 42 34 26 18 10 2 60 52 44 36 28 20 12 4 62 54 46 38 30 22 14 6 64 56 48 40 32 24 16 8 57 49 41 33 25 17 9 1 59 51 43 35 27 19 11 3 61 53 45 37 29 21 13 5 63 55 47 39 31 23 15 7'
BANG_LUA_CHON_BIT_E = '32 1 2 3 4 5 4 5 6 7 8 9 8 9 10 11 12 13 12 13 14 15 16 17 16 17 18 19 20 21 20 21 22 23 24 25 24 25 26 27 28 29 28 29 30 31 32 1'
BANG_S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]], 
[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],  
[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]], 
[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]], 
[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]], 
[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
BANG_HOAN_VI_P = '16 7 20 21 29 12 28 17 1 15 23 26 5 18 31 10 2 8 24 14 32 27 3 9 19 13 30 6 22 11 4 25'
BANG_HOAN_VI_IP_1 = '40 8 48 16 56 24 64 32 39 7 47 15 55 23 63 31 38 6 46 14 54 22 62 30 37 5 45 13 53 21 61 29 36 4 44 12 52 20 60 28 35 3 43 11 51 19 59 27 34 2 42 10 50 18 58 26 33 1 41 9 49 17 57 25'

# matrix_list = ' '.join(BANG_IP_1.replace('\n', ' ').strip().split())
# # matrix_list = [(NEW) for NEW in BANG_S2.split('\n')]
# listnew = []
# listnew2 = []
# # for i in matrix_list:
# #     listnew.append(int(i))
# # for i in range(4): 
# #     listnew[i] = ' '.join(matrix_list[i].split())
# # for i in range(4):
# #     for j in listnew[i].split():
# #         listnew2[i].append(int(j))
# print(matrix_list)
#in chuỗi bin ra màn hình
def OutScreen(message, num=7):
    translate = ''
    index = 0
    for char in message:
        translate += char
        index = (index + 1) % num
        if index == 0:
            translate += ' '    
    return translate

#chuyển đổi thập lục phân sang nhị phân
def Hex2Bin(hexNum, len1Hex=4):
    binNum = ''
    for char in hexNum:
        binNum += bin(BANG_THAP_LUC_PHAN.find(char))[2:].zfill(len1Hex)
    return binNum

#chuyển đổi thập phân sang nhị phân
def Dec2Bin(decNum, lenDec=4):
    return bin(decNum)[2:].zfill(lenDec)
    
#Chuyển đổi nhị phân sang thập lục phân
def Bin2Hex(binNum, lenBinTo1Hex=16):
    return hex(int('0b' + binNum, 2))[2:].zfill(lenBinTo1Hex).upper()

#hoán vị các bit(nhập vào bảng hoán vị, đầu ra có cùng độ dài với bản hoán vị)
def HoanViBit(binNum, bangHoanVi):
    binKetQua = ''
    for i in bangHoanVi.split(' '):
        binKetQua += binNum[int(i) - 1]
    return binKetQua

#chia thành các chuỗi con có cùng độ dài
def ChiaChuoi(message, num=2):
    sub = ['' for _ in range(num)]
    lenSub = int(len(message) / num)
    for i in range(num):
        sub[i] = message[i*lenSub:(i+1)*lenSub]
    return sub

#dịch chuyển trái 
def DichChuyenTrai(message, num):
    sub1 = message[num:]
    sub2 = message[:num]
    return sub1 + sub2

#tạo 16 key
def CreateKey(key):
    K_bin = Hex2Bin(key)
    Kp_bin = HoanViBit(K_bin, BANG_HOAN_VI_PC1)
    C = ['' for _ in range(17)]
    D = ['' for _ in range(17)]
    CD = ['' for _ in range(17)]
    K = ['' for _ in range(17)]
    C[0] = ChiaChuoi(Kp_bin)[0]
    D[0] = ChiaChuoi(Kp_bin)[1]

    for i in range(1, 17):
        C[i] = DichChuyenTrai(C[i-1], BANG_DICH_CHUYEN_TRAI[i-1])
        D[i] = DichChuyenTrai(D[i-1], BANG_DICH_CHUYEN_TRAI[i-1])
        CD[i] = C[i] + D[i]
        K[i] = HoanViBit(CD[i], BANG_HOAN_VI_PC2)
        # print(f'K{i} = ', OutScreen(K[i], 6))
    return K

#phép xor cho bit
def Xor(bin1, bin2):
    if len(bin1) != len(bin2):
        return 
    lenBin = len(bin1)
    bin1 = int('0b' + bin1, 2)
    bin2 = int('0b' + bin2, 2)
    ketQua = bin(bin1 ^ bin2)[2:].zfill(lenBin)
    return ketQua

def HangCot(bin):
    hang = int('0b' + bin[0] + bin[5], 2)
    cot = int('0b' + bin[1:5], 2)
    return [hang, cot]

def SnPn(KE_bin):
    if len(KE_bin) != 48:
        print('lỗi không đủ 48 kí tự')
        return
    KE = OutScreen(KE_bin, 6).split(' ')
    S = []
    for i in range(8):
        hang = HangCot(KE[i])[0]
        cot = HangCot(KE[i])[1]
        num = BANG_S[i][hang][cot]
        S.append(num)
    return ''.join((Dec2Bin(num)) for num in S)

# ke = '011000010001011110111010100001100110010100100111'
# print(OutScreen(ke, 6))
# print(OutScreen(SnPn(ke), 4))
# print('0101 1100 1000 0010 1011 0101 1001 0111')

def MaHoaDes(message, key):
    K = CreateKey(key)
    M_bin = Hex2Bin(message)
    IP = HoanViBit(M_bin, BANG_HOAN_VI_IP)
    
    L = ['' for _ in range(17)]
    R = ['' for _ in range(17)]
    E = ['' for _ in range(17)]
    KE = ['' for _ in range(17)]
    S = ['' for _ in range(17)]
    F = ['' for _ in range(17)]

    L[0] = ChiaChuoi(IP)[0]
    R[0] = ChiaChuoi(IP)[1]
    for i in range(1, 17):
        L[i] = R[i-1]
        E[i-1] = HoanViBit(R[i-1], BANG_LUA_CHON_BIT_E)
        KE[i] = Xor(E[i-1], K[i])
        S[i] = SnPn(KE[i])
        F[i] = HoanViBit(S[i], BANG_HOAN_VI_P)
        R[i] = Xor(L[i-1], F[i])
    
    RL = R[16] + L[16]
    IP_1 = HoanViBit(RL, BANG_HOAN_VI_IP_1)
    C = Bin2Hex(IP_1)
    return C

def Main():
    K_hex = '133457799BBCDFF1'
    M_hex = '0123456789ABCDEF'
    M =     '0129191919192992'
    C = MaHoaDes(M, K_hex)
    print(C)

if __name__ == '__main__':
    Main()

