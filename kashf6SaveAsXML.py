import re
import xml.etree.ElementTree as ET

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

denoised_text = re.sub(r'\.{2,}', '', text)
elementsKashf = denoised_text.split(".")

kashfalzunun = ET.Element("kashf")
for x in range(0, len(elementsKashf)-1):
	WordsElement = re.findall(r'\w+',elementsKashf[x])
	numberWordsElement = len(WordsElement)
	
	entryNew = ET.SubElement(kashfalzunun, "entry")
	entryID = ET.SubElement(entryNew, "ID")
	entryID.text = str(x+1)
	entryLength = ET.SubElement(entryNew, "Length")
	entryLength.text = str(numberWordsElement)
	entryText = ET.SubElement(entryNew, "Text")
	entryText.text = elementsKashf[x]
ET.ElementTree(kashfalzunun).write("kashfalzunun.xml")

kashf.close()