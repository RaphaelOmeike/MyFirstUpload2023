# # Diamond triangle advanced
# i, j= 0, 1
# input = 5
# while i < input:
#     k = 0
#     if i != 0:
#         print(" " * (input - i), end="")
#     while k < i:
#         print(f"{j}", end=' ')
#         j += 1
#         k += 1
#     if i != 0:
#         print()
#     i += 1

for i in range(50):
    if (i % 3 != 0) and (i % 7 != 0):
        print(i, end=" ")