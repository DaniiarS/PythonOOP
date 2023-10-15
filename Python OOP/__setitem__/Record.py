class Record:
	
	def __init__(self, *args, **kwargs):
		for key in kwargs.keys():
			self.__dict__[key] = kwargs[key]

	def __getitem__(self, item):
		if not isinstance(item, int) or ( item < 0 or item > len(self.__dict__.keys())):
			raise IndexError('неверный индекс поля')

		keyList = list(self.__dict__.keys())
		return self.__dict__[keyList[item]]
	
	def __setitem__(self, key, value):
		if not isinstance( key, int ) or ( key < 0 or key > len(self.__dict__)):
			raise IndexError('неверный индекс поля')

		keyList = list(self.__dict__.keys())
		self.__dict__[keyList[key]] = value
		return self
	
r = Record( file = "fileName", program = "programName")
print( r[0] )
r[0] = 'newFileName'
print( r[0] )