from base64 import b64decode as b64

for t in range(int(input())):
    print(f"#{t+1} {str(b64(input()))[2:-1]}")
