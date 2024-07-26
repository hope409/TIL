import sys
sys.stdin = open('input.txt', 'r')

def horizontal(li):
    global n, k
    cnt = 0
    for col in range(n):
        for row in range(n + 1 - k):
            if row + k == n:
                if li[col][row] == 1:
                    val = 0
                    for i in range(1, k):
                        if li[col][row + i] == 0:
                            break
                        val = 1
                    if val == 1:
                        cnt = cnt + 1
            else:
                if li[col][row] == 1 and li[col][row + k] == 0:
                    val = 0
                    for i in range(1, k):
                        if li[col][row + i] == 0:
                            break
                        val = 1
                    if val == 1:
                        cnt = cnt + 1
    return cnt

def vertical(li):
    global n, k
    cnt = 0
    for row in range(n):
        for col in range(n + 1 - k):
            if col + k == n:
                if li[col][row] == 1:
                    val = 0
                    for i in range(1, k):
                        if li[col + i][row] == 0:
                            break
                        val = 1
                    if val == 1:
                        cnt = cnt + 1
            else:
                if li[col][row] == 1 and li[col + k][row] == 0:
                    val = 0
                    for i in range(1, k):
                        if li[col + i][row] == 0:
                            break
                        val = 1
                    if val == 1:    
                        cnt = cnt + 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    n, k = tuple(map(int, input().split()))
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(f"#{test_case} {horizontal(arr) + vertical(arr)}")
    
