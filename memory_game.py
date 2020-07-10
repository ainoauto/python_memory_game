import sys, pygame, random
mouse_clicked = -1
mouse_second_click = -1
mouse_previous_state = 0
mouse_current_state = 0
hidden_cards = 0


def main():
	pygame.init()

	size = width, height = 500, 600
	screen = pygame.display.set_mode(size)
	white = (255,255,255)
	image_card = pygame.image.load("card.jpg")
	image_card_hover = pygame.image.load("card2.jpg")
	image_files = ["card_img", "card_img_2", "card_img_3", "card_img_4", "card_img_5", "card_img_6", \
		"card_img_7", "card_img_8", "card_img_9", "card_img_10", "card_img_11", "card_img_12", "card_img_13", \
		"card_img_14", "card_img_15", "card_img_16", "card_img_17", "card_img_18"]
	card_images = []
	card_visibility = []
	
	for file in image_files: 
		loaded = pygame.image.load(file + ".jpg")
		card_images.append(loaded)
		card_images.append(loaded) #append loaded images 2x
		card_visibility.append(True) #default setting for all cards
		card_visibility.append(True)
		
	random.shuffle(card_images)
		
	screen.fill(white)
	
	x = (width * 0.05)
	y = (height * 0.05)
	
	def mouse_state():
		global mouse_previous_state
		global mouse_current_state
		global mouse_state
		mouse_previous_state = mouse_current_state
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_current_state = 1
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_current_state = 0
		
	
	def card(x,y,id):
		global mouse_clicked
		global mouse_second_click
		global mouse_state
		global hidden_cards
		mp = pygame.mouse.get_pos()
		image = image_card
		mouse_in_image = x < mp[0] < (x + 43) and y < mp[1] < (y + 56)
		if mouse_in_image:
			image = image_card_hover
		if mouse_in_image and mouse_previous_state == 0 and mouse_current_state == 1:
			if mouse_clicked > -1: #if the first card is turned
				mouse_clicked = mouse_clicked
				if mouse_second_click > -1: #if the second card is turned
					if card_images[mouse_clicked] == card_images[mouse_second_click]:
						card_visibility[mouse_clicked] = False
						card_visibility[mouse_second_click] = False
						hidden_cards = hidden_cards + 2
					mouse_clicked = -1 #resets
					mouse_second_click = -1 #resets
				elif mouse_clicked != id:
					mouse_second_click = id #turns the second card
			else:
				mouse_clicked = id #turns the first card
		if mouse_clicked == id or mouse_second_click == id: #if the card is turned, set image
			image = card_images[id]
		screen.blit(image, (x,y))
	
	def board_cards(x,y):
		value_y = y
		id = 0
		for x_coordinate in range(0,6):
			for y_coordinate in range(0,6):
				if card_visibility[id] == True:
					card(x,y,id)
				id = id + 1 #card id
				y = y + 80 #card offset on y
			x = x + 60 #card offset on x
			y = value_y
			
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(white)
		board_cards(x,y)
		if hidden_cards == 36:
			myfont = pygame.font.SysFont("monospace", 15)
			label = myfont.render("Congrats, you won!", 1, (255,102,102))
			screen.blit(label, (100, 100))
		mouse_state()
		pygame.display.update()

main()