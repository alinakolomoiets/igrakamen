import random 
botvic=0
pvic=0
p1vic=0
p2vic=0
spisok=[]
s=["ножницы","бумага","камень"]
while True:
	print("1-играть с ботом")
	print("2-играть с другом")
	print("3-правила игры")
	print("4-выйти")
	valik=int(input())
	while valik not in [1,2,3,4]:
			try:
				valik=int(input())
			except ValueError:
				print("1,2,3 или 4")
	if valik==1:
		player=input("Введи действие: ")
		bot=random.choice(s)
		while player not in ["камень","ножницы","бумага"]:
			try:
				player=input("Введи действие: ")
			except ValueError:
				print("Напиши правильно")
		if player=="камень" and bot=="ножницы":
			print("Камень побеждает ножницы («камень затупляет или ломает ножницы»)")
			pvic+=1
		elif player=="бумага" and bot=="камень":
			print("Бумага побеждает камень («бумага обёртывает камень»)")
			pvic+=1
		elif player=="ножницы" and bot=="бумага":
			print("Ножницы побеждают бумагу («ножницы разрезают бумагу»)")
			pvic+=1
		elif bot=="камень" and player=="ножницы":
			print("Камень побеждает ножницы («камень затупляет или ломает ножницы»)")
			botvic+=1
		elif bot=="бумага" and player=="камень":
			print("Бумага побеждает камень («бумага обёртывает камень»)")
			botvic+=1
		elif bot=="ножницы" and player=="бумага":
			print("Ножницы побеждают бумагу («ножницы разрезают бумагу»)")
			botvic+=1
		else:
			print("Ничья")
		print(f"Победы игрока: {pvic}")
		print(f"Победы бота: {botvic}")
	elif valik==2: #проверка не работает
		player1=input("Игрок 1 введи действие: ")
		#while player1 not in ["камень","ножницы","бумага"]:
			#try:
				#player=input("Введи действие: ")
			#except ValueError:
				#print("Напиши правильно")
		player2=input("Игрок 2 введи действие: ")
		if player1=="камень" and player2=="ножницы":
			print("Камень побеждает ножницы («камень затупляет или ломает ножницы»)")
			p1vic+=1
		elif player1=="бумага" and player2=="камень":
			print("Бумага побеждает камень («бумага обёртывает камень»)")
			p1vic+=1
		elif player1=="ножницы" and player2=="бумага":
			print("Ножницы побеждают бумагу («ножницы разрезают бумагу»)")
			p1vic+=1
		elif player2=="камень" and player1=="ножницы":
			print("Камень побеждает ножницы («камень затупляет или ломает ножницы»)")
			p2vic+=1
		elif player2=="бумага" and player1=="камень":
			print("Бумага побеждает камень («бумага обёртывает камень»)")
			p2vic+=1
		elif player2=="ножницы" and player1=="бумага":
			print("Ножницы побеждают бумагу («ножницы разрезают бумагу»)")
			p2vic+=1
		#else:
			#print("Ничья")
		print(f"Победы игрока1: {p1vic}")
		print(f"Победы игрока2: {p2vic}")
	elif valik==3:
		print("Бумага побеждает камень («бумага обёртывает камень»)")
		print("Камень побеждает ножницы («камень затупляет или ломает ножницы»)")
		print("Ножницы побеждают бумагу («ножницы разрезают бумагу»)")
	elif valik==4:
		print("Спасибо за игру")
		break
