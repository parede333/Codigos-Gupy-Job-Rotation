# -*- coding: utf-8 -*-
"""
Criado por Willian Wagner de Brito Coura

Resolução do problema para o test de Job Rotatio - São Paulo
------------------------------------------------------------------------------------------
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
------------------------------------------------------------------------------------------
"""

import json

with open('dados.json') as f:
    lista = json.load(f)
    
lista2 = []
lista3 = []
x = 0
contador = 0

for i in lista:
    if i['valor'] != 0.0:
        x += i['valor'] 
        contador += 1
        lista3.append(i['valor'])
    lista2.append(i['valor'])
    
media_mensal = x / contador
print(30*'---')
print('Menor valor de faturamento ocorrido em um dia',min(lista2), 'reais')
print('Maior valor de faturamento ocorrido em um dia',max(lista2), 'reais')
print(30*'---')
contador2 = 0
for i in lista3:
    if i > media_mensal:
        contador2 += 1 
print(f'{contador2} dias em que o faturamento diario foi maior que o mensal.')
