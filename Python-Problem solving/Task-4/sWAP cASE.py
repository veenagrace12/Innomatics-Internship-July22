def swap_case(s):
    str_swap = ""
    for str_letter in s:
        if str_letter.isupper() == True:
            str_swap+=(str_letter.lower())
        else:
            str_swap+=(str_letter.upper())
    return str_swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)