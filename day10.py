# class cup:
#     __usercup:""
#     __height = ""
#     __capacity = ""
#     __colour = ""
#     __tom = ""
#     def setuUserup(self,usercup):
#         self.__usercup = usercup
#
#     def setHeight(self,height):
#         if height < 0 or height > 30:
#             print("对不起，高度过高")
#         else:
#             self.__height = height
#
#     def setCapacity(self,capacity):
#         if capacity < 0 or capacity > 3000:
#             print("对不起，容量过高")
#         else:
#             self.__capacity = capacity
#     def setColour(self,colour):
#         self.__colour = colour
#     def setTom(self,tom):
#         self.__tom = tom
#
#     def tea(self,teaname):
#         print(self.__usercup,"灌满了",teaname)
#     def teamilk(self,teamilkname):
#         print(self.__usercup,"灌满了",teamilkname)
#     def ed(self,edname):
#         print(self.__usercup,"灌满了",edname)
#     def water(self,watername):
#         print(self.__usercup,"灌满了",watername)
# p = cup()
# p.setuUserup("保温杯")
# p.setHeight(25)
# p.setCapacity(2500)
# p.setColour("猛男粉")
# p.setTom("不锈钢")
#
# p.tea("龙井")
# p.teamilk("冰雪迷城")
# p.ed("体制能量")
# p.water("怡宝")

class computer:
    __usercomputer:""
    __brand:""
    __model:""
    __display:""
    __cpu:""
    __graphicscard:""
    __amainboard:""
    __runningmemory:""

    def setUsercomputer(self,usercomputer):
        self.__usercomputer = usercomputer
    def setBrand(self,brand):
        self.__brand = brand
    def setModel(self,model):
        self.__model = model
    def setDisplay(self,display):
        self.__display = display
    def setCpu(self,cpu):
        self.__cpu = cpu
    def setGraphicscard(self,graphicscard):
        self.__graphicscard = graphicscard
    def setAmainboard(self,amainborad):
        self.__amainboard = amainborad
    def setRunningmemory(self,runninggmemory):
        self.__runningmemory = runninggmemory

    def play(self,gamename):
        print(self.__usercomputer,"正在玩",gamename)
    def kan(self,tvname):
        print(self.__usercomputer,"正在看",tvname)
    def shopping(self,websitename):
        print(self.__usercomputer,"正在逛",websitename)
    def study(self,hour):
        print(self.__usercomputer,"已经学了",hour,"个小时")
    def showMe(self):
        print("我的",self.__brand,"型号",self.__model,"显示器",self.__display)
p=computer()
p.setUsercomputer("笔记本电脑")
p.setBrand("机械师")
#品牌




p.setModel("F114")
#型号
p.setDisplay(16.5)
#显示屏
p.setCpu("i7 11700k")
#cpu
p.setGraphicscard("GTX 3090ti")
#显卡
p.setAmainboard("华硕Z97-A")
#主板
p.setRunningmemory("32G")
#运行内存

p.play("英雄联盟")
p.kan("你微笑时很美")
p.shopping("淘宝")
p.study(16)
p.showMe()



