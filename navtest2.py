from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.pickers import MDDatePicker,MDTimePicker
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screenmanager import ScreenManager




class MyTabs(TabbedPanel):
    pass

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):

    pass

class ThirdWindow(Screen):
    pass

class Windows(ScreenManager):
    pass


class EvansApp(MDApp):
    data = {
        'language-python': 'Python',
        'youtube': 'youtube', 'andriod': 'andriod',
    }
    def build(self,):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Amber'
        return Builder.load_file('nav.kv')

EvansApp().run()


