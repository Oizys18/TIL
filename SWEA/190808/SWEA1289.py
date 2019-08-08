# SWEA 1289 메모리 복구

def binIt(bit_len):
    binNum = int(bin((1<<bit_len)-1)[-(bit_len):])
    return binNum

for T in range(int(input())):
    aim = int(input())      
    bit_len = len(str(aim))
    cnt = 1
    bit_try = int(bin((1<<bit_len)-1)[-(bit_len):])
    
    while True:
        if aim == bit_try:
            print("#{0} {1}".format(T+1,cnt))
            break

        elif aim < bit_try: 
            cnt += 1
            diff = len(str(bit_try - aim))
            bit_try = bit_try - binIt(diff)

        elif aim > bit_try:
            cnt += 1
            diff = len(str(aim - bit_try))
            bit_try = bit_try + binIt(diff)