import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    farm_li = [list(map(int, input())) for _ in range(n)]
    # print(farm_li)
    val = 0
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            if n // 2 + j != n // 2 - j:
                if i != n - 1 - i:
                    val += farm_li[i][n // 2 - j]
                    val += farm_li[i][n // 2 + j]
                    val += farm_li[n - 1 - i][n // 2 - j]
                    val += farm_li[n - 1 - i][n // 2 + j]
                else:
                    val += farm_li[i][n // 2 - j]
                    val += farm_li[i][n // 2 + j]
            else:
                if i != n - 1 - i:
                    val += farm_li[i][n // 2]
                    val += farm_li[n - 1 - i][n // 2]
                else:
                    val += farm_li[i][n // 2]

    print(f"#{test_case} {val}")