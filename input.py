import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class AppTitle(App):
    def build(self):
        return Label(
            text ="nanana",
            font_size=23,
    
        )    


def main():
    AppTitle().run()


if __name__ == '__main__':
    main()