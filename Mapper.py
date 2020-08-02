import sys
for line in sys.stdin:
	line = line.strip()
	words = [line[:9],line[9:]]
	print "{0}.{1}".format(words[0],words[1])
