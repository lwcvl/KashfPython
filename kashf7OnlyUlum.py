import re
import xml.etree.ElementTree as ET

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

denoised_text = re.sub(r'\.{2,}', '', text)
elementsKashf = denoised_text.split(".")

kashfalzunun = ET.Element("kashf")
y = 1
for x in range(0, len(elementsKashf)-1):
	WordsElement = re.findall(r'\w+',elementsKashf[x])
	numberWordsElement = len(WordsElement)
	if WordsElement[0] =="علم":
		entryNew = ET.SubElement(kashfalzunun, "entry")
		entryNumber = ET.SubElement(entryNew, "Number")
		entryNumber.text = str(y)
		entryID = ET.SubElement(entryNew, "ID")
		entryID.text = str(x)
		entryLength = ET.SubElement(entryNew, "Length")
		entryLength.text = str(numberWordsElement)
		entryText = ET.SubElement(entryNew, "Text")
		entryText.text = elementsKashf[x]
		y = y+1
ET.ElementTree(kashfalzunun).write("kashfOnlyUlum.xml")

kashf.close()