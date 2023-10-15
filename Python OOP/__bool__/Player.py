import sys

class IntValidate:

	def __set_name__(self, owner, name):
		self.name = name
	
	def __get___(self, instance, name):
		return instance.__dict__[self.name]
	
	def __set__(self, instance, value):
		if self.isvalid(value):
			instance.__dict__[self.name] = value
	
	@classmethod
	def isvalid(cls, value):
		return type(value) is int

class StringValidate:

	def __set_name__(self, owner, name):
		self.name = name
	
	def __get___(self, instance, name):
		return instance.__dict__[self.name]
	
	def __set__(self, instance, value):
		if self.isvalid(value):
			instance.__dict__[self.name] = value
	
	@classmethod
	def isvalid(cls, value):
		return type(value) is str

class Player:
	name = StringValidate()
	old = IntValidate()
	score = IntValidate()

	def __init__(self, name, old, score):
		self.name = name
		self.old = old
		self.score = score
	
	def __bool__(self):
		return self.score > 0

lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [ Player( player.split('; ')[0], int(player.split('; ')[1]), int(player.split(';' )[2])) for player in lst_in]

players_filtered = list(filter( bool, players ))