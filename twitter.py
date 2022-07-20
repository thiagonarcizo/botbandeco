from os import access
import tweepy
from datetime import date

#Salva o dia de hoje formatado:
hoje = date.today()
data_em_texto = hoje.strftime('%d/%m/%Y')

#Abre os arquivos de autenticação e salva em variáveis:
api_key_file = open('api_key.txt', 'r', encoding='utf-8')
api_key = api_key_file.read()
api_key_file.close()

api_key_secret_file = open('api_key_secret.txt', 'r', encoding='utf-8')
api_secret_key = api_key_secret_file.read()
api_key_secret_file.close()

access_token_file = open('access_token.txt', 'r', encoding='utf-8')
access_token = access_token_file.read()
access_token_file.close()

access_token_secret_file = open('access_token_secret.txt', 'r', encoding='utf-8')
access_token_secret = access_token_secret_file.read()
access_token_secret_file.close()

#Autenticação do Twitter:
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Executa o arquivo main.py
exec(open("main.py").read())

#Lê cada arquivo que contém o seu respectivo cardápio:
text_lunch = open('almoco.txt', 'r', encoding='utf-8')
text_lunch_r = text_lunch.read()
text_lunch.close()

text_lunch_v = open('almoco_v.txt', 'r', encoding='utf-8')
text_lunch_v_r = text_lunch_v.read()
text_lunch_v.close()

text_dinner = open('janta.txt', 'r', encoding='utf-8')
text_dinner_r = text_dinner.read()
text_dinner.close()

text_dinner_v = open('janta_v.txt', 'r', encoding='utf-8')
text_dinner_v_r = text_dinner_v.read()
text_dinner_v.close()


#Escreve o texto de cada Tweet:
almoco = 'Bandeco de hoje ('+data_em_texto+'):\n\nAlmoço:\n\n'+text_lunch_r

almoco_v = 'Almoço Vegetariano:\n\n'+text_lunch_v_r

janta = 'Janta:\n\n'+text_dinner_r

janta_v = 'Janta Vegetariana:\n\n'+text_dinner_v_r




#Tweeting:
original_tweet = api.update_status(status=almoco)

reply1_tweet = api.update_status(status=almoco_v, 
                                 in_reply_to_status_id=original_tweet.id, 
                                 auto_populate_reply_metadata=True)

reply2_tweet = api.update_status(status=janta, 
                                 in_reply_to_status_id=reply1_tweet.id, 
                                 auto_populate_reply_metadata=True)

reply3_tweet = api.update_status(status=janta_v, 
                                 in_reply_to_status_id=reply2_tweet.id, 
                                 auto_populate_reply_metadata=True)