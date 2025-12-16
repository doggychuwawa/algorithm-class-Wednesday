# 문제 2. 여행 짐 꾸리기 최적 패킹 프로그램 (0/1 Knapsack, Bottom-up DP)

W = int(input("배낭 용량을 입력 하세요 : "))

items = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
wt = [3, 1, 2, 2, 1]
val = [12, 10, 6, 7, 4]

n = len(items)

A = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):
        if wt[i - 1] > w:
            A[i][w] = A[i - 1][w]
        else:
            A[i][w] = max(
                A[i - 1][w],
                val[i - 1] + A[i - 1][w - wt[i - 1]]
            )

max_value = A[n][W]

selected_items = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:
        selected_items.append(items[i - 1])
        w -= wt[i - 1]

selected_items.reverse()

print("최대 만족도:", max_value)
print("선택된 물건:", selected_items)
