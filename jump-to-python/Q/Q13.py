def gugudan(n) :
    if n in list(range(2,10)) :
        for i in list(range(2,10)) :
            print("%d * %d = %d" % (n, i, n*i) ) 
    else :
        print("2에서 9까지의 숫자만 입력하세요.")


n = input("구구단 몇단을 해볼까요?")
gugudan(int(n))