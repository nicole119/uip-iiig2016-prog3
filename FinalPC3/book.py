import string

"""
Se inicializa la clase con collecciones a la base de datos MongoDB
"""
class book(object):

#Inicimos la clase y se configura la base de datos con collecciones

	def __init__(self, database):
		self.db = database
		self.mynames = database.mynames

#Esta funcion busca los nombres
	def find_names(self):
		l = []
		for each_name in self.mynames.find():
			l.append({'name':each_name['name'], 'email':each_name['email']})

		return l

#Esta funcion maneja la insercion de nombres
	def insert_name(self,newname,newemail):
		newname = {'name':newname,'email':newemail}
		self.mynames.insert(newname)
