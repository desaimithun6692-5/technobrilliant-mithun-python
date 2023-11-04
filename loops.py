# # loops
#
# # initialization
# i = 0
#
# # condition
# # increament
#
# # while i <= 100:
# #     print(i)
# #     i += 1
#
# # text = "python"
# #
# # for i in text:
# #     print(i)
#
# for i in [10, 20, 30, 40]:
#     print(i)
#
# for i in range(10, 100):
#     print(i)
#
# for i in ["abc", "xyz", "pqr"]:
#     print(i)


# sum any 1 to n number


# Nested loops

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')
#
# # 2 d list
# list = [1, 2, 3]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     for i in row:
#         print(i)
#
# for row in matrix:
#     print(row)
#
#
#
# sum = 0
# for row in matrix:
#     for i in row:
#        sum+=i
#
#
#
#
#
# print(sum)
#
# print(matrix[1][2])
# print(matrix[2][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max = 0
for row in matrix:
    for i in row:
        if max < i:
            print("inside loop", i)
            max = i
print(max)
