# -*- coding: utf-8 -*-
"""
Criado por Willian Wagner de Brito Coura

Resolução do problema para o test de Job Rotatio - São Paulo
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
------------------------------------------------------------------------------------------
"""
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'outros': 19849.53
    }
j = 0
for x in faturamento_mensal.values():
    j += x
percentual = []
for x in faturamento_mensal.values():
    y = (100*x)/j
    percentual.append(y)

print(f'''
      O percentual de SP foi {percentual[0]} %
      O percentual de RJ foi {percentual[1]} %
      O percentual de MG foi {percentual[2]} %
      O percentual de ES foi {percentual[3]} %
      O percentual dos outros estados foram {percentual[4]} %
      ''')