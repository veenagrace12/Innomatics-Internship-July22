def minion_game(string):
    # your code goes here
    vowel = 'aeiou'.upper()
    player1 = 0; #kevin
    player2 = 0; #stuart
    str_len = len(string)
    for i in range(str_len):
        if s[i] in vowel:
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 == player2:
        print("Draw")
    elif player1 > player2:
        print("Kevin", player1)
    else:
        print("Stuart",player2)
    

if __name__ == '__main__':
    s = input()
    minion_game(s)