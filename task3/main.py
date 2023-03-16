with open("../task2/tokens.txt", encoding='utf-8') as file_token:
  tokens = file_token.read().splitlines()
index = {i: [] for i in tokens}
for i in range(1, 101):
  step = str(i)
  with open("../task1/" + step + ".html", 'r', encoding='utf-8') as file:
    website_html = file.read()
    website_html.lower()
    for item in tokens:
      if item in website_html:
        arr = index.get(item)
        arr.append(i)
        index.update({item: arr})
with open("inverted_index.txt", "w", encoding='utf-8') as file:
  for key, value in index.items():
    file.write('%s:%s\n' % (key, value))

print("Inverted index complete")


