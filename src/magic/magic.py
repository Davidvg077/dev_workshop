import math


class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        a, b = 0,1
        for _ in range(n):
            a, b = b, a + b
        return a     
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        fibonacci = [0,1]

        for i in range(2,n):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

        if n == 1:
            return [0]

        return fibonacci[:n]    
            
        
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True    

    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos        
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1:
            return False
        suma_divisores = 0
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                suma_divisores += i 
        return suma_divisores == n        
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        pascal = [[1]]

        for i in range(1,filas):
            fila = [1]
            for j in range (1,i):
                fila.append(pascal[i-1][j-1]+pascal[i-1][j])
            fila.append(1)
            pascal.append(fila)

        return pascal        
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n == 0 or n == 1:
            return 1 
        else:
            return n * self.factorial(n-1)
        
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b != 0:
            a, b = b , a % b
        return a   
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        def mcd(a,b):
            while b != 0:
                a , b = b , a % b
            return a 
        return abs(a*b)// mcd(a,b)
        
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(digit)for digit in str(n))
    
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        num_str = str(n)
        num_digits = len(num_str)
        suma = sum(int(digit) ** num_digits for digit in num_str)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        for fila in matriz:
            if sum(fila) != suma_referencia:
                return False
            
        for col in range(n):
            if sum(matriz[fila][col]for fila in range(n)) != suma_referencia:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_referencia:
            return False

        if sum(matriz[i][n - 1 -i] for i in range(n)) != suma_referencia:
            return False

        return True        