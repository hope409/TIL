import sys
sys.stdin = open('input.txt', 'r')

def horizontal(li, n, k):
    cnt = 0
    for col in range(n + 1 - k):
        for row in range(n + 1 - k):
            status = True
            for i in range(k):
                if li[col][row + i] != 1:
                    status = False
                    break
            if row + 2 < n and status == True:
                if li[col][row + 2] == 1:
                    status = False
            
            if status == True:
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

    print(horizontal(arr, n, k))
    # print(f"#{test_case} {horizontal(arr) + vertical(arr)}")
    
