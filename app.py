def sumar(a, b):
    return a + b

def restar(a, b):
    # Error intencional: se suma en lugar de restar
    return a + b

if __name__ == "__main__":
    print(f"Resultado de la suma 2 + 3: {sumar(2, 3)}")
