
import random


with open("word.txt", "r") as words:
	array = []
	for line in words:
		array.append(line.upper())

play = 1
while play == 1:
	a = random.randint(0 , (len(array)-1))
	
	word = list(array[a][:(len(array[a])-1)])
	Str = list(array[a][:(len(array[a])-1)])
	
	for index in range(len(Str)):
	   if Str[index].isalpha():
	   	Str[index] = "_"
	chances = 6
	missed = []
	choose = []
        win = 0
	while chances > 0:
		g = raw_input('Yor geuss (letters only): ')
                gg = list(g)
                if len(gg) != 1:
			print 'not avalid character. please enter letter'
			continue
                guess = gg[0]
                guess = guess.upper()
		if not guess.isalpha():
			print 'not avalid character. please enter letter'
			continue
		choosed = 0
		for c in choose:
			if c == guess:
				choosed = 1
		if choosed == 1:
			print 'you have already tried this character. guess again'
			continue

		choose.append(guess)
		good = 0;
		for index in range(len(word)):
		   if word[index] == guess:
				Str[index] = guess
				good = 1

		if good == 0:
			chances -= 1
			missed.append(guess)

		win = 1
		for index in range(len(Str)):
		   if Str[index] == '_':
				win = 0

		print'Chances Remaining : ', chances
		print'Missed Letters : ', missed
		print '\n' , Str

		if win == 1:
			print "Congratulation"
			break;

	if win == 0:
            print 'you lost the word is : ' , word
	pp = raw_input('play again (Y/N) : ')
        p = pp[0]
	p = p.upper()
	if p == 'N':
		play = 0

