def get_grades():
    while True:
        try:
            grades_input=input("Ingrese una lista de calificaciones separadas por comas: ")

            grades_list=grades_input.split(',')

            grades = [int(grade.strip()) for grade in grades_list]

            print("Las calificaciones ingresadas son:", grades)
            break
        
        except ValueError:
            print("Error: Por favor ingrese solo números enteros separados por comas. ")
            
get_grades()