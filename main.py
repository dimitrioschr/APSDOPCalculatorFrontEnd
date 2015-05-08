from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty


class CalculatorApp(App):

    class StandardTextInput(BoxLayout):
        text_input_wid = ObjectProperty(None)

    class CPPopup(Popup):
        ballast_bonus_input_wid = ObjectProperty(None)
        aps_hire_rate_input_wid = ObjectProperty(None)

        def Close(self):
            print(self.ballast_bonus_input_wid.text_input_wid.text,
                  self.aps_hire_rate_input_wid.text_input_wid.text)
            # print to prove access to data
            self.dismiss()

    class VSLPopup(Popup):
        rob_input_wid = ObjectProperty(None)
        price_input_wid = ObjectProperty(None)
        speed_input_wid = ObjectProperty(None)
        consumption_input_wid = ObjectProperty(None)

        def Close(self):
            print(self.rob_input_wid.text_input_wid.text,
                  self.price_input_wid.text_input_wid.text,
                  self.speed_input_wid.text_input_wid.text,
                  self.consumption_input_wid.text_input_wid.text)
            # print to prove access to data
            self.dismiss()

    class ListElement(BoxLayout):

        def Add(self, app):
            if app.line_number < 9:
                app.root.ids.list.add_widget(self)
                app.line_number += 1
                print(app.line_number)
                # do all necessary things when adding
                # an element to the list

        def Remove(self, app):
            self.parent.remove_widget(self)
            app.line_number -= 1
            print(app.line_number)
            # also do any more stuff needed
            # when elements are removed from list


    line_number = 0

    def Reset(self):
        self.root.ids.list.clear_widgets()
        self.root.ids.dop.text = 'DOP'
        self.line_number = 0
        # do any other things to bring app
        # back to reset state

    def Calculate(self):
        self.root.ids.dop.text = '123456'


if __name__ == '__main__':
    CalculatorApp().run()