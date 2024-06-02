class Car:
    
    def __init__(self, color, speed = 0):  #모든 클래스에 소속된 첫번쨰 인자들은 반드시 self이다. #현재 나를 호출한 게 누군지를 알려주는 키워드. 다른 언어에서 this와 같다.
        self.color = color #멤버 변수 initialization. 멤버 변수, 멤버 메서드든 모두 self가 붙는다.
        self.speed = speed
    def speedUp(self):
        self.speed += 10
    def speedDown(self):
        self.speed -= 10
    def __str__(self):
        return 'Color = %s : Speed = %s' %(self.color, self.speed)
    def __eq__(self, carB) :
        return "yes" if self.color == carB.color else "no"


if __name__ == '__main__' :
    car1 = Car('Black', 0)
    car2 = Car('Red', 120)
    car3 = Car('Yellow')

    print(car1.color)
    print(car1.speed)
    car1.speedUp()
    print(car1.speed)

    print(car1 == car2)
    print(car1 == car3)

