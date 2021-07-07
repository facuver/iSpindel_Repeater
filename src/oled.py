from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
from cfg import iSpindels 
import cfg

class Screen():

    def __init__(self,i2c,width = 128,height = 64):
        self.i2c =i2c
        self.oled_width = width
        self.oled_height = height
        self.oled = SSD1306_I2C(self.oled_width, self.oled_height, i2c)   
        self.oled.contrast(0)

    def update(self,iSpindel):

        self.oled.fill(0)
        self.oled.show()
       
        self.oled.text(iSpindel["name"],0,0)
        self.oled.text("B:{:.2f}V  G:{:.3f}".format(iSpindel["battery"],iSpindel["gravity"] ),0,12 )
        self.oled.text("T:{:.1f}C    R:{}".format(iSpindel["temperature"], iSpindel["RSSI"]),0,24 )
        self.oled.text("A:{:.1f}  ".format(iSpindel["angle"]),0,36 )
        self.oled.text("IP:{}".format(cfg.ip),0,48 )

        self.oled.show()
        

    def print_msg(self,msg):
        self.oled.fill(0)
        msg = msg.split("\n")
        for line , text in enumerate(msg):
            self.oled.text(text,0,(line*12))

        self.oled.show()


i2c = I2C(0,sda=Pin(19),scl=Pin(18))

screen = Screen(i2c)

