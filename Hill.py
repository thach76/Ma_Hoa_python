import numpy as np
np.set_printoptions(suppress=True)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#tính det(k) k là ma trận m * m
def Det(A, modulo=26):
    det = np.linalg.det(A)
    det =  int(np.round(det, decimals=1))
    return det % modulo

#nhập ma trận k sao cho k là khả nghịch (det(k) != 0)
def NhapMaTran(m):
    while True:
        matrix = np.zeros((m,m))
        
        for i in range(m):
            for j in range(m):
                matrix[i, j] = int(input(f'Nhập giá trị cho phần tử [{i+1}, {j+1}]: '))

        if Det(matrix) == 0:
            print('Ma trận không khả nghịch! Vui lòng thử lại')
        else:
            # print('Khóa của bạn là: \n', matrix)
            return
        return matrix

#nhân ma trận (1 * m )(m * m)
def Nhan2MaTran(matrix1, matrix2, modulo=26):
    result = np.dot(matrix1, matrix2) % modulo
    return result


def Ucln(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#tìm module của a (a*i ≡ 1 mod m hay tìm i sao cho a * i chia cho m dư 1)
def Module(a, m=26):
    if Ucln(a, m) != 1:
        return None
    i = 1
    while True:
        if a * i % m == 1:
            return i % m
        if i > 1000:
            return None
        i+=1

def LayMaTranCon(matrix, hang, cot):
    # Tạo ma trận con bằng cách xóa hàng và cột cụ thể
    ma_tran_con = np.delete(np.delete(matrix, hang, axis=0), cot, axis=1)
    return ma_tran_con

#tính nghỉnh đảo của na trận
def TinhNghichDao(matrix):
    nghichDaoDet = Module(Det(matrix))

    
    m = matrix.shape[0]
    
    phuDaiSo = -1
    if m == 3:
        matrix = np.transpose(matrix)
        AdjList = [[], [], []]
        for i in range(m):
            for j in range(m):
                matrixSub = LayMaTranCon(matrix, i, j)
                phuDaiSo *= -1
                det = Det(matrixSub) * phuDaiSo
                AdjList[i].append(det)
        AdjMatrix = np.array(AdjList)
        AdjMatrix = AdjMatrix % 26
        nghichDaoMatrix = AdjMatrix * nghichDaoDet
        nghichDaoMatrix = nghichDaoMatrix % 26

        return nghichDaoMatrix
    if m == 2:
        AdjMatrix = np.array([[matrix[1][1], -matrix[0][1]],
                              [-matrix[1][0], matrix[0][0]]])
        AdjMatrix = AdjMatrix % 26
        nghichDaoMatrix = AdjMatrix * nghichDaoDet
        nghichDaoMatrix = nghichDaoMatrix % 26

        return nghichDaoMatrix
    

def ThayThe(message:str, goc:str):
    out = ''
    index = 0
    for char in goc:
        if char in LETTERS:
            if index < len(message):
                out += message[index]
                index+=1
        else:
            out += char
    return out

def RemodeNonLetter(message:str):
    out = ""
    for char in message:
        if char in LETTERS:
            out+=char
    return out
            

#mật mã hill
#mã hóa: y = x * k
#giải mã: x = y * k^-1
#k là ma trận vuông cấp m * m
#x và y là ma trận 1 * m 
#nếu x không đủ để thành ma trận 1 * m thì thêm kí tự x vào đằng sau
def HillCipher(message:str, key: np, mode='MAHOA'):
    m = key.shape[0]
    
    message = message.upper()
    goc = message
    message = RemodeNonLetter(message)

    while True:
        if len(message) % m != 0:
            message += 'X'
            goc += 'X'
        else:
            break

    
    keyNghichDao = TinhNghichDao(key)
    translated = ""
    messageSub = []

    for char in message + 'X': #duyệt mảng đầu vào
        if char in LETTERS: #kiểm tra xem có phải chữ cái không
            charIndexLetters = LETTERS.find(char) #lấy giá trị của chữ cái 
            if len(messageSub) == m: #nếu là ma trận 1 * m 
                if mode == 'MAHOA': #chế độ mã hóa
                    x = np.array(messageSub) #khởi tạo ma trận
                    ketqua = Nhan2MaTran(x, key) % len(LETTERS)
                    #print("Giá trị của ketqua[0][i]:", ketqua[2])
                    for i in range(m): #chạy m phần tử
                        translated += LETTERS[ketqua[i]] #trả về kết quả mã hóa
                if mode == 'GIAIMA':     
                    x = np.array(messageSub) #khởi tạo ma trận
                    ketqua = Nhan2MaTran(x, keyNghichDao) % len(LETTERS)
                    #print("Giá trị của ketqua[0][i]:", ketqua[2])
                    for i in range(m): #chạy m phần tử
                        translated += LETTERS[ketqua[i]] #trả về kết quả mã hóa
                messageSub = []
                messageSub.append(charIndexLetters)
            else:
                messageSub.append(charIndexLetters)

    translated = ThayThe(translated, goc)

    return translated

#main
def Main():
    print('hello, world')
    # Tạo một ma trận vuông A
    A = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    B = np.array([1, 2, 4])

    message = "I Love you"
    message2 = 'U BGRI CEM'
    sub = ''
    key = np.array([[3, 3],
                    [2, 5]])
    
    # key = np.array([[17, 17, 5],
    #              [21, 18, 21],
    #              [2, 2, 19]])
    # key = np.array([[1, 2, 3],
    #              [0, 1, 4],
    #              [5, 6, 0]])
    print(HillCipher(message, key, "MAHOA"))
    print(HillCipher(message2, key, "GIAIMA"))
    #print(TinhNghichDao(key))


if __name__ == '__main__':
    Main()
