inventory = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

print(max([sum([int(j) for j in i.split('\n') if j != '']) for i in inventory.split('\n\n')]))

print(sum(sorted([sum([int(j) for j in i.split('\n') if j != '']) for i in inventory.split('\n\n')], reverse=True)[:3]))
