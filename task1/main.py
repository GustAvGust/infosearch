import requests
import bs4
import re

response = requests.get(f"https://8500.ru/cat/site.html")

tree = bs4.BeautifulSoup(response.text, 'html.parser')

result = re.findall(
    r"/cat/site-.[a-z]*.html", str(tree)
)

list_of_sites = list(map(lambda x: "https://8500.ru" + x, result))
count = 0
site_list = []
for item in list_of_sites:
    response = requests.get(item)
    tree = bs4.BeautifulSoup(response.text, 'html.parser')
    result = re.finditer(
        r"https?://(www.)?[a-z\-1-9]*\.(ru|com|org|info)", str(tree.find('style'))
    )
    for site in result:
        if count == 100:
            break
        try:
            response_local = requests.get(site.group(0))
            if response_local.status_code == 200:
                count += 1
                tree_local = bs4.BeautifulSoup(response_local.text, 'html.parser')
                name = str(count) + ".html"
                site_list.append(name + ": " + str(site.group(0)))
                with open(name, "w", encoding = 'utf-8') as file:
                    file.write(str(tree_local))
        except: pass
with open("index.txt", "w", encoding='utf-8') as file:
    file.write("\n".join(site_list))
