from numpy import dot
from numpy.linalg import norm

lemma_dict = {}
lemma_doc_list = {}

with open("../task2/lemmas.txt", 'r', encoding='utf-8') as fp:
    data = fp.read()
    data_list = data.splitlines()
    for item in data_list:
        lemma_dict.update({item.split(':')[0]: 0.0})

for i in range(1, 101):
    step = str(i)
    with open("../task4/lemma_" + step + "_tf_idf.txt", 'r', encoding='utf-8') as fp:
        data = fp.read()
        dict_copy = lemma_dict.copy()
        data_list = data.splitlines()
        for item in data_list:
            dict_copy.update({item.split(' ')[0]: float(item.split(' ')[2])})
        lemma_doc_list.update({step: dict_copy})

while True:

    qr = str(input())
    qr_split = qr.split(' ')
    qr_dict = lemma_dict.copy()
    for item in qr_split:
        qr_dict.update({item: 1.0})
    sim_list = {}
    for i in range(1,101):
        list_of_qr_values = list(qr_dict.values())
        normed_list_of_qr_values = norm(list_of_qr_values)
        list_of_dict_values = list(lemma_doc_list.get(str(i)).values())
        normed_list_of_dict_values = norm(list_of_dict_values)
        dotted = dot(list_of_qr_values, list_of_dict_values)
        result = dotted / (normed_list_of_qr_values * normed_list_of_dict_values)
        sim_list.update({i: result})
    sorted_res = dict(sorted(sim_list.items(), key=lambda x: x[1], reverse=True))
    print(list(sorted_res.keys()))
