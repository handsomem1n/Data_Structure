from Car import Car

class SuperCar(Car) :
    def __init__(self, color, speed=0, bool터보 = True):
        super().__init__(color, speed) #부모 클래스를 상속받은 자식 클래스를 생성하고 싶을때, 부모 클래스의 생성없이는 생성할 수 없다. 따라서, 부모 클래스의 생성자를 직접 호출하여 부모 클래스를 먼저 만듦.
        self.bool터보 = bool터보
    
    def set터보(self, bool터보) : 
        self.bool터보 = bool터보
    
    #method overriding
    def speedUp(self) :
        if self.bool터보 : # if 불터보일 때
            self.speed += 50
        else :
            super().speedUp() # = (self.speed += 10)

if __name__ == "__main__":
    SC1 = SuperCar("gold", 0)
    SC2 = SuperCar("white", 0, false)

    SC1.speedUp()
    SC2.speedUp()

    print(s1)
    print(s2)