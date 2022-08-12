# Trabalho Pratico 1 - Jogo Domino
# Disciplina: Paradigmas de Linguagem de Programacao
# Instituto de Computacao - IComp
# Universidade Federal do Amazonas - UFAM
# Autores: Lukas Takatani - 21204522 - lekt@icomp.ufam.edu.br
# 	   Arthur Melo - 21550189 - avgm@icomp.ufam.edu.br
# Professor Avaliador: Professor Dr. Ruiter B. Caldas

# Programa utilizando Python3, para execução digite no terminal "python3 domino.py" 

pedrasimg = u'🀱🀲🀳🀴🀵🀶🀷' +             u'🀸🀹🀺🀻🀼🀽🀾' +              u'🀿🁀🁁🁂🁃🁄🁅' +              u'🁆🁇🁈🁉🁊🁋🁌' +              u'🁍🁎🁏🁐🁑🁒🁓' +              u'🁔🁕🁖🁗🁘🁙🁚' +              u'🁛🁜🁝🁞🁟🁠🁡' +              u'🁣🁤🁥🁦🁧🁨🁩' +              u'🁪🁫🁬🁭🁮🁯🁰' +              u'🁱🁲🁳🁴🁵🁶🁷' +              u'🁸🁹🁺🁻🁼🁽🁾' +              u'🁿🂀🂁🂂🂃🂄🂅' +              u'🂆🂇🂈🂉🂊🂋🂌' +              u'🂍🂎🂏🂐🂑🂒🂓'

# Função para desenhar a pedra.
def pedrades(pedra):
    orientacao = 0 if pedra[0] != pedra[1] else 1
    i = ((orientacao*49) + 7*pedra[0] + pedra[1])
    return pedrasimg[i:i+1]

# Função para desenhar a mão.
def maodes(mao, orientacao = 1):
    if orientacao == 1:
        return ' '.join([pedrades(p) for p in mao])
    else:
        return ' '.join([pedrades(invertida(mao[-i])) for i in range(1, len(mao)+1)])+' '

invertida = lambda pedra: (pedra[1], pedra[0])

# Domino Python Funcional - Exercícios:
# Defina funções para obter a primeira pedra,
prim = lambda mesa: mesa[0]
def primpedra (mesa):
    print (pedrades(prim(mesa)))


# e cada uma das listas de pedras jogadas ao norte,
# leste, sul e oeste da primeira pedra (braços)
cima = lambda mesa: mesa[1]
def norte (mesa):
    print (maodes(cima(mesa)))

dir = lambda mesa: mesa[2]
def leste (mesa):
    print (maodes(dir(mesa)))

baixo = lambda mesa: mesa[3]
def sul (mesa):
    print (maodes(baixo(mesa)))

esq = lambda mesa: mesa[4]
def oeste (mesa):
    print (maodes(esq(mesa)))

carrocas = lambda mao: len([p for p in mao if p[0]==p[1]])

# Função para desenhar a mesa.
def mesades(mesa):
    espacos = int(1.7 * len(esq(mesa)) - 0.8 * carrocas(esq(mesa)))
    linha1 = '' if len(cima(mesa)) == 0 else espacos * ' ' + maodes(cima(mesa)) + '\n'
    linha2 = maodes(esq(mesa), 0) + pedrades(prim(mesa)) + maodes(dir(mesa))
    linha3 = '' if len(baixo(mesa)) == 0 else '\n' + espacos * ' ' + maodes(baixo(mesa))
    return linha1 + linha2 + linha3

# Defina uma função para retornar a pedra na ponta de um braço.
pont = lambda braco: None if len(braco) == 0 else braco[-1]
def ponta (braco):
    print (pedrades(pont(braco)))

# Defina uma função para retornar as pedras nas pontas dos braços.
pontas = lambda mesa: [pont(braco) for braco in mesa[1:] if braco]
def todas_pontas(mesa):
    ptas = pontas(mesa)
    return [prim(mesa)] + ptas if len(ptas) == 1 else ptas

# Defina uma função que calcule o total de pontos de uma configuração
valorp = lambda pedra: pedra[0]+pedra[1] if pedra[0]==pedra[1] else pedra[1]
def pontos_domino(mesa):
    ptos = sum([valorp(p) for p in todas_pontas(mesa)])
    return ptos if ptos % 5 == 0 else 0


# Configuração da Mesa.
mesa0 = [(6,6),
        [(6,2), (2,5), (5,5)],
        [(6,3), (4,3), (3,2), (2,1), (1,1), (1,4), (4,0), (0,3)],
        [(6,1), (1,3), (3,3), (3,4)],
        [(6,5), (5,4), (4,4)]]

print ("\nMesa:")
print (mesades(mesa0))

print ("\nPrimeira pedra, Norte, Leste, Sul e Oeste:")
primpedra(mesa0)
norte(mesa0)
leste(mesa0)
sul(mesa0)
oeste(mesa0)

print ("\nPonta Norte e Sul:")
ponta(cima(mesa0))
ponta(baixo(mesa0))

print ("\nTodas as pontas:")
print(maodes(todas_pontas(mesa0)))

print ("\nTotal de pontos da mesa:")
print (pontos_domino(mesa0))
