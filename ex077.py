from unidecode import unidecode
palavras = 'abóbora', 'vaca', 'crochê', 'constituição', 'macarrão', 'limonada', 'estudante', 'professor'

for p in palavras:
    vogais = ''
    for letra in p:
        # Tira o acento da letra caso esteja acentuada
        letraSemAcento = unidecode(letra.lower())
        if letraSemAcento in 'aeiou':
            vogais += ' ' + letraSemAcento
    print(f'Na palavra {p.upper()} temos {vogais}')
