def get_fuel_percentage():
    while True:
        try:
            fraction=input("Ingrese una fracción (X/Y): ")
            X,Y= fraction.split('/')

            X=int(X)
            Y=int(Y)

            if X > Y or Y == 0:
                raise ValueError
            
            percentage= (X/Y) * 100

            if percentage < 1:
                print("E")
            elif percentage > 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break

        except ValueError:
            print("Error: Por favor ingrese una fracción válida con números entero y asegúrese que X sea <= Y.")
        except ZeroDivisionError:
            print(" Error: No se puede dividir entre cero, intente nuevamente")

get_fuel_percentage()