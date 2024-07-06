# Solve a system of ecuations.

import os
import re
import numpy as np
from tabulate import tabulate

def get_number(number):
    """Obtains a number, of type int, float or complex."""
    invalid_menssage = "The value is not an int, float or complex"
    try:
        number = int(number)
    except ValueError:
        try:
            number = float(number)
        except ValueError:
            try:
                number = complex(number)
            except (ValueError, SystemError):
                if number == 'q':
                    return number
                else:
                    print(invalid_menssage)
                    number = 'invalid number'
                return number
    return number

def create_matrix_A(dimension):
    """Create an nxn matrix coefficients"""
    matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            number_str = input(f"Enter A({i+1}, {j+1}): ")
            number_str = re.sub(r'\s', '', number_str)
            number = get_number(number_str)
            if number == 'invalid number':
                while number == 'invalid number':
                    number_str = input(f"Enter A({i+1}, {j+1}): ")
                    number_str = re.sub(r'\s', '', number_str)
                    number = get_number(number_str)
            elif number == 'q':
                return 'q'
            row.append(number)
        matrix.append(row)
    return np.array(matrix)

def create_matrix_b(dimension):
    """Create an nx1 matrix independent terms"""
    independent_terms = []
    for i in range(dimension):
        number_str = input(f"Enter b({i+1}, 1): ")
        number_str = re.sub(r'\s', '', number_str)
        number = get_number(number_str)
        if number == 'invalid number':
            while number == 'invalid number':
                number_str = input(f"Enter b({i+1}, 1): ")
                number_str = re.sub(r'\s', '', number_str)
                number = get_number(number_str)
        elif number == 'q':
            return
        independent_terms.append(number)
    return np.array(independent_terms)

def change_number_A(matrix, i, j):
    number_str = input(f"Enter A({i}, {j}): ")
    number_str = re.sub(r'\s', '', number_str)
    number = get_number(number_str)
    while number == 'invalid number':
        number_str = input(f"Enter A({i}, 1): ")
        number_str = re.sub(r'\s', '', number_str)
        number = get_number(number_str)
    if isinstance(number, complex):
        matrix = matrix.astype(complex)
    i -= 1
    j -= 1
    matrix[i,j] =  number
    return matrix

def change_number_b(matrix, i):
    number_str = input(f"Enter b({i}, 1): ")
    number_str = re.sub(r'\s', '', number_str)
    number = get_number(number_str)
    while number == 'invalid number':
        number_str = input(f"Enter b({i}, 1): ")
        number_str = re.sub(r'\s', '', number_str)
        number = get_number(number_str)
    if isinstance(number, complex):
        matrix = matrix.astype(complex)
    i -= 1
    matrix[i] =  number
    return matrix

def clean_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('cls')
    
def get_positive_int(message):
    while True:
        number = input(message)
        if number == 'q':
            return number
        try:
            number = abs(int(number))
            return number
        except ValueError:
            print("The entry must be an integer.")
            continue

def print_matrix_nxn(matrix):
    # Inicializa una lista vacía para almacenar la matriz formateada
    matrix_str = []
    # Recorre cada fila en la matriz original
    for row in matrix:
        # Inicializa una lista vacía para almacenar la fila formateada
        formatted_row = []
        # Recorre cada elemento en la fila actual
        for cell in row:
            # Verifica si el elemento es de tipo float o complex
            if isinstance(cell, (float, complex)):
                formatted_cell = f'{cell:.2f}'  # Formatea con dos decimales
            else:
                formatted_cell = str(cell)  # Convierte en cadena
            formatted_row.append(formatted_cell)  # Agrega el elemento formateado a la fila
        matrix_str.append(formatted_row)  # Agrega la fila formateada a la matriz resultante
    # Genera la tabla formateada usando tabulate
    table = tabulate(matrix_str, tablefmt='fancy_grid', numalign="center")
    print(f"\n{table}")

def print_matrix_nx1(matrix):
    # Inicializa una lista vacía para almacenar la matriz formateada
    matrix_str = []
    # Recorre la matriz unidimensional y crea una lista de listas con un solo elemento en cada fila
    for number in matrix:
        formatted_row = [f'{number:.2f}']
        matrix_str.append(formatted_row)
    # Genera la tabla formateada usando tabulate
    table = tabulate(matrix_str, tablefmt='fancy_grid', numalign="center")
    print(f"\n{table}")

def print_matrix_nx1_results(matrix):
    # Inicializa una lista vacía para almacenar la matriz formateada
    matrix_str = []

    def has_any_string(matrix):
        # Usa numpy.vectorize para aplicar isinstance a cada elemento de la matriz
        is_string = np.vectorize(lambda x: isinstance(x, str))(matrix)
        # Usa numpy.any para verificar si al menos un elemento es True (es una cadena de texto)
        return np.any(is_string)
    
    # Recorre la matriz unidimensional y crea una lista de listas con un solo elemento en cada fila
    for number in matrix:
        if has_any_string(matrix):
            formatted_row = [f'{number}']
        else:
            formatted_row = [f'{number:.6f}']
        matrix_str.append(formatted_row)
    # Genera la tabla formateada usando tabulate
    table = tabulate(matrix_str, tablefmt='fancy_grid', numalign="center")
    print(f"\n{table}")

def rect_to_polar(matrix):
    # Convierte los números complejos a forma polar
    angles = np.angle(matrix)
    magnitudes = np.abs(matrix)
    # También crea una matriz de cadenas de texto que representan los números en forma polar
    complex_numbers_polar_str = np.array([f"{mag:.2f}∠{angle:.2f}°" for mag, angle in zip(magnitudes.flatten(), np.degrees(angles).flatten())])
    complex_numbers_polar_str = complex_numbers_polar_str.reshape(matrix.shape)
    return complex_numbers_polar_str

def has_complex_element(arr):
    # Verifica si al menos un elemento es complejo
    is_complex = np.iscomplex(arr)
    return np.any(is_complex)