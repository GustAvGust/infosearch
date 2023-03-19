import collections
import math

inverted_index_count = {}
tokens_dictionary = {}

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

def compute_idf(word, count, dictionary):
    return math.log10(len(dictionary)/count[word])

with open("../task3/inverted_index.txt", encoding='utf-8') as file_token:
    tokens = file_token.read().splitlines()

for item in tokens:
    ex1 = item.split(":")
    li = []
    kr = ex1[1].replace('[', '')
    kr = kr.replace(']', '')
    spl = kr.split(", ")
    name = ex1[0]
    inverted_index_count[name] = len(spl)

for i in range(1, 101):
    step = str(i)
    with open("../task2/tokens" + step + ".txt", 'r') as f:
      data = f.read()
      data_list = data.splitlines()
      tokens_dictionary[step] = data_list

for key, value in tokens_dictionary.items():
    tf_idf_dictionary = {}
    computed_tf = compute_tf(value)
    
    for word in computed_tf:
        idf = compute_idf(word, inverted_index_count, tokens_dictionary)
        tf_idf_dictionary[word] = [idf, computed_tf[word] * idf]
    
    with open('../task4/token_' + key + '_tf_idf.txt', 'w') as f:
        for key1, value1 in tf_idf_dictionary.items():
            result_string = key1 + " " + str(value1[0]) + " " + str(value1[1])
            f.write("%s\n" % result_string)

# ==========================================
        
lemma_dictionary = {}

for i in range(1, 101):
    step = str(i)
    with open("../task2/lemmas" + step + ".txt", 'r') as fp:
        data = fp.read()
        data_list = data.splitlines()
        lemma_dictionary[step] = data_list
        
for key, value in tokens_dictionary.items():
    tf_idf_dictionary = {}
    computed_tf = compute_tf(value)
    curerent_lemmas = lemma_dictionary[key]
    
    for lemma in curerent_lemmas:
        values = lemma.split(' ')
        tf_lemma_sum = float(0)
        idf_sum = float(0)
        
        for i in range(1,len(values)):
            tf_lemma_sum += computed_tf[values[i]]
            idf_sum += compute_idf(values[i], inverted_index_count, lemma_dictionary)
        
        tf_idf_dictionary[values[0].replace(":", "")] = [idf_sum, tf_lemma_sum * idf_sum]
    
    with open('../task4/lemma_' + key + '_tf_idf.txt', 'w') as f:
        for key1, value1 in tf_idf_dictionary.items():
            result_string = key1 + " " + str(value1[0]) + " " + str(value1[1])
            f.write("%s\n" % result_string) 