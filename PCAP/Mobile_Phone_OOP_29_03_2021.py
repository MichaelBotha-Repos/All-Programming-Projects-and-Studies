class Mobile:
    def __init__(self, number):
        self.number = number 
    def turn_on(self):
        print("mobile phone",self.number,"is turned on")
    def turn_off(self):
        print("mobile phone is turned on")
    def call(self, num):
        #self.num = num
        print("calling",num)

samsung = Mobile("0794755845")
nokia = Mobile("0832606429")

samsung.turn_on()
nokia.turn_on()
nokia.call("0726413101")
samsung.turn_off()
nokia.turn_off()

