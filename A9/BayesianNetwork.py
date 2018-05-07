class BayesianNetwork(object):

        def compute_probability(self, values):
                return  (self.get_defaults("B",values[0],None,None) * self.get_defaults("E",values[1],None,None) * self.get_defaults("A|B,E",values[2],values[0],values[1]) * self.get_defaults("J|A",values[3],values[2],None) * self.get_defaults("M|A",values[4],values[2],None))

	def get_defaults(self, query, value1, value2, value3):
		if query == "B":
			if value1:
				return 0.001
			else:
				return 0.999
		if query == "E":
			if value1:
				return 0.002
			else:
				return 0.998
		if query == "A|B,E":
			if value2 and value3:
				p_2 = 0.95
			if value2 and not value3:
				p_2 = 0.94
			if not value2 and value3:
				p_2 = 0.29
			if not value2 and not value3:
				p_2 = 0.001
			if value1:
				return p_2
			else:
				return (1-p_2)
		if query == "J|A":
			if value2:
				p_2 = 0.9
			else:
				p_2 = 0.05
			if value1:
				return p_2
			else:
				return (1-p_2)
		if query == "M|A":
			if value2:
				p_2 = 0.7
			else:
				p_2 = 0.01
			if value1:
				return p_2
			else:
				return (1-p_2)

	def fit(self,values):
		if not None in values:
			return self.compute_probability(values)
		else:
			nones = values.index(None)
			next_items = list(values)
			next_items[nones] = True
			val1 = self.fit(next_items)
			next_items[nones] = False
			val2 = self.fit(next_items)
			return val1 + val2

	def get_values(self,values):
		result = []
		if "Bt"	in values:
			result.append(True)
		elif "Bf" in values:
			result.append(False)
		else:
			result.append(None)
		if "Et"	in values:
			result.append(True)
		elif "Ef" in values:
			result.append(False)
		else:
			result.append(None)
		if "At"	in values:
			result.append(True)
		elif "Af" in values:
			result.append(False)
		else:
			result.append(None)
		if "Jt"	in values:
			result.append(True)
		elif "Jf" in values:
			result.append(False)
		else:
			result.append(None)
		if "Mt"	in values:
			result.append(True)
		elif "Mf" in values:
			result.append(False)
		else:
			result.append(None)

		return result
