import math
from sympy import diff, symbols, sympify, lambdify,exp
from math import sqrt



def funcao():
    f_str = input("Digite a função: ")
    return f_str



def calcular_phi():
    phi = (1 + math.sqrt(5)) / 2
    return phi



def regula_falsi(func, intervaloA, intervaloB, pres1, pres2, it):
    raiz = 0
    k = 0


    if abs(func(intervaloA)) < pres2 or abs(func(intervaloB)) < pres2 or abs(intervaloA - intervaloB) < pres1:
        raiz = intervaloA
        return raiz
    else:
        M = func(intervaloA)

        x1 = (intervaloA * func(intervaloB) - intervaloB * func(intervaloA)) / (func(intervaloB) - func(intervaloA))

        while abs(func(x1)) > pres2 and k < it and abs(intervaloB - intervaloA) > pres1:
            k += 1

            if M * func(x1) > 0:
                intervaloA = x1
            else:
                intervaloB = x1

            M = func(intervaloA)
            x1 = (intervaloA * func(intervaloB) - intervaloB * func(intervaloA)) / (func(intervaloB) - func(intervaloA))

        raiz = x1

    return raiz

def bissecao(func, a, b, s, m):
    k = 0
    finicio = 0
    meio = 0
    fmeio = 0
    
    if abs(b - a) > s:
        while abs(b - a) > s and k < m:
            finicio = func(b)
            meio = (a + b) / 2
            fmeio = func(meio)
            
            if finicio * fmeio < 0:
                b = meio
            else:
                a = meio
            k += 1
            
        return meio
    else:
        return a
    
    
def mil(x0, s, it):
    raiz = 0
    x1 = 0
    k = 0

    if abs(func(x0)) < s:
        raiz = x0
        k += 1
    else:
        x1 = calcular_phi(x0)
        while abs(func(x1)) > s and abs(x0 - x1) > s and k < it:
            x0 = x1  
            x1 = calcular_phi(x0)
            k += 1
        raiz = x1

    return raiz

def newton(func,x0, s, max_iter, it):
    x = symbols('x')

    # Criar uma função numérica a partir da expressão original
    f = lambdify(x, func)

    # Derivar simbolicamente a expressão
    func_deriv = diff(func, x)

    # Criar uma função numérica a partir da derivada
    func_deriv_num = lambdify(x, func_deriv)
    
    k = 0
    fx = f(x0)

    if abs(fx) > s:
        fxlinha = func_deriv_num(x0)
        
        x1 = x0 - (fx / fxlinha)
        fx = f(x1)

        while abs(fx) > s and abs(x1) - abs(x1 - x0) > s and k < max_iter:
            k += 1
            x0 = x1
            fxlinha =  func_deriv_num(x0)
            x1 = x0 - (fx / fxlinha)
            fx = f(x1)

        return x1
    else:
        return x0

def MetodoSecante(func, x0, x1, prec, it):
    k = 1

    if abs(func(x0)) < prec:
        return x0
    elif abs(func(x1)) < prec and abs(x1 - x0) < prec:
        return x1
    else:
        while abs(func(x1)) > prec and abs(x1 - x0) > prec and k < it:
            x2 = x1
            print(f"x1: {x1}, x2: {x2}")
            x1 = x1 - ((func(x1) * (x1 - x0)) / (func(x1) - func(x0)))
            x0 = x2
            print(f"x0: {x0}, x1: {x1}, x2: {x2}")
            k += 1
        
        return x1


def switch(numero, func):
    if numero == 1:
        intervaloA = float(input("Digite o intervalo A: "))
        intervaloB = float(input("Digite o intervalo B: "))
        pres1 = float(input("Digite a precisão 1: "))
        pres2 = float(input("Digite a precisão 2: "))
        it = int(input("Digite o número de interações: "))

        resultado = regula_falsi(func, intervaloA, intervaloB, pres1, pres2, it)
        print(f"Resultado: {resultado}")

        return resultado
    else:
        if numero == 2: 
            a = float(input("Digite Intervalo A :"))
            b = float(input("Digite Intervalo B: "))
            s = float(input("Digite a precisão s:  "))
            m = float(input("Digite a precisão m : "))
        
            resultado = bissecao(func, a, b, s, m)
        
            print(f"Resultado: {resultado}")

            return resultado
        else:
            if numero == 3: 
                
                x0 = float(input("Digite x0"))
                s = float(input("Digite press "))
                it = float(input("Digite iterão"))
                
                resultado = mil(func,x0,s,it)
                print(f"Resultado: {resultado}")
            else:
                if numero == 4:
                    
                    x0 = 1.0  # Aproximação inicial
                    s = 1e-6  # Precisão
                    max_iter = 100 
                    it = 30
                 
                   # x0 = float(input("Digite x0"))
                    #s = float(input("Digite press"))
                    #max_iter = float(input("Digite iterações"))
                    #it = float(input("interações it"))
                    resultado = newton(expr,x0, s, max_iter, it)
                    print(f"Resultado: {resultado}")
                else:
                    if numero == 5:
                        
                     x0 = float(input("Digite x0"))
                     s = float(input("Digite press"))
                     max_iter = int(input("Digite s"))
                     it =  int(input("Digite it"))
                    
                    resultado = MetodoSecante(func,x0, s, max_iter, it)
                    print(f"Resultado: {resultado}")
                        
                        
                         
if __name__ == "__main__":
    
        x = symbols('x')

       

      #  equation = funcao()


       # expr = sympify(equation)


        #func = lambdify(x, expr)
        equation_str = "exp(x) - 4*x^2"
        expr = sympify(equation_str)  # Converte a string para uma expressão simbólica
        func = lambdify(x, expr)  # Cria uma função numérica a partir da expressão simbólica
        
                    
        numero = int(input("Digite o numero: "))

        resultado = switch(numero, func)




