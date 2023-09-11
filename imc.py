def calcular_imc(peso, altura):
    altura_metros = altura / 100 
    imc = peso / (altura_metros ** 2)
    return imc
def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.99:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em cm): "))
imc = calcular_imc(peso, altura)
interpretação = interpretar_imc(imc)
print(f"Seu IMC é: {imc:.2f}")
print(f"Interpretação: {interpretação}")

