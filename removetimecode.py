import xml.etree.ElementTree as ET

file = "dummytestfile_copy.xml"
tree = ET.parse(file)
root = tree.getroot()
#y = ET.tostring(root, encoding='utf8').decode('utf8')
finalfile = "fixedfile.xml"
out = open("out.xml", "w")
#newfile = ""

#This program  is a training test that removes
#all dialogue from a subtitle file and returns it 
#as a .txt file with each sub separated.
#For my training purposes, much junk is left in it
#that I was trying out, and I want to look over them again later.
#so apologies for the mssy code and a few unused items
#that are still in it.

#print(root[1].tag)

body = root[1]
record = body[0]
textrows = record[0]
actualevent = textrows[0]
#note it can have two children, so actualevent isn't fixed, but don't need it right now

#subtitletext = root[1]

#print(record.tag)

# filetext = ""
# for child in body:
#     eventext = ""
#     for child in textrows:
#         eventext += child.text + "\n"
#     filetext += eventext + "\n"

filetext = ""
for child in body:
    #eventext = ""
    #eventext += child[0].text + "\n"
    for child in child[0]:
        filetext += str(child.text) + "\n"
    filetext += "\n"


# filetext = ""
# for child in body:
#     print(child[0][0].tag)


print(filetext)

with open("out.txt", "w") as out:
    out.write(filetext)
#y = ET.tostring(filetext, encoding='utf8').decode('utf8')

#these three work, but are encoding the entire OLD xml
#y = ET.tostring(root, encoding='utf8').decode('utf8')
#out.write(y)
#out.close()

#tree.write(out)
#for timeIn in record.iter('timeIn'):
 #   record.timeIn == ""
