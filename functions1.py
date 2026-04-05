def plantsame():
	if(can_harvest()):
		ett = get_entity_type()
		harvest()
		plant(ett)
		if(get_water()<0.3):
			use_item(Items.Water)
def default():
	X = get_world_size()-2
	Y = get_world_size()-6
	for i in range(2):
		for j in range(Y-1):
			till()
			plant(Entities.Carrot)
			move(North)
		till()
		plant(Entities.Carrot)
		move(East)
		for j in range(Y-1):
			till()
			plant(Entities.Carrot)
			move(South)
		till()
		plant(Entities.Carrot)
		move(East)
	for i in range((X-4)/2):
		for j in range(Y-1):
			if((get_pos_x()+get_pos_y())%2==0):
				plant(Entities.Tree)
			move(North)
		if((get_pos_x()+get_pos_y())%2==0):
			plant(Entities.Tree)
		move(East)
		for j in range(Y-1):
			if((get_pos_x()+get_pos_y())%2==0):
				plant(Entities.Tree)
			move(South)
		if((get_pos_x()+get_pos_y())%2==0):
			plant(Entities.Tree)
		move(East)
	for i in range(X):
		move(West)
	while True:
		for i in range(X/2):
			for j in range(Y-1):
				plantsame()
				move(North)
			plantsame()
			move(East)
			for j in range(Y-1):
				plantsame()
				move(South)
			plantsame()
			move(East)
		for i in range(X):
			move(West)