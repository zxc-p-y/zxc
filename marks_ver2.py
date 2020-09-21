print('1) внести оценки из журнала')
print('2) показать оценки по предмету')
print('3) показать весь журнал')
print('4) показать плановые оценки')

listOfObjects = ['alg.txt', 'chem.txt', 'eng.txt', 'geom.txt', 'inf.txt', 'pe.txt','rus.txt',
				 'bio.txt', 'de.txt', 'geog.txt', 'hist.txt', 'lit.txt', 'phis.txt', 'sos.txt']

listOfObjectsToShow = ['алгебра', 'химия', 'английский', 'геометрия', 'информатика', 'физ-ра', 'русский', 
					   'биология', 'немецкий', 'география', 'история', 'литература', 'физика', 'обществознание',]

planedMarkForIObj = [5, 4, 5, 5, 5, 5, 5,
					 4, 5, 4, 4, 5, 4, 4,]

def enterMarks(x):
	obj = open(listOfObjects[x], 'a')
	print(listOfObjectsToShow[x])
	obj.write(str(input()))
	obj.close()
def showJournal(numOfObj):
	fileWithMarks = (open(listOfObjects[numOfObj], 'r'))
	listOfMarks = list(fileWithMarks.read()) #читаем оценки из файла и запихиваем их в listOfMarks
	
	print(listOfObjectsToShow[numOfObj] + ' ', end = '')#В начало строки пишем название предмета

	for x in range(len(listOfMarks)):
		print(listOfMarks[int(x)], end=' ')# печатаем все оценки

	sumOfMarks = 0
	for x in range(len(listOfMarks)):
		sumOfMarks+=int(listOfMarks[x])#считаем сумму оценок
	try:
		print('средний бал: ' + str(sumOfMarks/len(listOfMarks)) + ' ', end='')#пытаемся показать средний бал
	except ZeroDivisionError:
		print('средний бал неопределен')

	try:
	 	print('отклонение от плана: ' + str(sumOfMarks/len(listOfMarks)-planedMarkForIObj[numOfObj]))#в одну строку
		# считаем и печатаем разницу между планируемым балом по предмету x и текущем
	except ZeroDivisionError:
		pass

ask = int(input())

if ask == 1:#внести новые данные о предметах
	for x in range(14):
		enterMarks(x)

if ask == 2:#показать ситуацию по одному отдельному предмету
	for x in range(14):
		print(str(x+1) + ' ' + listOfObjectsToShow[x])
	showJournal(int(input('по какому именно?'))-1)

if ask == 3:#показать ситуацию по каждому предмету
	for x in range(14):
		showJournal(x)

if ask == 4:#Показать плановые оценки
	for x in range(14):
		print(listOfObjectsToShow[x] + ' ' + str(planedMarkForIObj[x]))