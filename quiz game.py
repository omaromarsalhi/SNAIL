
while True:
    qst = {"who is the big bastard?: ": "A", "who is the bitch?: ": "C", "who is the gay?: ": "D"
        , "how do the face of louay look like?: ": "C"}

    answers = [["A. louay","B. touhemi","C. zambala","D. chalbeya"],["A. taher","B. 7med","C. louay","D. bhiim"],
           ["A. 7ssin","B. fathi","C. kamel","D. louay"],["C. ass","C. ass","C. ass","C. ass"]]
    def show():
        gusses=[]
        k = 0
        for key in qst:
            print(key)
            for i in answers[k]:
                print(i)
            k+=1
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            gusses.append(input('give ana answer A/B/C/D: ').upper())
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        ball = list(qst)
        s = 0
        score = 0
        for i in range(4):
            crr_ans = qst.get(ball[s])
            if gusses[s] == crr_ans:
                score += 1
            else:
                score += 0
            s += 1
        result = int((score * 100) / 4)
        print('your answers are: ', gusses)
        print('right answer are: A C D C ')
        print('your score is: ', result, '%')
        if score <= 2:
            print('you are an idiot')
        elif score == 3:
            print("hah it's okey nesxt time i will call you an idiot idiot")
        else:
            print("you are intellegent idiot")
    show()
    ply_again=input('you wanna play again yes or no').upper()
    if  ply_again== "NO":
        break


