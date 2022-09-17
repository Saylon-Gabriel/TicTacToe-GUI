from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
	pass


class Game(Screen):
	btn1 = ObjectProperty(None)
	btn2 = ObjectProperty(None)
	btn3 = ObjectProperty(None)
	btn4 = ObjectProperty(None)
	btn5 = ObjectProperty(None)
	btn6 = ObjectProperty(None)
	btn7 = ObjectProperty(None)
	btn8 = ObjectProperty(None)
	btn9 = ObjectProperty(None)
	
	matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	jogadas = 0
	quem_joga = 1
	max_jogadas = 9
	vencedor = ''
	win = False
	
	def on_pressed(self, id, l, c):
		if self.jogadas < self.max_jogadas and self.quem_joga == 1:
			self.update(id, l, c, 'X')
			self.quem_joga = 2
			self.jogadas += 1
		elif self.jogadas < self.max_jogadas and self.quem_joga == 2:
			self.update(id, l, c, 'O')
			self.quem_joga = 1
			self.jogadas += 1
	def update(self, id, l, c, sym):
		self.matriz[l][c] = sym
		id.text = self.matriz[l][c]
		id.disabled = True
	def on_releassed(self, id):
		self.vencedor = self.winCheck()
		if self.vencedor == 'X' or self.vencedor == 'O':
			self.reset()
	def reset(self):
		self.matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.jogadas = 0
		self.quem_joga = 1
		self.max_jogadas = 9
		self.vencedor = ''
		self.win = False
		self.ids.btn1.text = ''
		self.ids.btn2.text = ''
		self.ids.btn3.text = ''
		self.ids.btn4.text = ''
		self.ids.btn5.text = ''
		self.ids.btn6.text = ''
		self.ids.btn7.text = ''
		self.ids.btn8.text = ''
		self.ids.btn9.text = ''
	
		self.ids.btn1.disabled = False
		self.ids.btn2.disabled = False
		self.ids.btn3.disabled = False
		self.ids.btn4.disabled = False
		self.ids.btn5.disabled = False
		self.ids.btn6.disabled = False
		self.ids.btn7.disabled = False
		self.ids.btn8.disabled= False
		self.ids.btn9.disabled = False
	
	def winCheck(self):
		vit = 'n'
		simbolos = ['X', 'O']
		
		for s in simbolos:
			
			vit = 'n'
			il=ic=0
			
			while il < 3:
				soma = 0
				ic = 0
				
				while ic < 3:
					if self.matriz[il][ic] == s:
						soma+=1
					ic+=1
				if soma == 3:
					vit = s
					break
				il+=1
			if vit != 'n':
				break
				
			il=ic=0
			while ic < 3:
				soma = 0
				il = 0
				
				while il < 3:
					if self.matriz[il][ic] == s:
						soma+=1
					il+=1
				if soma == 3:
					vit = s
					break
				ic+=1
			if vit != 'n':
				break
				
			soma = 0
			idiag = 0
			
			while idiag < 3:
				if self.matriz[idiag][idiag] == s:
					soma+=1
				idiag+=1
			if soma == 3:
				vit = s
				break
			
			soma = 0
			idiag = 0
			idiagl = 0
			idiagc = 2
			
			while idiagc >= 0:
				if self.matriz[idiagl][idiagc] == s:
					soma+=1
				idiagl+=1
				idiagc-=1
			if soma == 3:
				vit = s
				break
		return vit
class App(App):
	def build(self):
		return Manager()
		
App().run()