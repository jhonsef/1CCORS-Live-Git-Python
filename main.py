import random
from withmath.basics import somar, subtrair, multiplicar, dividir

def main():
  x = random.randint(1, 100)
  y = random.randint(1, 100)
  print(f"Valores: x = {x}, y = {y}\n")
  print(f"Soma: {somar(x, y)}")
  print(f"Subtração: {subtrair(x, y)}")
  print(f"Multiplicação: {multiplicar(x, y)}")
  print(f"Divisão: {dividir(x, y)}")

if __name__ == "__main__":
  main()
