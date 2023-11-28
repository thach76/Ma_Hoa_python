#Mã dịch vòng
# A	0	N	13
# B	1	O	14
# C	2	P	15
# D	3	Q	16
# E	4	R	17
# F	5	S	18
# G	6	T	19
# H	7	U	20
# I	8	V	21
# J	9	W	22
# K	10	X	23
# L	11	Y	24
# M	12	Z	25

#LÝ THYẾT
# Mã hóa: Y[i] = (X[i] + k mod N)
# Giải mã: X[i] = (Y[i] - k mod N)

#MÃ HÓA input x = "HELLOWORD" K = 8
#kết quả: PMTTWEWZL

#GIẢI MÃ input x = "HELLOWORD" K = 8
#kết quả: ZWDDGOGJV

# x = input("Nhập vào chuỗi cần mã hóa: ")
# print(x)

BANGCHUCAI = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Ceacer(x, k, mode):
    x = x.upper()
    y = ""
    for i in x:
        if i in BANGCHUCAI:
            xc = ord(i) - ord('A')
            if mode == 1:
                yc = (xc + k) % 26
            elif mode == 2:
                yc = (xc - k) % 26
            else:
                return ""
            y += chr(yc + ord('A'))
        else:
            y += i
    return y

def Menu():
    print("1. Mã hóa")
    print("2. Giải mã")
    print("Còn lại. Thoát")
    

while True:
    x = input("\nnhập vào 1 chuỗi: ")
    k = int(input("nhập khóa: "))
    Menu()
    chon = int(input("vui lòng chọn mã hóa hoặc giải mã: "))
    if (chon == 1):
        print("kết quả mã hóa: " + Ceacer(x, k, chon))
    elif (chon == 2):
        print("kết quả mã hóa: " + Ceacer(x, k, chon))
    else:
        print("DONE")
        break