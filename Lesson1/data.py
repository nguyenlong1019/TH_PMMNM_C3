import random
a = int(input("Nhập số ẩn: "))

with open('data2.txt', 'a') as f:
    f.write('1000\n')
    for i in range(a):
        for j in range(a+1):
            txt = f"{random.randint(0,1000)} "
            f.write(txt)
        f.write('\n')