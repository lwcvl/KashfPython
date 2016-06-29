import re
import xml.etree.ElementTree as ET

kashf = open('KashfAlZunun.txt', mode='r', encoding='utf-8')
text = kashf.read()

elementsKashf = text.split(".")

print(len(elementsKashf))

kashf.close()