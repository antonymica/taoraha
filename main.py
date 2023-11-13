from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
import datetime
from datetime import date
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
import kivy
kivy.require('2.2.1')  # remplacez ceci par votre version de Kivy

from kivy.config import Config
Config.set('kivy', 'clipboard', 'sdl2')  # ou 'simple' ou 'pygame'


class TodoCard(MDFloatLayout):
    title = StringProperty()
    description = StringProperty()


class TaorahaApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("addtodo.kv"))
        return screen_manager
    
    def on_start(self):
        today = date.today()
        wd = date.weekday(today)
        days = ['Alatsinainy', 'Talata', 'Alarobia', 'Alakamisy', 'Zoma', 'Asabotsy', 'Alahady']
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime("%b"))
        day = str(datetime.datetime.now().strftime("%d"))
        screen_manager.get_screen("main").date.text=f"{days[wd]}, {day} {month} {year}"
        
        
    def on_complete(self, checkbox, value, description, bar):
        if value:
            description.text = f"[s]{description.text}[/s]"
            bar.md_bg_color = 0, 179/255, 0, 1
        else:
            remove = ["[s]", "[/s]"]
            for i in remove:
                description.text = description.text.replace(i, "")
                bar.md_bg_color = 1, 170/255, 23/255, 1
    
    def add_todo(self, title, description):
        if title != "" and description != "" and len(title) < 21 and len(description) < 61:
            screen_manager.current = "main"
            screen_manager.transition.direction = "right"
            screen_manager.get_screen("main").todo_list.add_widget(TodoCard(title=title, description=description))
            screen_manager.get_screen("add_todo").description.text=''
        elif title == "":
            Snackbar(text='Hadigno ny lohateny!', snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
                     size_hint_x=(Window.width - 20) / Window.width, bg_color=(1, 170/255, 23/255, 1),
                     font_size="18sp").open()
        elif description == "":
            Snackbar(text='Hadigno ny fanazavana', snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
                     size_hint_x=(Window.width - 20) / Window.width, bg_color=(1, 170/255, 23/255, 1),
                     font_size="18sp").open()
        elif len(title) > 21:
            Snackbar(text='Lava loatsa ny lohateny', snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
                     size_hint_x=(Window.width - 20) / Window.width, bg_color=(1, 170/255, 23/255, 1),
                     font_size="18sp").open()
        elif len(description) > 60:
            Snackbar(text='Lava loatsa ny fanazavana', snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
                     size_hint_x=(Window.width - 20) / Window.width, bg_color=(1, 170/255, 23/255, 1),
                     font_size="18sp").open()

if __name__ == "__main__":
    TaorahaApp().run()
