import cmd
from rooms import get_room
import textwrap

class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		
		self.loc = get_room("A31")
		self.look()

	def move(self, dir):
		newroom = self.loc._neighbor(dir)
		if newroom is None:
			print("You can't go that way.")
		else:
			self.loc = get_room(newroom)
			self.look()
	
	def look(self):
		print('')
		for line in textwrap.wrap(self.loc.description, 72):
			print(line)
	
	def do_look(self, args):
		"""Shows description of current room"""
		self.look()
	
	def do_n(self, args):
		"""Go North"""
		self.move('n')
		
	def do_s(self, args):
		"""Go South"""
		self.move('s')
		
	def do_e(self, args):
		"""Go East"""
		self.move('e')
		
	def do_w(self, args):
		"""Go West"""
		self.move('w')

	def do_search(self, args):
		"""Search the room for anything hidden"""
		if len(self.loc.hidden) > 0:
			print('')
			for line in textwrap.wrap(self.loc.hidden, 72):
				print(line)
		else:
			print("\nYou search the room, but find nothing of interest.")

	def do_inspect(self, args):
		"""Investigate a little more thoroughly than 'search'."""
		print("\nWhat would you like to inspect?")
		action = input("")
		if action in self.loc.secrets:
			print('')
			for line in textwrap.wrap(self.loc.secret_result, 72):
				print(line)
		else:
			print("\nYou find nothing of interest.")
	
	def do_get(self, args):
		"""Pick up an item you discover and add it to your inventory"""
		
	
	def do_quit(self, args):
		"""Leaves the game."""
		print("Thank you for playing.")
		return True

if __name__ == "__main__":
	g = Game()
	g.cmdloop()
