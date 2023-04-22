import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')



Builder.load_file('login.kv')

class LoginScreen(Widget):
    username = ObjectProperty(id = 'username1')
    password = ObjectProperty(id = 'password1')
    
    def validate_login(self, username1, password1):
        if username1 == "sdca.itpe02" and password1 == "@itpe02":
            #print(username1)

            popup = Popup(title="Login Successful", content=Widget(), size_hint=(None, None), size=(250, 200))
            popup.content = BoxLayout(orientation='vertical')
            popup.content.add_widget(Label(text="You have successfully logged in!", font_size=13))
            exit_button = Button(text="Exit", font_size=15, background_color=[1, 0.5, 0, 1],on_press=lambda *args: (popup.dismiss(), self.clear_fields()))
            popup.content.add_widget(exit_button)
            popup.background_color = [1, 0.9, 0.7, 1]  # cream color

            popup.open()
        else:
            popup = Popup(title="Invalid Login", content=Widget(), size_hint=(None, None), size=(250, 200))
            popup.background_color = [1, 0.9, 0.7, 1]  # cream color
            popup.content = BoxLayout(orientation='vertical')
            popup.content.add_widget(Label(text="Invalid username or password.\nPlease try again.", font_size=13))
            popup.content.add_widget(Button(text="OK",font_size=15, background_color=[1, 0.5, 0, 1],  on_press=lambda *args: (popup.dismiss(), self.clear_fields())))
            popup.open()



    def clear_fields(self):
        self.ids.username1.text = ''
        self.ids.password1.text = ''



    def exit_app(self, instance):
        App.get_running_app().stop()



class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
