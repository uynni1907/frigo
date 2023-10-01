import geocoder
from kivy.config import Config

# Set the resolution
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView,MapMarker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
class Screen_1(Screen):
    def __init__(self, **kwargs):
        super(Screen_1, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen1.png'))

        button1 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.205},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_2)
        self.add_widget(button1)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

class Screen_2(Screen):
    def __init__(self, **kwargs):
        super(Screen_2, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen2.png'))

#WIDE BUTTON
        button1 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.395},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_3)
        self.add_widget(button1)

        button2 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.27},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_4)
        self.add_widget(button2)

        button3 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.145},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_5)
        self.add_widget(button3)

    def change_to_3(self, instance):
        self.manager.current = 'Screen_3'

    def change_to_4(self,instance):
        self.manager.current = 'Screen_4'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

class Screen_3(Screen):
    def __init__(self, **kwargs):
        super(Screen_3, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen3.png'))

#ICON BUTTON
        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.6, 'y':.92},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_2)
        self.add_widget(button4)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

class Screen_4(Screen):
    def __init__(self, **kwargs):
        super(Screen_4, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen4.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)
        
        button4 = Button(size_hint=(.08, .07),
                            pos_hint={'x':.344, 'y':.73},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_10)
        self.add_widget(button4)

        button5 = Button(size_hint=(.04, .04),
                            pos_hint={'x':.62, 'y':.91},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button5.bind(on_press=self.change_to_12)
        self.add_widget(button5)
    
    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_10(self,instance):
        self.manager.current = 'Screen_10'

    def change_to_12(self,instance):
        self.manager.current = 'Screen_12'

class Screen_5(Screen):
    def __init__(self, **kwargs):
        super(Screen_5, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen5.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.56},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_6)
        self.add_widget(button4)

        button5 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.42},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button5.bind(on_press=self.change_to_8)
        self.add_widget(button5)

        button6 = Button(size_hint=(.30, .07),
                        pos_hint={'x':.35, 'y':.29},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button6.bind(on_press=self.change_to_13)
        self.add_widget(button6)

        button7 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.6, 'y':.92},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button7.bind(on_press=self.change_to_2)
        self.add_widget(button7)
        
    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_6(self,instance):
        self.manager.current = 'Screen_6'

    def change_to_8(self,instance):
        self.manager.current = 'Screen_8'

    def change_to_13(self,instance):
        self.manager.current = 'Screen_13'

class Screen_6(Screen):
    def __init__(self, **kwargs):
        super(Screen_6, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen6.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.04, .04),
                            pos_hint={'x':.6, 'y':.92},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_5)
        self.add_widget(button4)

        button5 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.6, 'y':.63},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button5.bind(on_press=self.change_to_7)
        self.add_widget(button5)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_7(self,instance):
        self.manager.current = 'Screen_7'

class Screen_7(Screen):
    def __init__(self, **kwargs):
        super(Screen_7, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen7.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.04, .04),
                            pos_hint={'x':.61, 'y':.91},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_6)
        self.add_widget(button4)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_6(self,instance):
        self.manager.current = 'Screen_6'

class Screen_8(Screen):
    def __init__(self, **kwargs):
        super(Screen_8, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen8.png'))
        button_back = Button(size_hint=(.04, .04),
                        pos_hint={'x':.61, 'y':.676},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button_back.bind(on_press=self.change_to_5)
        self.add_widget(button_back)
        button1 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.55, 'y':.6},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_7)
        self.add_widget(button1)
        button2 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.43, 'y':.6},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_7)
        self.add_widget(button2)
        button3 = Button(size_hint=(.08, .06),
                        pos_hint={'x':.46, 'y':.47},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_10)
        self.add_widget(button3)
    def change_to_7(self, instance):
        self.manager.current = 'Screen_7'

    def change_to_10(self,instance):
        self.manager.current = 'Screen_10'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

class Screen_9(Screen):
    def __init__(self, **kwargs):
        super(Screen_9, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen9.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.04, .04),
                            pos_hint={'x':.62, 'y':.89},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_13)
        self.add_widget(button4)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'
    
    def change_to_13(self,instance):
        self.manager.current = 'Screen_13'

