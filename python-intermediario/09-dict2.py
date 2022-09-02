perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'resposta': {
            'a':'1',
            'b':'2',
            'c':'3',
            'd':'4',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 0+1',
        'resposta': {
            'a':'1',
            'b':'2',
            'c':'3',
            'd':'4',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+1',
        'resposta': {
            'a':'1',
            'b':'2',
            'c':'3',
            'd':'4',
        },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}] : {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('EEHHHHHH!!!! Você acertou!!!!')
        respostas_certas += 1 
    else:
        print('IXIIII!!! Você ERROOOUUU')

    qtd_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas / qtd_perguntas * 100
    print(f'Você acertou {respostas_certas} perguntas')
    print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
    print()