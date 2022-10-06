from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")
    
    car = Car("AMS244", Account("Juan Assa", "34122"))
    print(vars(car))
    print(vars(car.driver))