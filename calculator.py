from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class calculatorScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class myCalculator(App):

    def build(self):
        return RootWidget()
    

myCalculator().run()