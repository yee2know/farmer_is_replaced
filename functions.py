def plant_pumpkin():
	if(get_entity_type()==None):
		plant(Entities.Pumpkin)
		return 0
	elif(get_entity_type()==Entities.Pumpkin):
		return 1
	else:
		plant(Entities.Pumpkin)
		return 0
def pumpkin():
	for i in range(3):
		for j in range(5):
			till()
			move(East)
		till()
		move(North)
		for j in range(5):
			till()
			move(West)
		till()
		if(i!=2):
			move(North)
	for i in range(5):
		move(South)
	while True:
		num=0
		while num<36:
			num = 0
			for i in range(3):
				for j in range(5):
					num+=plant_pumpkin()
					move(East)
				num+=plant_pumpkin()
				move(North)
				for j in range(5):
					num+=plant_pumpkin()
					move(West)
				num+=plant_pumpkin()
				if(i!=2):
					move(North)
			for i in range(5):
				move(South)
		harvest()

def sunflower():
	for i in range(get_world_size()-7):
		till()
		plant(Entities.Sunflower)
		use_item(Items.Water)
		use_item(Items.Water)
		move(North)
	till()
	plant(Entities.Sunflower)
	use_item(Items.Water)
	use_item(Items.Water)
	move(East)
	for i in range(get_world_size()-7):
		till()
		plant(Entities.Sunflower)
		use_item(Items.Water)
		use_item(Items.Water)
		move(South)
	till()
	plant(Entities.Sunflower)
	use_item(Items.Water)
	use_item(Items.Water)
	move(West)
	while True:
		for i in range(get_world_size()-7):
			harvest()
			plant(Entities.Sunflower)
			use_item(Items.Water)
			move(North)
		harvest()
		plant(Entities.Sunflower)
		use_item(Items.Water)
		move(East)
		for i in range(get_world_size()-7):
			harvest()
			plant(Entities.Sunflower)
			use_item(Items.Water)
			move(South)
		harvest()
		plant(Entities.Sunflower)
		use_item(Items.Water)
		move(West)