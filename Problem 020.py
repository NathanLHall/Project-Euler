def main(number):
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i

    length = len(str(factorial))
    sum = 0
    for i in range(length):
        sum += factorial % 10
        factorial = factorial // 10
    return sum

if  __name__ == "__main__":
        number = 100
        result = main(number)
        print(result)