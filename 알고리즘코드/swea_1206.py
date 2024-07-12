n = int(input())
arr = list()
arr2 = list()
sol = 0
arr.append(list(map(int, input().split())))

for i in range(n):
    if i < 2 or i > n-3:
        continue
    else:
        l1 = arr[i] - arr[i-1]
        r1 = arr[i] - arr[i+1]
        l2 = arr[i] - arr[i-2]
        r2 = arr[i] - arr[i+2]
        arr2.append(l1)
        arr2.append(r1)
        arr2.append(l2)
        arr2.append(r2)

        if l1 > 0 and r1 > 0:
            if l2 > 0 and r2 > 0:
                sol = sol + arr2.min()
    print(sol)