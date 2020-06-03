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