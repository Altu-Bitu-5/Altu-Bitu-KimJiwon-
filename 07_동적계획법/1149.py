# 1번 집의 색은 2번 집의 색과 동일하면 안 됨

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

    """
        26 40 83
        49 60 57
        13 89 99
    """

for i in range(1, n):  # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0] = min(a[i - 1][1], a[i - 1][2]) + a[i][0]  # 40 + 49 =89, 83 + 13 = 96
    a[i][1] = min(a[i - 1][0], a[i - 1][2]) + a[i][1]  # 26 + 60 =86, 83 + 89
    a[i][2] = min(a[i - 1][0], a[i - 1][1]) + a[i][2]  # 26 + 57 =83, 86 + 99

print(min(a[n - 1][0], a[n - 1][1], a[n - 1][2]))  # 96
