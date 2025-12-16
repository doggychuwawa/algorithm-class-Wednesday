# 문제 1. 계단 오르는 방법의 수 계산 프로그램 (Bottom-up DP)

n = int(input("계단의 개수를 입력하시오: "))

dp = [0] * (n + 1)
dp[0] = 1
if n >= 1:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(f"{n}개의 계단을 오르는 방법의 수는 {dp[n]}가지입니다.")
