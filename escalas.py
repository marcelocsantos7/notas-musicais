NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0,2,4,5,7,9,11)}


def escalas(tonica, tonalidade):
    """
    {
        'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    }
    """
    intervalos = ESCALAS[tonalidade]
    posicao_tonica = NOTAS.index(tonica)
    temp = []

    for intervalo in intervalos:
        nota = (posicao_tonica + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}  


print(escalas('A', 'maior'))