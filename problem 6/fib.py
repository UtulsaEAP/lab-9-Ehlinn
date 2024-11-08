def fibonacci(n):
    fibnum = 1
    fibtwo = 0
    fibval = 0
    if n < 0:
        fibval = -1
    elif n == 1:
        fibval = 1
    while n > 1:
        fibprev = fibnum
        fibnum = fibnum + fibtwo
        fibval = fibnum
        fibtwo = fibprev
        n += -1
    return fibval
if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')