T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    st_n, sub_n = map(int, input().split())
    st_li = list(map(lambda x : x + 1, range(st_n)))
    sub_li = list(map(int, input().split()))
    sub_li.sort()
    n = 0
    for i in sub_li:
        st_li.pop(i-1-n)
        n = n + 1
    for i in range(len(st_li)):
        if i == 0:
            print(f"#{test_case}", end=' ')
        print(st_li[i],end = ' ')
    print()