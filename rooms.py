import json

def get_room(id):
	ret = None
	with open(str(id)+".json", "r") as f:
		jsontext = f.read()
		d = json.loads(jsontext)
		d['id'] = id
		ret = Room(**d)
	return ret

class Room():
	def __init__(self, id, description="an empty room", hidden="", secrets="", secret_result="", items="", neighbors={}):
		self.id = id
		self.description = description
		self.hidden = hidden
		self.secrets = secrets
		self.secret_result = secret_result
		self.items = items
		self.neighbors = neighbors
	
	def _neighbor(self, direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None
	
	def north(self):
		return self_neighbor('n')

	def south(self):
		return self_neighbor('s')

	def east(self):
		return self_neighbor('e')

	def west(self):
		return self_neighbor('w')
