import kivy
from kivy.app import App
from kivy.properties import Objectproperty
from kivy.uix.widget import widget


class MyGridLayout(widget):
    
        self.name = Objectproperty(None)
        self.address = Objectproperty(None)
        self.number = Objectproperty(None)

        def press(self):
            Methodname = self.name.text
            Methodaddress = self.address.text
            Methodnumber = self.number.text
            
class MyApp(App) :
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
  