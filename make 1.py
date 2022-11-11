from collections import Counter

c = Counter(['apple','banana','apple','coke','banana','banana'])

print('apple',c['apple'])
print('banana',c['banana'])
print('coke',c['coke'])