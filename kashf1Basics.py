import re

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

print(len(text))
list_of_words = re.findall(r'\w+', text) 
print(len(list_of_words))

kashf.close()