import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
# arr의 type이 list로 나오지 않고, numpy.ndarray로 나온다. -> numpy는 선형대수
print(type(arr))
print(arr)

# arr = np.random.rand(100)
arr = np.random.randn(10)
print(arr)

# plt.plot(arr)
# plt.show()

# arr = np.random.rand(10000)
arr = np.random.normal(5, 3, 10000)
print(arr)

# 평균
print(arr.mean())

# 합계
print(arr.sum())

# 표준편차
print(arr.std())

# 분산
print(arr.var())

# 최대값
print(arr.max())

# 최소값
print(arr.min())

# 최대값 최소값 위치
print(arr.argmax(), arr.argmin())

# subplots(row, col)
# fig, subplots = plt.subplots(2, 2)
# fig, subplots = plt.subplots(1, 2)
fig, subplots = plt.subplots(2, 1)

# subplots[0, 0].plot(arr)
# subplots[0, 1].hist(arr, edgecolor='black', linewidth=1.2)
subplots[0].plot(arr)
subplots[1].hist(arr, bins=10, edgecolor='black', linewidth=1.2)

plt.show()
