
f=open("day7_part1.txt","r")#abrir el documento y guardar linea a linea en una lista.
#f=open("day7_part1_test.txt","r")
lista=f.readlines()


#make something that can read trough the input and get the information
#we only need the pair of letters.

alphabet=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
for n in range(len(lista)):	
	lista[n]=lista[n][5:6]+lista[n][36:37]



for n in range(len(lista)):

	lista[n]=alphabet.index(lista[n][0])+1 , alphabet.index(lista[n][1])+1
	

	




#deal with ordering normaly
	#goes through list and saves information about the letters that are not before.
	
list2=[]
list3=[]
list4=[]
for n in range(len(lista)):
	list2.append(lista[n][0])

for n in range(1,27):
	if n not in list2:
		list3.append(n)

list4.append(list3[0])
print(list2)
print(list4)
list2.remove(list4[0]) #no hay que borrarlo de aqui si no de la segunda columna.






	#orders alfabetically




