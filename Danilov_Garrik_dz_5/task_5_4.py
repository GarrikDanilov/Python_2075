# Задание 4

# import time
# import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# start = time.perf_counter()
def get_numbers(src: list):
    return (src[index] for index in range(1, len(src)) if src[index] > src[index - 1])


print(*get_numbers(src))
# print(time.perf_counter() - start)
# print(sys.getsizeof(get_numbers(src)))
