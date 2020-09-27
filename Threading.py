#from threading import *
#from time import sleep

class Athlete1(Thread):
    def run(self):
        for i in range(100):
            print('Athlete 1 running')
            #sleep(1)


class Athlete2(Thread):
    def run(self):
        for i in range(100):
            print('Athlete 2 running')
            #sleep(1)


class Athlete3(Thread):
    def run(self):
        for i in range(100):
            print('Athlete 3 running')
            #sleep(1)

a1 = Athlete1()
a2 = Athlete2()
a3 = Athlete3()

#a1.run()
#a2.run()
#a3.run()

a1.start()
#sleep(0.1)

a2.start()
#sleep(0.1)

a3.start()

#a1.join()
#a2.join()
#a3.join()

print('Lap finished')
