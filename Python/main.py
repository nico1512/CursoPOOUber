from car import Car

if __name__ == "__main__":
    print("Hola mundo")
    car = Car()
    car.licence = "AMS244"
    car.driver = "Juan Assa"
    print(vars(car))
    
    car2 = Car()
    car2.licence = "ABB200"
    car2.driver = "Mocho"
    print(vars(car2))