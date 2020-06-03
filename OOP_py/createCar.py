class Car: #Основной классс машины
    speed = '220ml/h'
    model = 'Mercedes'
    color = 'Green'
    def createCar(self):
        print('Создана машина:\n' + 'Модель - ' + self.model + '\nЦвет - ' + self.color + '\nСкорость - ' + self.speed)
    def __del__(self):
        print('_' + self.speed + self.model, self.color, "удален из памяти")

class miniCar(Car): #Дочерний класс машины
    carType = 'mini'        
    def createCar(self):
        print('Создана машина мини:\n' + 'Модель - ' + self.model + '\nЦвет - ' + self.color + '\nСкорость - ' + self.speed + '\nТип - ' + self.carType)
    def __del__(self):
        print('_' + self.speed, self.model,  self.color, self.carType, "удален из памяти")

def showInfoCar(point): #Функция
    if point == 1:
        car = Car()
        car.createCar()
    elif point == 2:
        carMini = miniCar()
        carMini.color = 'black'
        carMini.speed = '120ml/h'
        carMini.model = 'BMW'
        carMini.createCar()
    elif point == 3:
        exit()
    else:
        print('Некорректный пункт меню\n' + '_______________________')        

if __name__ == "__main__":
    while True:
        print('Выберите пункт:\n' + '1. Создать машину\n' + '2. Создать маленькую машину\n' + '3. Выход')
        pointMenu = int(input('Введите номер пункта: '))
        showInfoCar(pointMenu)
    
