from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
import pymystem3
from pymystem3 import Mystem
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')
# nltk.download("stopwords")

official_words_ru = stopwords.words('russian')
official_words_en = stopwords.words('english')

m = Mystem()

def not_official_words(word):
  return not(word in official_words_en or word in official_words_ru)

def add_word_to_lemma(word, lemma):
  if not(lemma in lemmas.keys()):
    lemmas[lemma] = set()
  lemmas[lemma].add(word)

for i in range(1, 101):
  lemmas = {}
  step = str(i)
  print("Processing" + step)
  with open("../task1/" + step + ".html", 'r', encoding='utf-8') as file:
    website_html = file.read()

  tree = BeautifulSoup(website_html, 'html.parser')

  for data in tree(['style', 'script', 'head', 'title', 'meta', '[document]']):
      data.decompose()

  full_text = ' '.join(tree.stripped_strings)

  full_text = re.sub("[^a-zA-Zа-яА-Я]+", ' ', full_text)
  uniq_clean_words = list(set(filter(not_official_words, full_text.lower().split(' '))))

  print(len(uniq_clean_words))
  for word in uniq_clean_words:
    if word == '':
      continue
    if re.match("[a-zA-Z]", word):
      lemma = WordNetLemmatizer().lemmatize(word)
    else:
      lemma = m.lemmatize(word)[0]
    
    add_word_to_lemma(word, lemma)

  with open("lemmas" + step + ".txt", "w", encoding='utf-8') as file:
    for el in lemmas:
      file.write(el + ": " + " ".join(lemmas[el]) + "\n")
  # print(lemmas)

  tokens = []
  for el in lemmas.values():
    tokens = tokens + list(el)

  with open("tokens" + step + ".txt", "w", encoding='utf-8') as file:
    file.write("\n".join(tokens))
  # print(tokens)