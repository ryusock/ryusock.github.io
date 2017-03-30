import geocoder

f = open('sample-estimates.txt')
contents = f.read()
f.close()
newcontents = ""

lines = contents.split("\n")
for l in lines:
	try:
		upperbound = l.index(";")
		address = l[:upperbound]
		g = geocoder.google(address)
		lat = g.latlng[0]
		lng = g.latlng[1]
		newcontents = newcontents + l[:upperbound] + ";" + str(lat) + ";" + str(lng) + l[upperbound:] + "\n"
	except:
		continue

f = open('coordinates.txt', 'w')
f.write(newcontents)
f.close()