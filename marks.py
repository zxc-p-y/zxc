import random

while True:
	print('1) внести оценки из журнала')
	print('2) текущее положение относительно плана')
	print('3) показать оценки по предмету')
	print('4) показать весь журнал')
	print('5) показать плановые оценки')
	print('6) комментарий президента о моих оценках')
	listOfObjects = ['alg.txt', 'chem.txt',\
					 'eng.txt', 'geom.txt', \
					 'inf.txt', 'pe.txt',\
					 'rus.txt', 'bio.txt', \
					 'de.txt', 'geog.txt', \
					 'hist.txt', 'lit.txt', \
					 'phis.txt', 'sos.txt']
	listOfObjectsToShow = ['алгебра', 'химия',\
						   'английский', 'геометрия',\
						   'информатика', 'физ-ра',\
						   'русский', 'биология',\
						   'немецкий', 'география',\
						   'история', 'литература',\
						   'физика', 'обществознание',]
	planedMarkForIObj = ['5', '4', \
						 '5', '5', \
						 '5', '5', \
						 '5', '4', \
						 '5', '4', \
						 '4', '5', \
						 '4', '4',]
	def divisionTwoInts(a, b, type):
		try:
			a/b
		except ZeroDivisionError:
			return 'ZeroDivisionError'
		else:
			if type == 'int':
				return int(a/b)
			elif type == 'str':
				return str(a/b)
			elif type == 'float':
				return float(a/b)
			else:
				print('в функции divisionTwoInts параметр type указан неправильно, програмист, вызвавший функцию - клоун')
				return 'TypeError'
	def enterMarks():
		i = 0
		while i != int(len(listOfObjects)):
			obj = open(listOfObjects[i], 'a')
			print(listOfObjectsToShow[i])
			while True:
				try:
					newMarks_str = str(input('оценки писать в строчку, без пробелов'))
					if newMarks_str == '':
						break
					int(newMarks_str)
				except ValueError:
					print('неверное значение')
					continue
				else:
					break
			obj.write(newMarks_str)
			obj.close()
			i+=1

	def countAvarage():
		marksCount = 0
		i = int(0)
		sumOfMarks = 0
		while i != int(len(listOfObjects)):
			i2 = int(0)
			obj = open(listOfObjects[i], 'r')
			listOfMarks = list(str(obj.read()))
			while i2 != int(len(listOfMarks)):
				if len(listOfMarks) == 0:
					break
				marksCount+=1
				sumOfMarks += int(listOfMarks[i2])
				i2+=1
			i+=1
		return str(divisionTwoInts(sumOfMarks, marksCount, 'float'))

	def showJournal(numOfObj):
		obj = open(listOfObjects[numOfObj], 'r')
		listOfMarks = list(obj.read())
		obj.close()
		x = 0
		print(listOfObjectsToShow[numOfObj] + '\n оценки: ', end='')
		while x != len(listOfMarks):
			print(listOfMarks[x] + ' ', end='')
			x+=1
		sumOfMarks = 0
		x = 0
		while x != len(listOfMarks):
			sumOfMarks+=int(listOfMarks[x])
			x+=1
		if divisionTwoInts(sumOfMarks, len(listOfMarks), 'int') == 'ZeroDivisionError':
			print('средний бал неопределен ')
		else:
			print('средний бал: ' + str(divisionTwoInts(sumOfMarks, len(listOfMarks), 'float')), end=' ')
			print('отклонение от плана ' + str(divisionTwoInts(sumOfMarks, len(listOfMarks), 'float') - float(planedMarkForIObj[numOfObj])) + ' балов')
		return ''
	def showAllJournal():
		i = 0
		while i != 14:
			print(showJournal(i), end='')
			i+=1
	def showPlan():
		x = 0
		while x != 14:
			print(listOfObjectsToShow[x] + ' ' + planedMarkForIObj[x])
			x +=1
	try:
		ask1 = int(input())
	except ValueError:
		continue
	if ask1 == 1:
		enterMarks()
	elif ask1 == 2:
		x = 0
		while x != 14:
			showJournal(x)
			x+=1
		print('общий средний бал ' + countAvarage())
	elif ask1 == 3:
		x = 0
		while x != 14:
			print(str(x+1) + ' ' + listOfObjectsToShow[x])
			x+=1
		try:
			print(showJournal(int(input('по какому именно?'))-1))
		except IndexError:
			print('нету такого предмета')
	elif ask1 == 4:
		showAllJournal()
	elif ask1 == 5:
		showPlan()
	elif ask1 == 6:
		x = random.random()
		print(x)
		if float(x) > 0.5:
			print('Безусловно, российское образование является одним из лучших в мире, Россия - ведущая держава в сфере\
			предоставления гражданам качественного, актуального и самое главное - доступного школьного и высшего образования\
				  что касается сумм бесконечных геомерических рядов в учебнике алгебры 9-го класса... знаете, совсем недавно\
				  как раз посещал московскую школу, \
				  меня очень, к слову, впечатлил ее внешний вид, а современный ремонт важен для процесса учебы. \
				  также я беседовал с многими преподавателями, очень умные и компитентные в своем деле люди, ну так что касается \
				  вашего вопроса - могу вас полностью заверить в том, что современные учебники проходят полную проверку\
				  перед попаданием непосредственно в прекрасные российские школы, в этом плане я горжусь нашей страной')
		else:
			print('zzz')
	input()
''' DOCUMENTATION
	divisionTwoInts()(a, b, type)
a - число, которое делят
b - число, на которое делят
type - тип возвращаемого значения. Допустимые значения: int, str, float.Тип писать в кавычках.
Если указан неправильно напишет в 'функции divisionTwoInts() параметр type указан неправильно'
и вернет TypeError
	listOfObjects
Список имен файлов. В самих файлах указаны оценки без пробелов
	listOfObjectsToShow
Список предметов. Логический i-й элемент является реальным воплощением i-го элемента списка listOfObjects
	planedMarkForIObj
Список оценок. Логический i-й элемент представляет соло планируемую оценку по i-му предмету списка listOfObjectsToShow
...
лень дописывать
'''
