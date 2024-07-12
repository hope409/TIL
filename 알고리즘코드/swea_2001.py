T = int(input())
for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    max = 0
    pre = 0
    arr = list()
    
    for col in range(m):
        arr.append(list(map(int, input().split())))
    # print(arr)
    
    for i in range(m - n + 1):
        for j in range(m - n + 1):
            pre = 0
            for k in range(n):
                for l in range(n):
                    pre = pre + arr[i+k][j+l]
                    if pre >= max:
                        max = pre
                    # print(f"pre : {pre}")
                    # print(f"max : {max}")
    
    print(f"#{test_case} {max}")

