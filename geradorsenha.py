import random
import string
import re
import hashlib

print(" ____ _            ")
print("/ ___| ___ _ __ __ _ __| | ___ _ __")
print("| | _ / _ \ '__/ _` |/ _`| / _ \| '__|")
print("| |_| | __/ | | (_| | (_||  (_) | |   ")
print("\____|\___|_| \__,_|\__,_| \___/|_|  \n")



print("..%%%%...%%%%%%..%%..%%..%%..%%...%%%%....%%%%..")
print(".%%......%%......%%%.%%..%%..%%..%%..%%..%%.....")
print("..%%%%...%%%%....%%.%%%..%%%%%%..%%%%%%...%%%%..")
print(".....%%..%%......%%..%%..%%..%%..%%..%%......%%.")
print("..%%%%...%%%%%%..%%..%%..%%..%%..%%..%%...%%%%..")
print("................................................\n")


def gerar_senha(tamanho, letras, numeros, simbolos):
    """
    Gera uma senha aleatória com base nas preferências do usuário.
    """
    caracteres = ''
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if caracteres:
        return ''.join(random.choice(caracteres) for i in range(tamanho))
    else:
        return 'Você deve selecionar pelo menos um tipo de Caractere.'

def hash_senha(senha):
    """
    Cria um hash SHA-256 da senha.
    """
    sha256 = hashlib.sha256()
    sha256.update(senha.encode('utf8'))
    return sha256.hexdigest()

def main():
    """
    Função principal que solicita as preferências do usuário, gera a senha e salva no arquivo.
    """
    tamanho = int(input('Digite o tamanho da senha: '))
    letras = input('Deseja Incluir Letras? (s/n) ').lower() == 's'
    numeros = input('Deseja incluir números? (s/n) ').lower() == 's'
    simbolos = input('Deseja Incluir síbolos? (s/n) ').lower() == 's'
    quantidade = int(input('Quantas senhas você deseja gerar? '))

    with open('senha.txt', 'w') as f:
        for i in range(quantidade):
            senha = gerar_senha(tamanho, letras, numeros, simbolos)
            while not (re.search(r'.{8,}', senha) and re.search(r'[A-Z]', senha) and re.search(r'\d', senha) and re.search(r'[!@#$%¨&*]', senha)):
                print(" A senha não atende aos critérios de força. Tente Novamente.")
                senha = gerar_senha(tamanho, letras, numeros, simbolos)
            senha_hashed = hash_senha(senha)
            f.write(f'Senha {i+1}: {senha} (Hash: {senha_hashed})\n')

    print(f"As {quantidade} Senhas foram salvas no arquivo 'senhas.txt'.")

if __name__ == "__main__":
    main()
