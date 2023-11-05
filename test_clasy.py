class LightSwitch():    # definicja klasy
    def __init__(self):
        self.switchIsOn = False
    def turnOn(self):
        self.switchIsOn = True
        #print ('turn on')
    def turnOff(self):
        self.switchIsOn = False
    def show(self):
        print(self.switchIsOn)

oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

oLightSwitch1.show()
oLightSwitch2.show()

oLightSwitch1.turnOn()
oLightSwitch2.turnOff()

oLightSwitch1.show()
oLightSwitch2.show()

oLightSwitch1.turnOff()
oLightSwitch2.turnOn()

oLightSwitch1.show()
oLightSwitch2.show()


