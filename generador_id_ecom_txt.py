import os
from datetime import date
from datetime import datetime


class Generator():

	def iniciar_generador(self):
		if os.path.isfile ("database/id.txt") == False:
			txt = open("database/id.txt", "w")
			txt.write("9")
			txt.close()
			return '9'
		else:
			txt = open ("database/id.txt", "r")
			ids = txt.read()
			txt.close()
			return str(ids)
	
	def new_id(self):
		ids = self.iniciar_generador()
		ids = int(ids)+1
		txt = open ("database/id.txt", 'w')
		num = "{}".format(ids)
		txt.write(num)
		txt.close()
		return str(ids)
  
  
  
  
