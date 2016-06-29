import re
import xml.etree.ElementTree as ET

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

denoised_text = re.sub(r'\.{2,}', '', text)
elementsKashf = denoised_text.split(".")

f = open("KashfActualLengthEntries.txt","w")

for x in range(0, len(elementsKashf)):
	numberWordsElement = re.findall(r'\w+',elementsKashf[x])
	f.write(str(len(numberWordsElement))+"\n")
    
f.close()
kashf.close()