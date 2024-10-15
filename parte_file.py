fil = open('pandaS.txt', 'r')

datos = fil.readlines()

del1 = 500
nl = len(datos)

np1 = int(nl/del1)

pref = 'pandas'

k = 0

for i in range(np1):
  namefil = pref + str(i) + '.txt'
  fil = open(namefil, 'w')
  for j in range(del1):
    fil.write(datos[k])
    k = k+1
  fil.close()

namefil = pref + str(np1) + '.txt'
fil = open(namefil, 'w')
for j in range(k, nl):
  fil.write(datos[j])
fil.close()



