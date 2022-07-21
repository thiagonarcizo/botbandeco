# -*- coding: utf-8 -*-

from base64 import encode
from sys import displayhook
import requests
import os
import pandas as pd
import numpy as np


vgm_url = 'https://www.sar.unicamp.br/RU/view/site/cardapio.php'

try: 
    html_text = requests.get(vgm_url).text
except:
    print('Erro ao conectar ao site')
    quit()

df_html = pd.read_html(html_text)

for i, table in enumerate(df_html):
    table.to_csv('data{}.csv'.format(i),'a')



lunch = open('data2.csv', 'r', encoding='utf-8')

df_lunch = pd.read_csv(lunch, sep='\t')
df_lunch['a0'] = df_lunch['a0'].str[2:]
try:
    df_lunch = df_lunch.drop(df_lunch.index[7])
    df_lunch.to_csv('almoco.csv', index=False)
    np.savetxt(r'almoco.txt', df_lunch.values, fmt='%s', encoding='utf-8')
    lunch.close()
except:
    naoRegistro = open('almoco.txt', 'w', encoding='utf-8')
    naoRegistro.write('Sem almoço cadastrado!')
    lunch.close()
    naoRegistro.close()




lunch_v = open('data3.csv', 'r', encoding='utf-8')

df_lunch_v = pd.read_csv(lunch_v, sep='\t')
df_lunch_v['a0'] = df_lunch_v['a0'].str[2:]
try:
    df_lunch_v = df_lunch_v.drop(df_lunch_v.index[7])
    df_lunch_v.to_csv('almoco_v.csv', index=False)
    np.savetxt(r'almoco_v.txt', df_lunch_v.values, fmt='%s', encoding='utf-8')
    lunch_v.close()
except:
    naoRegistro = open('almoco_v.txt', 'w', encoding='utf-8')
    naoRegistro.write('Sem almoço vegetariano cadastrado!')
    lunch_v.close()
    naoRegistro.close()



dinner = open('data4.csv', 'r', encoding='utf-8')

df_dinner = pd.read_csv(dinner, sep='\t')
df_dinner['a0'] = df_dinner['a0'].str[2:]
try:
    df_dinner = df_dinner.drop(df_dinner.index[7])
    df_dinner.to_csv('dinner.csv', index=False)
    np.savetxt(r'janta.txt', df_dinner.values, fmt='%s', encoding='utf-8')
    dinner.close()
except:
    naoRegistro = open('janta.txt', 'w', encoding='utf-8')
    naoRegistro.write('Sem janta cadastrada!')
    dinner.close()
    naoRegistro.close()



dinner_v = open('data5.csv', 'r', encoding='utf-8')

df_dinner_v = pd.read_csv(dinner_v, sep='\t')
df_dinner_v['a0'] = df_dinner_v['a0'].str[2:]
try:
    df_dinner_v = df_dinner_v.drop(df_dinner_v.index[7])
    df_dinner_v.to_csv('dinner_v.csv', index=False)
    np.savetxt(r'janta_v.txt', df_dinner_v.values, fmt='%s', encoding='utf-8')
    dinner_v.close()
except:
    naoRegistro = open('janta_v.txt', 'w', encoding='utf-8')
    naoRegistro.write('Sem janta vegetariana cadastrada!')
    dinner_v.close()
    naoRegistro.close()

for i in range(0,6):
    os.remove('data{}.csv'.format(i))

try:
    os.remove('almoco.csv')
    os.remove('almoco_v.csv')
    os.remove('dinner.csv')
    os.remove('dinner_v.csv')
except:
    print('Não foi possível remover os arquivos')