from sklearn.feature_extraction.text import CountVectorizer
from nltk import ngrams
import pandas as pd

carpus=['I am a machine learning engineer','I am a data scientist','I am a data engineer']

count_vec=CountVectorizer()
x=count_vec.fit_transform(carpus)

df=pd.DataFrame()
df['voc']=count_vec.get_feature_names()

print(df.head(20))
#________

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = ['Cats have four legs',
          'Cats and dogs are antagonistic',
          'He hate dogs']

tfidf = TfidfVectorizer()
vect = tfidf.fit_transform(corpus)

df = pd.DataFrame()
df['vocabulary'] = tfidf.get_feature_names()
df['sentence1'] = vect.toarray()[0]
df['sentence2'] = vect.toarray()[1]
df['sentence3'] = vect.toarray()[2]

df.set_index('vocabulary', inplace=True)
print(df.T)

#---------
from nltk import ngrams

sentence = 'I like dancing in the rain'

ngram = ngrams(sentence.split(' '), n=2)

for x in ngram:
    print(x)