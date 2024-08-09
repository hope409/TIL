# Stack4

## 백트래킹
### 부분집합
### 순열

## 가지치기

## 분할정복

### 백트래킹 기법으로 powerset 만들기
---
- n개의 원소가 들어있는 집합을 만들때 true, false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용(상태 집합 만들기)

### powerset 백트래킹 알고리즘
---
``` python
def backtrack(a, k, n): # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end = ' ')
    print()

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1, 2, 3, 4]
backtrack(a, 0, 3)
```

### 순열을 생성하는 방법
``` python
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```

