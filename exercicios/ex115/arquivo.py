from interface import titulo
from exercicios.geral.dados import leiaInt

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Ocorreu um erro ao ler o arquivo!')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f' {dado[0]:<39}{f"{dado[1]} anos":<8}')
    finally:
        a.close()


def cadastrar(arquivo):
    titulo('NOVO CADASTRO')
    nome = str(input('Nome: ')).strip().title()
    idade = leiaInt('Idade: ')
    if nome == str():
        nome = 'desconhecida'
    if idade == int():
        idade = 0
    try:
        a = open(arquivo, 'at')
    except:
        print('Ocorreu um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um erro ao escrever os dados no arquivo!')
        else:
            print(f'Registro de {nome} adicionado ao {arquivo}'.replace('.txt', ''))
            a.close()
