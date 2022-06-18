def notas(*n, sit=False):
    """
    ==> Função para analizar notas e situações de vários alunos.
    :param n: Uma ou mais notas do aluno (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    media = (sum(n)) / len(n)
    pessoa = {}
    pessoa['total'] = len(n)
    pessoa['maior'] = max(n)
    pessoa['menor'] = min(n)
    pessoa['media'] = media
    if sit is True:
        if media < 5:
            pessoa['situação'] = ('RUIM')
        if 5 <= media < 7:
            pessoa['situação'] = ('RAZOÁVEL')
        if media >= 7:
            pessoa['situação'] = ('BOA')
    return pessoa


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)