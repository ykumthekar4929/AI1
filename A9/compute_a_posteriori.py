from sys import argv
if len(argv) > 1:
	obs_str = argv[1]
else:
	obs_str = ""

res_file = open("result.txt", 'w+')
res_file.write("Observation Sequence Q: %s\n" % obs_str)
res_file.write("Length of Q: %i\n" % len(obs_str))
obs_str = obs_str.upper().strip()
obs_str = obs_str +"C"

po_hypos = [{
                                'h1':0.1,
                                'h2':0.2,
                                'h3':0.4,
                                'h4':0.2,
                                'h5':0.1
                        }]
prioris = {
			'C|h1': 1,
                        'L|h1': 0,
			'C|h2': 0.75,
                        'L|h2': 0.25,
			'C|h3': 0.5,
                        'L|h3': 0.5,
			'C|h4': 0.25,
                        'L|h4': 0.75,
			'C|h5': 0,
                        'L|h5': 1
		}

po_queries = []
init_prob = 0

for key in po_hypos[0]:
        curr_value = (prioris[obs_str[0] +'|' +key] * po_hypos[0][key])
        init_prob += curr_value

po_queries.append({obs_str[0]:init_prob})

for j in range(0,len(obs_str)-1):
	if len(po_hypos) -1 < j:
		po_hypos.append({})
	if len(po_queries) -1 < j:
		po_queries.append({})
	curr_val = 0
	for key in po_hypos[0]:
		po_hypos[j][key] = prioris[obs_str[j]+'|'+key] * po_hypos[j-1][key] / po_queries[j-1][obs_str[j]]
		curr_val += prioris[obs_str[j+1]+'|'+key] * po_hypos[j][key]
	po_queries[j][obs_str[j+1]] = curr_val

keys_list = po_hypos[-1].keys()
keys_list = sorted(keys_list)
for key in keys_list:
        res_file.write('P(%s|Q) = %.5f\n'%(key, round(po_hypos[-1][key], 5)))
p_next_C = po_queries[-1]["C"]
res_file.write( "Probability that the next candy we pick will be C, given Q: %.5f\n" % round(p_next_C, 5) )
res_file.write( "Probability that the next candy we pick will be L, given Q: %.5f\n" % round(1.000-p_next_C, 5))
res_file.close()
