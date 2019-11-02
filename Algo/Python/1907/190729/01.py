# SW.EA  D2 1945. 소인수 분해
# 내 코드 
for i in range(int(input())):
    N = int(input())
    print(f"#{i+1}",end=' ')
    a = b = c = d = e = 0
    while N != 1:
        if N % 2 == 0:
            N = N / 2
            a += 1
        elif N % 3 == 0:
            N = N / 3 
            b += 1
        elif N % 5 == 0:
            N = N / 5
            c += 1
        elif N % 7 == 0:
            N = N / 7 
            d += 1
        elif N % 11 == 0:
            N = N / 11
            e += 1
    print(f"{a} {b} {c} {d} {e}")


# vincentj의 코드
for T in range(int(input())):
    N=int(input())
    t=''
    for i in (2,3,5,7,11):
        d=0
        while N%i==0:
            d+=1
            N/=i
        t+=str(d)+' '
    print(f'#{T+1} {t}')