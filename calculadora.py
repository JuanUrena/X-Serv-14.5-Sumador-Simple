#!/usr/bin/python3
#Juan Ureña García-Gasco_Calculadora
import sys
# tomar datos desde la ejecucion del programa
from sys import argv
# importa una funcion concreta para no tener que llamarla de sys
# Obtengo los datos desde la linea de comandos

# Compruebo el valor de la operacion para llevarla acabo

def suma(op1,op2):
    return str(op1+op2)
        
def resta(op1,op2):
    return str(op1-op2)

def multi(op1,op2):
    return str(op1*op2)       

def div(op1,op2):
    try:
        return str(op1/op2)
        
    except ZeroDivisionError:
        return("Error: No se puede dividir entre cero")

function ={
   "suma": suma, 
   "resta": resta, 
   "multiplicacion":multi,
   "division": div,
}
    
if __name__ == "__main__":

    try:
        operacion = (argv[1])
        num1 = float((argv[2]))
        num2 = float((argv[3]))
        print(str(funciones[operacion](num1,num2)))
    except IndexError:
        print('Error: La entrada debe ser:')
        exit('python3 calculadora.py <operación> <num1> <num2>')
    except ValueError:
        print('Error: La entrada debe ser:')
        exit('python3 calculadora.py <operación> <num1> <num2>')
    except KeyError:
        print('Operacion no detectada, pruebe con:')
        print('suma, resta, multiplicacion, division')
