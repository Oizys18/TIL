# SWEA 1976. 시각덧셈
for t in range(int(input())):
    time = list(map(int,input().split()))
    ntime = divmod((time[0]+time[2])*60 + time[1] + time[3],60)
    print(f"#{t+1} {ntime[0] if ntime[0]<= 12 else ntime[0]-12} {ntime[1]}")
