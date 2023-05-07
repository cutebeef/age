driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit #程式在此中斷

age = input('請問你的年齡？')
age = int(age)
if driving == '有':
    if age >= 18 :
        print('你很棒，守法的公民')
    else:
        print('抓到了，你怎麼能開車!')
elif driving == '沒有':
    if age >=18 :
        print('怎麼還不去考駕照？')
    else:
        print('再等個幾年就可以考駕照了')