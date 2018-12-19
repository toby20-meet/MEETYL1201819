'''
class Animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yum! " + self.name + " is eating "+food)
	def description(self):
		print(self.name + " is "+ str(self.age) + " years old  and loves the color "+ self.favorite_color)
	def make_sound(self,times):
		print(self.sound*times)

j = Animal("woof", "doggo", 6, "yellow")
j.eat("Cheese")
j.description()
j.make_sound(3)
'''
'''
class Person(object):
	def __init__(self, name, age, city, gender, fv_breakfast, speciality):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.speciality = speciality
		self.fv_breakfast = fv_breakfast
	def eat(self):
		print(self.name + " is eating "+ self.fv_breakfast)
	def work(self):
		print(self.name+"'s speciality is being a "+ self.speciality)

j = Person("Logan", 23, "New York", "Male", "CornFlakes", "Wood Chuck")
j.eat()
j.work()
'''

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self,lyrics):
		dude = self.lyrics.split('?')
		for i in dude:
			print(i)



Psycho = Song("Johny Johny Yes Papa Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah!  Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah! Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah!")
Psycho.sing_me_a_song("Johny Johny Yes Papa Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah!  Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah! Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah!")
