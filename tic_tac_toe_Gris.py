le_bord = list(range(1,10))

def draw_board(le_bord):
    print ("-" * 13)
    for i in range(3):
        print ("|", le_bord[0+i*3], "|", le_bord[1+i*3], "|", le_bord[2+i*3], "|")
        print ("-" * 13)

def take_input(token):
    valid = False
    while not valid:
        answer = input("Point the number of the cell  " +token+"? ")
        try:
            answer = int(answer)
        except:
            print ("You must submit the number of the cell")
            continue
        if answer >= 1 and answer <= 9:
            if (str(le_bord[answer-1]) not in "XO"):
                le_bord[answer-1] = token
                valid = True
            else:
                print ("This cell is filled")
        else:
            print ("Enter the numbers between 1 and 9 ")

def check_win(le_bord):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if le_bord[each[0]] == le_bord[each[1]] == le_bord[each[2]]:
            return le_bord[each[0]]
    return False

def main(le_bord):
    counter = 0
    win = False
    while not win:
        draw_board(le_bord)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "La victiore est avec toi!")
                win = True
                break
        if counter == 9:
            print ("С'est le faire match nul!")
            break
    draw_board(le_bord)

main(le_bord)


