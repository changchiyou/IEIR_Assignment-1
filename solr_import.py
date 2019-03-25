import pandas as pd
import pysolr

QA_Pair_list = []

df = pd.read_csv('novel_data.csv',encoding='utf_8_sig',index_col=0)
df_size = df.shape[0]

QA_Pair = {}
QA_Pair['id'] = 0
QA_Pair['question'] = 'Hello , how are you ?'
QA_Pair['answer'] = 'I am fine, and you?'
QA_Pair_list.append(QA_Pair)

for i in range(df_size):
    print('Pairing',i,':',df.loc[i,'title'])
    
    QA_Pair = {}
    QA_Pair['id'] = i*2+1
    QA_Pair['question'] = df.loc[i,'title'] + ' 網址 是什麼'
    QA_Pair['answer'] = df.loc[i,'link']
    QA_Pair_list.append(QA_Pair)
    
    QA_Pair = {}
    QA_Pair['id'] = i*2+2
    QA_Pair['question'] = df.loc[i,'title'] + ' 作者 是誰'
    QA_Pair['answer'] = df.loc[i,'author']
    QA_Pair_list.append(QA_Pair)


# Define the target solr collection
solr = pysolr.Solr('http://127.0.0.1:8983/solr/Assignment1', timeout=60)

# Import all data in QA_Pair_list
solr.add(QA_Pair_list)