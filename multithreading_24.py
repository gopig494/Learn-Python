from threading import Thread

class Multi(Thread):
    def fun(self):
        for i in range(10):
            print('i am child')

def  callme():
    for i in range(10):
        print("call me")
a=Multi()
ac=Thread(target=a.fun)
ac.start()
bc=Thread(target=callme)
bc.start()
ac.join()
bc.join()

for i in range(10):
    print("i am main")
for j in range(10):
    print('i am sub main')

