# 수도 요금 경쟁 
for i in range(int(input())):
    print(f"#{i+1}",end=' ')
    li = input().split(' ')
    P = int(li[0]) 
    Q = int(li[1]) 
    R = int(li[2]) 
    S = int(li[3]) 
    W = int(li[4]) 
     
    if W <= R:
        print(f"{W*P > Q and Q or W*P < Q and W*P}")
    elif W > R:
        print(f"{(W*P) < Q+(W-R)*S and W*P or (W*P) > Q+(W-R)*S and Q+(W-R)*S}")

 
for i in range(int(input())):
    P,Q,R,S,W = map(int,input().split(' '))
    print(f"#{i+1} {min(P*W,max(Q, Q+(W-R)*S))}")