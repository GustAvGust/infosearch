with open("inverted_index.txt", encoding='utf-8') as file_token:
  tokens = file_token.read().splitlines()
index = {}
for item in tokens:
    ex1 = item.split(":")
    li = []
    kr = ex1[1].replace('[', '')
    kr = kr.replace(']', '')
    spl = kr.split(", ")
    name = ex1[0]
    index[name] = spl
while(True):
  print('Enter command: NOT <word> | <word1> [OR|AND] <word2>')
  qr = str(input()).split(" ")
  full = [str(i) for i in range(1, 101)]
  if qr[0] == "NOT":
      res = [x for x in full if x not in index.get(qr[1])]
      print(res)
  else:
      word1 = index.get(qr[0])
      word2 = index.get(qr[2])
      if qr[1] == "OR":
        print(word1 or word2)
        res = list(set(word1).union(set(word2)))
        print(res)
      elif qr[1] == "AND":
        res = list(set(word1).intersection(set(word2)))
        print(res)