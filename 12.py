
f=open("6.txt","r")#abrir el documento y guardar linea a linea en una lista.
#f=open("6prueba.txt","r")
lista=f.readlines()

#separar coordenadas x y 
for n in range(len(lista)):
	lista[n]=lista[n].split(", ")
	lista[n][0]=int(lista[n][0])
	lista[n][1]=int(lista[n][1])


def mandis(a,b):
	a[0]=(a[0])
	a[1]=(a[1])
	b[0]=(b[0])
	b[1]=(b[1])
	result=abs(a[0]-b[0])+abs(a[1]-b[1])
	return result

	

#ordenar los valores. No creo que haga falta pero asi luego no te rompes la cabeza tanto.
#Averiguar coordenadas máximas
xmax=0
for element in lista:
	if element[0]>xmax:
		xmax=element[0]
		
xmin=1000000
for element in lista:
	if element[0]<xmin:
		xmin=element[0]


ymax=0
for element in lista:
	if element[1]>ymax:
		ymax=element[1]
		
ymin=1000000
for element in lista:
	if element[1]<ymin:
		ymin=element[1]

#localizar coordenadas exteriores e interiores
#esquinas
abajoizq=(xmax,ymax)
abajoder=(xmin,ymax)
arribaizq=(xmax,ymin)
arribader=(xmin,ymin)

for n in range(len(lista)):
	if lista[n][0]<abajoizq[0] and lista[n][1]<abajoizq[1]:
		abajoizq=lista[n]

	if lista[n][0]>abajoder[0] and lista[n][1]<abajoder[1]:
		abajoder=lista[n]

	if lista[n][0]<arribaizq[0] and lista[n][1]>arribaizq[1]:
		arribaizq=lista[n]

	if lista[n][0]>arribader[0] and lista[n][1]>arribader[1]:
		arribader=lista[n]


#print("Esquinas",abajoizq,abajoder,arribaizq,arribader)

#lados
listalados=[abajoizq,abajoder,arribaizq,arribader]

for n in range(len(lista)):

	if lista[n][1]<=ymin and lista[n] not in listalados:

		listalados.append(lista[n])

	if lista[n][1]>=ymax and lista[n] not in listalados:

		listalados.append(lista[n])

	if lista[n][0]<=xmin and lista[n] not in listalados:

		listalados.append(lista[n])

	if lista[n][0]>=xmax and lista[n] not in listalados:

		listalados.append(lista[n])
		
#print("Contorno",listalados)

a=[0,0]

contador=0
contador2=0
indice=0
empate=False
listaresul=[0]*len(lista)

for x in range(xmax):
	
	for y in range(ymax):
		
		for n in range(len(lista)):
			a=[x,y]
			contador+=mandis(a,lista[n])
			
		if contador<10000:
			contador2+=1
			
		contador=0
print(contador2)
			
			
		
		










