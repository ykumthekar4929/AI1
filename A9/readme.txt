ASSIGNMENT  9:
NAME: Yashodhan Kumthekar
UTA ID: 1001544391


How to run:
	Task 1:
	python compute_a_posteriori.py <string>
	for example >> python compute_a_posteriori.py CLLCCCLLL
	The output is written to a file called "result.txt" as per the instructions.

	Task 2:
	python bnet.py <query1> <query2> <query3> ... given  <Observation1> <Observation> <Observation>...

	for example >> python bnet.py Jt Af given Bt Ef
	the 'given' argument is optional, its absence will mark all inputs as queries
	for example >> python bnet.py Bt Af Mf Jt Et

    Note: bnet uses a class from BayesianNetwork.py, it is imported in the code.
