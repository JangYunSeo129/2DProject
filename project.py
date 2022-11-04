inter = 5
tax = 25
money = int(input("저축금액을 입력하시오.: "))
print("원금:    {0:d}\n이자:     {1:d}\n세금:      {2:d}\n최종:    {3:d}".format(money, money//20, (money//20)//4, money + money//20 -(money//20)//4))