from classes import *

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
    
