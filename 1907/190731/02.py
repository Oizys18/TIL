for i in range(int(input())):
    l = list(map(int,input().split()))
    print(f"#{i+1} {max([l.count(x) for x in l])}")