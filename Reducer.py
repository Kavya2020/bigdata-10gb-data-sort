import sys

curKey = None
keyWords = []

for line in sys.stdin:
	line = line.strip()
	try:
		key,word = line.split("\t")
		if key!=curKey:
			for w in sorted(keyWords):
				print "{0}{1}".format(curKey,w)
			curKey = key
			keyWords = []
		keyWords.append(word)
	except:
		Pass

if curKey!=None:
	for w in sorted(keyWords):
		print "{0}{1}".format(curKey,w)
	keyWords = []
