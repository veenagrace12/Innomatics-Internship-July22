def merge_the_tools(string, k):
    import textwrap
    # your code goes here
    for i in textwrap.wrap(string, k):
        lst = list()
        for j in i:
            if not j in lst:
                lst.extend(j)
        print(''.join(lst))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)