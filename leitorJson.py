import json

def readParameters():
	with open('exemplo.json') as file:
		k = json.load(file)
	return k

def getInJson():	
	pyson = readParameters()
	for i in pyson.keys():
		if i == "root":
			for j in pyson[i]:
				if j == "grupo0":
					print(pyson[i][j]["user0"].keys())
		
getInJson()