from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

resource_add_path('C:\Windows\Fonts')
LabelBase.register(DEFAULT_FONT,'HGRPRE.TTC')

class GreetingWidget(Widget):
    text = StringProperty()
    def __init__(self, **kwargs):
        super(GreetingWidget, self).__init__(**kwargs)
        self.text = "START"
    
    def morningClick(self):
        self.text = 'おはよう'

    def eveningClick(self):
        self.text = 'こんにちは'
        
    def goodnightClick(self):
        self.text = 'こんばんは'

class Test2App(App):
    def __init__(self, **kwargs):
        super(Test2App, self).__init__(**kwargs)
        self.title = 'greeting'

Test2App().run()

