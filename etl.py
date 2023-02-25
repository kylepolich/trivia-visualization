import json

f = open('data.txt', 'r')
s = f.read()
f.close()

result = {
	"nodes": [],
	"edges": []
}

nodes = set()
nmap = {}
c = 1
i = s.find('\n') + 1
s = s[i:]
for row in s.split('\n'):
	arr = row.split('\t')
	if len(arr) == 3:
		n1 = arr[0]
		n2 = arr[1]
		if n1 not in nodes:
			nodes.add(n1)
			nmap[n1] = c
			c += 1
		if n2 not in nodes:
			nodes.add(n2)
			nmap[n2] = c
			c += 1
		e = {
			'source': nmap[n1],
			'target': nmap[n2],
			'caption': arr[2]
		}
		result['edges'].append(e)

for node in nodes:
	n = {
		'id': nmap[node],
		'label': node
	}
	result['nodes'].append(n)

json.dump(result, open('team.json', 'w'), indent=4)
