def main():
    x = int(input("Qual é o X? "))
    print("x é", square(x))


def square(n):
    return pow(n, 2)


main()