from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget


class StandardTextInput(BoxLayout):
    text_input_wid = ObjectProperty(None)


class CPPopup(Popup):
    ballast_bonus_input_wid = ObjectProperty(None)
    aps_hire_rate_input_wid = ObjectProperty(None)

    def Close(self):
        print(self.ballast_bonus_input_wid.text_input_wid.text,
              self.aps_hire_rate_input_wid.text_input_wid.text)
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
        self.dismiss()


class ListElement(BoxLayout):
    description_wid = ObjectProperty(None)

    # Add could move into CalculatorApp-class
    def Add(self, app, element_type_selected):
        if app.line_number < 9:
            self.description_wid.text = element_type_selected
            pad = app.root.ids.list.children[0]
            app.root.ids.list.remove_widget(pad)
            app.root.ids.list.add_widget(self)
            app.root.ids.list.add_widget(Widget())
            app.line_number += 1

    # Remove cannot move into CalculatorApp-class,
    # reference by instance to itself will be lost
    # !!! or maybe just do: app.Remove(root) !!!
    def Remove(self, app):
        self.parent.remove_widget(self)
        app.line_number -= 1


class AddElementDropDown(DropDown):
    pass


class CalculatorApp(App):

    line_number = 0
    instance = 0
    element_type_selected = 0

    def CPPopupOpen(self):
        CPPopup().open()

    def VSLPopupOpen(self):
        VSLPopup().open()

    def ListElementAdd(self, element_type_selected):
        ListElement().Add(self, element_type_selected)

    def AddElementDropDownOpen(self, AddElementButton):
        DropDownInstance = AddElementDropDown()
        DropDownInstance.open(AddElementButton)
        DropDownInstance.bind(
            on_select = lambda instance, element_type_selected: setattr(
                self, 'element_type_selected', element_type_selected
            )
        )

    def Reset(self):
        self.root.ids.list.clear_widgets()
        self.root.ids.list.add_widget(Widget())
        self.root.ids.dop.text = 'DOP'
        self.line_number = 0

    def Calculate(self):
        self.root.ids.dop.text = '123456'


if __name__ == '__main__':
    CalculatorApp().run()