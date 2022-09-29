
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()


# with open('file.txt', 'a') as data:
#     data.write('\nLine 11111\n')
#     data.write('Line 22222\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# import hello as h

# print(h.f(1))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))



# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))



# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34



# Кортежи

# # a = (3, 4)
# a = (3,)
# print(a)
# print(a[0])
# print(a[-1])

a = (3, 4, 5)
for item in a:
    print(item)

