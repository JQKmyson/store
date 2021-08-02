from threading import Thread
import time

breads = 0


class Cook(Thread):
    username = ""
    bread = 0

    def run(self) -> None:
        global breads
        while True:
            if breads < 600:
                time.sleep(0.5)
                self.bread += 1
                breads += 1
                print("厨师", self.username, "做了", self.bread, "个面包")
                print("销售柜台总共有",breads,"个面包")
            elif breads == 600:
                    time.sleep(0.5)


class Customer(Thread):
    username = ""
    money = 3000
    count = 0

    def run(self) -> None:
        global breads
        while True:
            if self.money > 0:
                if breads > 0:
                    breads -= 1
                    self.money -= 2
                    self.count += 1
                    print("顾客", self.username, "已买了",self.count)
                elif breads == 0:
                    time.sleep(1)
            elif self.money == 0:
                print("顾客", self.username, "已消费完" )
                break


cook1 = Cook()
cook2 = Cook()
cook3 = Cook()
cook1.username = "王嘉奇"
cook2.username = "乐东楊"
cook3.username = "李禹成"
shopper1 = Customer()
shopper2 = Customer()
shopper3 = Customer()
shopper4 = Customer()
shopper5 = Customer()
shopper6 = Customer()
shopper1.username = "1"
shopper2.username = "2"
shopper3.username = "3"
shopper4.username = "4"
shopper5.username = "5"
shopper6.username = "6"
cook1.start()
cook2.start()
cook3.start()
shopper1.start()
shopper2.start()
shopper3.start()
shopper4.start()
shopper5.start()
shopper6.start()