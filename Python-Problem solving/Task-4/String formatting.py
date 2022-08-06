def print_formatted(number):
    # your code goes here
    n = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print(f"{i:{n}d} {i:{n}o} {i:{n}X} {i:{n}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)