import bottle
import pymongo
import book

"""
Ruta por defecto para el index
"""
@bottle.route('/')
def book_index():
	mynames_list = book.find_names()
	return bottle.template('index', dict(mynames = mynames_list))


"""
Postea las nuevas entrada para ser insertadas a MongoDB
"""
@bottle.route('/newguest', method='POST')
def insert_newguest():
	name = bottle.request.forms.get("name")
	email = bottle.request.forms.get("email")
	book.insert_name(name,email)
	bottle.redirect('/')



"""
Se configura la conexion de datos
"""

"""
Configura una conexion string al servidor local
"""
connection_string = "mongodb://localhost"

"""
Gestiona la conexion entre MongoDB y PyMongo, PyMongo maneja nuestro pool
"""
connection = pymongo.MongoClient(connection_string)
#Now we want to set a context to the names database we created using the mongo interactive shell
"""
Enviamos la base de datos de nombres al shell de mongo
"""
database = connection.names

"""
Se adjunta la data u objeto
"""
book = book.book(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)