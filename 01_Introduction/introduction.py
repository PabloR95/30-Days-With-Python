# Introduction
# Day 1 - 30 days of python challenge ----- Guía practica que te llevara desde lo básico hasta un nivel avanzado en el uso de Python.

# Arithmetic operators 

print(10 + 5)  # addiction(+)
print(8 - 4)   # subtracrion(-)
print(9 * 6)   # multiplication(*)
print(5 * 8)   # division (/)
print(8 ** 2)  # exponential (**) spanish: potenciación
print(5 % 3)   # modulus (%)      spanish: modulo(residuo)
print(8 // 4)  # floor division operator (//) spanish: division que muestra parte entera

# Checking data types  ---- Revisar tipos de datos

print(type(10))                             #Int ------ Entero
print(type(4.80))                           #Float ---- Décimal
print(type(1 + 9j))                         #Comlex ----Complejo 
print(type("Exponential"))                  #String
print(type([1, 2, 3, 4]))                   #List
print(type((1, 2, 3, 4,)))                  #Tuple
print(type({"name" : "Pablo", "edad" : 30}))#Dictionary 
print(type({3.65, 2.14, 6.6}))              #Set
print(type(8==8))                           #Bool
print(type(8>=8))                           #Bool   
print(type(range(8)))                       #Range
print(type(b"Hello"))                       #Bytes
print(type(memoryview(bytes(6))))           #Memoryview
print(type(None))                           #NoneType

# If you want to specify the data type, you can use the following constructor functions------- Si quieres especificar el tipo de dato, puedes usar las siguientes funciones 
variable = str("Hello World")
print(variable)

variable = int(65)
print(variable)

variable = float(85.65)
print(variable)

variable = complex(3 + 5j)
print(variable)

variable = list = ["apple", "cherry", "tomato"]   # list[]
print(variable)

variable = tuple(("apple", "cherry", "tomato"))   #Tuple()
print(variable)
