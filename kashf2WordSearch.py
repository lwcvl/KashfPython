import re

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

def word_counter (search_word):
	findNumberOfWord = re.findall(search_word, text)
	print(len(findNumberOfWord))

word_counter("شرح")

kashf.close()