# Resolver un sistema de ecuaciones.

import solve_system_ecuations as sse
import numpy as np

# Comienzo del programa principal.
print("\t\tSOLVE SYSTEM ECUATIONS\n")
print("Systems of the form 'Ax = b' by Gauss-Jordan elimination")
print("--------------------------------------------------------\n")
exit = None
while exit != 'q':
    try:
        print("\nEnter 'q' at any time to exit\n")
        
        # Solicita la dimension.
        message ="Enter the dimension for the matrix (n): "
        dimension = sse.get_positive_int(message)
        if dimension == 'q':
            print("\nFinished program")
            exit = 'q'
            continue
        
        # Crea la matriz de coeficientes.
        print("\nEnter the elements for matrix 'A' (Real or Complex)")
        print("Fractions are not accepted")
        print("You can make changes later\n")

        matrix_A = sse.create_matrix_A(dimension)
        if isinstance(matrix_A, str):
                print("\nFinished program")
                exit = 'q'
                continue
        sse.print_matrix_nxn(matrix_A) 
        ctrl_question_0 = input(
            "\nDo you want to change a number? (y/n) ")
        if ctrl_question_0 == 'q':
            print("\nFinished program")
            exit = 'q'
            continue
        elif ctrl_question_0 == 'y':
            while True:
                print("\nEnter A(i, j)")
                message = "Enter i: "
                i = sse.get_positive_int(message)
                message = "Eneter j: "
                j = sse.get_positive_int(message)
                matrix_A = sse.change_number_A(matrix_A, i, j)
                ctrl_question_1 = input(
                    "\nDo you want to change another one? (y/n) ")
                if ctrl_question_1 == 'n':
                    break
                elif ctrl_question_1 == 'q':
                    print("\nFinished program")
                    exit = 'q'
                    continue
            sse.print_matrix_nxn(matrix_A)
        
        # Crea la matriz de terminos independientes.
        print("\nEnter the elements for matrix 'b' (Real or Complex)")
        print("Fractions are not accepted")
        print("You can make changes later\n")

        matrix_b = sse.create_matrix_b(dimension)
        if isinstance(matrix_b, str):
                print("\nFinished program")
                exit = 'q'
                continue
        sse.print_matrix_nx1(matrix_b) 
        ctrl_question_0 = input(
            "\nDo you want to change a number? (y/n) ")
        if ctrl_question_0 == 'q':
            print("\nFinished program")
            exit = 'q'
            continue
        elif ctrl_question_0 == 'y':
            while True:
                print("\nEnter b(i, 1)")
                message = "Enter i: "
                i = sse.get_positive_int(message)
                sse.change_number_b(matrix_b, i)
                ctrl_question_1 = input(
                    "\nDo you want to change another one? (y/n) ")
                if ctrl_question_1 == 'n':
                    break
                elif ctrl_question_1 == 'q':
                    print("\nFinished program")
                    exit = 'q'
                    continue
            sse.print_matrix_nx1(matrix_b)

        # Resuelve el sistema.
        result = np.linalg.solve(matrix_A, matrix_b)
        sse.print_matrix_nx1_results(result)
        if sse.has_complex_element(result):
            polar_result = sse.rect_to_polar(result)
            sse.print_matrix_nx1_results(polar_result)
        
        # Pregunta si se quiere limpiar la consola.
        ctrl_question_0 = input(
            "\nDo you want to clean the console? (y/n) ")
        if ctrl_question_0 == 'y':
            sse.clean_console()
            
    except IndexError:
        print("\nYou cannot change an element that does not exist")
    except np.linalg.LinAlgError:
        print("\nSingular Matrix.")