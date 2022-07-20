from sys import displayhook
import requests
import os
import pandas as pd
import numpy as np


vgm_url = 'https://www.sar.unicamp.br/RU/view/site/cardapio.php'

element = """<span class="titulo_cardapio">Almoço</span>"""

try: 
    #file = open("cardapio.html", "r", encoding='utf-8')
    #html_text = file.read()
    #file.close()
    html_text = requests.get(vgm_url).text
except:
    print('Erro ao conectar ao site')
    quit()

df_html = pd.read_html(html_text)

for i, table in enumerate(df_html):
    table.to_csv('data{}.csv'.format(i),'a')



lunch = open('data2.csv', 'r', encoding='utf-8')

df_lunch = pd.read_csv(lunch)
df_lunch['a0'] = df_lunch['a0'].str[2:]
df_lunch = df_lunch.drop(df_lunch.index[7])
df_lunch.to_csv('almoco.csv', index=False)
np.savetxt(r'almoco.txt', df_lunch.values, fmt='%s', encoding='utf-8')
lunch.close()


lunch_v = open('data3.csv', 'r', encoding='utf-8')

df_lunch = pd.read_csv(lunch_v)
df_lunch['a0'] = df_lunch['a0'].str[2:]
df_lunch = df_lunch.drop(df_lunch.index[7])
df_lunch.to_csv('almoco_v.csv', index=False)
np.savetxt(r'almoco_v.txt', df_lunch.values, fmt='%s', encoding='utf-8')
lunch_v.close()

dinner = open('data4.csv', 'r', encoding='utf-8')

df_lunch = pd.read_csv(dinner)
df_lunch['a0'] = df_lunch['a0'].str[2:]
df_lunch = df_lunch.drop(df_lunch.index[7])
df_lunch.to_csv('dinner.csv', index=False)
np.savetxt(r'janta.txt', df_lunch.values, fmt='%s', encoding='utf-8')
dinner.close()

dinner_v = open('data5.csv', 'r', encoding='utf-8')
df_lunch = pd.read_csv(dinner_v)
df_lunch['a0'] = df_lunch['a0'].str[2:]
df_lunch = df_lunch.drop(df_lunch.index[7])
df_lunch.to_csv('dinner_v.csv', index=False)
np.savetxt(r'janta_v.txt', df_lunch.values, fmt='%s', encoding='utf-8')
dinner_v.close()

for i in range(0,6):
    os.remove('data{}.csv'.format(i))