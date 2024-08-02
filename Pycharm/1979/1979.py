import sys

sys.stdin = open('input.txt', 'r')

def check_width(arr, col, row, check):
    global n, k
    if 0 < row < n - k:
        if arr[col][row - 1] == 1:
            return 0
        else:
            for i in check:
                if i != k:
                    if arr[col][row + i] != 1:
                        return 0
                else:
                    if arr[col][row + i] == 1:
                        return 0
            return 1
    elif row == 0:
        for i in check:
            if arr[col][row + i] != 1:
                return 0
        return 1
    else:
        if arr[col][row - 1] == 1:
            return 0
        else:
            for i in check[:-1]:
                if arr[col][row + i] != 1:
                    return 0
            return 1


t = int(input())
for test_case in range(1, t + 1):
    n, k = tuple(map(int, input().split()))
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    check_list = [i for i in range(1, k + 1)]
    cnt = 0
    for col in range(n):
        for row in range(n + 1 - k):
            if arr[col][row] == 1:
                cnt += check_width(arr, col, row, check_list)
                # cnt += check_width(arr, row, col, check_list)
    print(cnt)
