from kivy.uix.screen import Screen
from kivy.lang import Builder

Builder.load_file('kv/login.kv')

class LoginScreen(Screen):
    def login(self):
        self.manager.current = 'dashboard'
