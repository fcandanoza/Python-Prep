class Modulo_7:

    def __init__(self, listado):
        self.listado = listado
        
    #BLOQUE DE CÓDIGO PARA REVISAR SI CADA ELEMENTO DE LA LISTA ES NÚMERO PRIMO
    #Método para Verificar Números Primos 
    def __numero_primo (self, numero):
        validador = 1
        
        for divisor in range (2, numero):
            if numero % divisor == 0:
                validador = 0
                break
                            
        if validador == 1:
            es_primo = True
        else:
            es_primo = False
        
        if numero == 0 or numero == 1:
            es_primo = False
        return es_primo
    
    # Método para llamar al método privado __numero_primo
    def numero_primo (self):
        for i in self.listado:
            if self.__numero_primo(i):
                print (i, "es número primo")
            else:
                print (i, "no es número primo")


    #BLOQUE DE CÓDIGO PARA OBTENER EL VALOR MODAL
    #Método para valor modal
    def __Valor_Modal (self, lista_numeros):
        elementos_unicos   = list(set(lista_numeros))
        dicc_mas_repetidos = {}

        if len(lista_numeros) == 0:
            print("La lista está vacía")

        for elemento in elementos_unicos:
            dicc_mas_repetidos [elemento] = lista_numeros.count(elemento)
            mas_repetido                  = max(dicc_mas_repetidos, key = dicc_mas_repetidos.get)
            cant_repeticiones             = max(dicc_mas_repetidos.values())

        return (mas_repetido, cant_repeticiones)
    
    #Método para llamar el método privado de valor modal
    def valor_modal(self):
        moda, cant_repeticiones = self.__Valor_Modal(self.listado)
        print ("El valor modal es", moda, "con", cant_repeticiones, "repeticiones")
    

    #BLOQUE DE CÓDIGO PARA HACER CONVERSIONES DE MEDIDAS DE TEMPERATURA
    #Método para conversión grados
    def __conversion_temperatura (self, valor, medida_origen, medida_destino):
   
        if medida_origen == "C" and medida_destino == "F":
            conversion_temp  = (valor * (9/5)) + 32

        elif medida_origen == "C" and medida_destino == "K":
            conversion_temp = valor + 273.15

        elif medida_origen == "F" and medida_destino == "C":
            conversion_temp = (valor - 32) * (5 / 9)

        elif medida_origen == "F" and medida_destino == "K":
            conversion_temp = ((valor - 32) * 5/9) + 273.15

        elif medida_origen == "K" and medida_destino == "C":
            conversion_temp = valor - 273.15

        elif medida_origen == "K" and medida_destino == "F":
            conversion_temp = ((valor - 273.15) * (9/5)) + 32

        elif medida_origen == medida_destino:
            conversion_temp = valor
    
        else:
            return "Los parámetros ingresados no son correctos"

        return conversion_temp
    
    # Método para llamar al método privado __conversion_temperatura
    def conversion_temperatura (self, medida_origen, medida_destino):
        for k in self.listado:
            print (k, "°", medida_origen, "es igual a", self.__conversion_temperatura(k, medida_origen, medida_destino), "°", medida_destino)
    

    #BLOQUE DE CÓDIGO PARA CALCULAR EL FACTORIAL DE CADA ELEMENTO DE LA LISTA
    #Método para calcular el Factorial de un número
    def __factorial (self, numero_fact):
    
        if type(numero_fact) != int:
            return "Debe ingresar un número entero"
        
        if numero_fact > 1:
            fact = numero_fact * self.__factorial (numero_fact - 1)
            return fact
        
        if numero_fact == 1 or numero_fact == 0:
            fact = 1
            return fact
        
        if numero_fact < 0:
            return "Debe ingresar un número entero positivo"
        
    
    # Método para llamar al método privado __factorial
    def factorial (self):
        for j in self.listado:
            factorial_j = self.__factorial(j)
            print ("El factorial de", j, "es", factorial_j)
    