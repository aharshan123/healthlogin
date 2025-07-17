
#Exception

# a = 10
# print(a/0)
# print(b)
# 'hello'.append('h')
# {1,2,3}.remove(7)
# 'hell'[10]
'''
try:
    a = int(input())
    b = int(input())
    res = a/b
except (IndexError,ZeroDivisionError):
    print("exception handled")
else:
    print(res)
finally:
    print("end")

'''

class Bank:
    def __init__(self, cid, cname, bal, acno):
        self.cid = cid
        self.cname = cname
        self.bal = bal
        self.acno =  acno

    def withdrawl(self, amount):
        if self.bal>= amount:
            self.bal -= amount
            print("please collect your cash")
        else:
            raise Exception("insufficient bal")


c1 = Bank(1, 'dinga', 1000, 12345)
c1.withdrawl(700)














