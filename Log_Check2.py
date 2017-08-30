#Script to check logfiles for WINPE+OOBE matching SN's, and add good items to list
import codecs
winpe = []
oobe = []
left = []
#Attatch corresponding log items to correct list
with codecs.open('C:\\Users\\Admin\\Desktop\\Project.txt', 'r', 'utf-16') as log:
	lines = log.read().splitlines()
for line in lines:
	if "WINPE" in line:
		winpe.append(line)
	if "OOBE" in line:
		oobe.append(line)
#If service tag is in both, attach it to a list and save
for x in winpe:
	if any(x[:7] in y for y in lines):
		if any(x[:7] in y for y in oobe):
			left.append(x[:24])
output = open('c:\Test.txt', 'r+')
for item in left:
	output.write(item+'\n')
print(left)
#Check for leftover items
for x in lines:
	if not any(x[:7] in y for y in oobe):
		print(x)
for x in lines:
	if not any(y[:7] in y for y in winpe):
		print(x)