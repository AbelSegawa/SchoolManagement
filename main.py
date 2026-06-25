from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from database.db import init_db

class SchoolApp(MDApp):
    def build(self):
        init_db()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

SchoolApp().run()
