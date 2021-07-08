def notas(*provas, sit=False):
    """
        Função para analisar notas e a situação da turma.
    :param provas: uma ou mais notas dos alunos.
    :param sit: Indicação se deve mostrar a situação da turma.
    :return: Um dicionário com as notas, média e a situação (caso seja solicitado) da turma.
    """
    d = dict()
    d['quantidade'] = len(provas)
    d['maior'] = max(provas)
    d['menor'] = min(provas)
    d['média'] = sum(provas)/d['quantidade']
    if sit:
        if d['média'] >= 7:
            d['situação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


resp = notas(3.5, 5.5, 6, 5.5, 5, 2, sit=True)
print(resp)
resp = notas(10, 5.5)
print(resp)
help(notas)
