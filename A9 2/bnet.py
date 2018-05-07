from BayesianNetwork import BayesianNetwork
from sys import argv

given = False
observations = []
query = []

for _arg in argv:
        if _arg == "given":
                given = True
        query.append(_arg)
        if given:
                observations.append(_arg)

bnet = BayesianNetwork()

if query:
	num = bnet.fit(bnet.get_values(query))
	if observations:
		den = bnet.fit(bnet.get_values(observations))
	else:
		den = 1
	print "The probability is : %.9f" % (num/den)
else:
	print "Invalid query string"
