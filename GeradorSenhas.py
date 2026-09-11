import random

def gerar_senha(tamanho):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Gerador de Senhas")
print("Digite o tamanho da senha desejada:")
tamanho = int(input())
senha = gerar_senha(tamanho)
print("Senha gerada:", senha)