class Screen_10(Screen):
    def __init__(self, **kwargs):
        super(Screen_10, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen10.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button_back = Button(size_hint=(.04, .04),
            pos_hint={'x':.612, 'y':.92},
            background_color=(0,0,0,0),
            border=(0, 0, 0, 0))
        button_back.bind(on_press=self.change_to_4)
        self.add_widget(button_back)

        button_4 = Button(size_hint=(.04, .04),
            pos_hint={'x':.35, 'y':.845},
            background_color=(0,0,0,0),
            border=(0, 0, 0, 0))
        button_4.bind(on_press=self.change_to_11)
        self.add_widget(button_4)
    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_4(self,instance):
        self.manager.current = 'Screen_4'
    def change_to_11(self,instance):
        self.manager.current = 'Screen_11'

class Screen_11(Screen):
    def __init__(self, **kwargs):
        super(Screen_11, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen11.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)
    #chinh lai accept
        button4 = Button(size_hint=(.1, .1),
                        pos_hint={'x':.35, 'y':.12},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_10)
        self.add_widget(button4)
    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'
    def change_to_10(self,instance):
        self.manager.current = 'Screen_10'
class Screen_12(Screen):
    def __init__(self, **kwargs):
        super(Screen_12, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen12.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.04, .04),
                            pos_hint={'x':.615, 'y':.91},
                            background_color=(0,0,0,0),
                            border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_4)
        self.add_widget(button4)

        button5 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.6, 'y':.42},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button5.bind(on_press=self.change_to_9)
        self.add_widget(button5)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'

    def change_to_4(self,instance):
        self.manager.current = 'Screen_4'

    def change_to_9(self,instance):
        self.manager.current = 'Screen_9'

class Screen_13(Screen):
    def __init__(self, **kwargs):
        super(Screen_13, self).__init__(**kwargs)
        self.add_widget(Image(source='image\screens\screen13.png'))

        button1 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.38, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button1.bind(on_press=self.change_to_5)
        self.add_widget(button1)

        button2 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.477, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button2.bind(on_press=self.change_to_2)
        self.add_widget(button2)

        button3 = Button(size_hint=(.05, .07),
                        pos_hint={'x':.575, 'y':.03},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button3.bind(on_press=self.change_to_3)
        self.add_widget(button3)

        button4 = Button(size_hint=(.07, .07),
                        pos_hint={'x':.46, 'y':.50},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button4.bind(on_press=self.change_to_9)
        self.add_widget(button4)

        button5 = Button(size_hint=(.04, .04),
                        pos_hint={'x':.6, 'y':.92},
                        background_color=(0,0,0,0),
                        border=(0, 0, 0, 0))
        button5.bind(on_press=self.change_to_5)
        self.add_widget(button5)

    def change_to_2(self, instance):
        self.manager.current = 'Screen_2'

    def change_to_3(self,instance):
        self.manager.current = 'Screen_3'

    def change_to_5(self,instance):
        self.manager.current = 'Screen_5'
    
    def change_to_9(self,instance):
        self.manager.current = 'Screen_9'

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(CustomScreenManager, self).__init__(transition=FadeTransition(), **kwargs)

class TestApp(App):
    def build(self):
        sm = CustomScreenManager()
        sm.add_widget(Screen_1(name='Screen_1'))
        sm.add_widget(Screen_2(name='Screen_2'))
        sm.add_widget(Screen_3(name='Screen_3'))
        sm.add_widget(Screen_4(name='Screen_4'))
        sm.add_widget(Screen_5(name='Screen_5'))
        sm.add_widget(Screen_6(name='Screen_6'))
        sm.add_widget(Screen_7(name='Screen_7'))
        sm.add_widget(Screen_8(name='Screen_8'))
        sm.add_widget(Screen_9(name='Screen_9'))
        sm.add_widget(Screen_10(name='Screen_10'))
        sm.add_widget(Screen_11(name='Screen_11'))
        sm.add_widget(Screen_12(name='Screen_12'))
        sm.add_widget(Screen_13(name='Screen_13'))
        return sm

if __name__ == '__main__':
    TestApp().run()