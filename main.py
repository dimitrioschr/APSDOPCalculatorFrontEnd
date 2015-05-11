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
class VSLPopup(Popup):
    rob_input_wid = ObjectProperty(None)
    price_input_wid = ObjectProperty(None)
    speed_input_wid = ObjectProperty(None)
    consumption_input_wid = ObjectProperty(None)
class ListElement(BoxLayout):
    description_wid = ObjectProperty(None)
class AddElementDropDown(DropDown):
    pass
class MainCalculatorLayout(BoxLayout):
    list_wid = ObjectProperty(None)
    dop_wid = ObjectProperty(None)


class CalculatorApp(App):

    line_number = 0
    element_type_selected = 0

    def CPPopupOpen(self):
        CPPopup().open()

    def CPPopupClose(self, CPPopupInstance):
        print(CPPopupInstance.ballast_bonus_input_wid.text_input_wid.text,
              CPPopupInstance.aps_hire_rate_input_wid.text_input_wid.text)
        CPPopupInstance.dismiss()

    def VSLPopupOpen(self):
        VSLPopup().open()

    def VSLPopupClose(self, VSLPopupInstance):
        print(VSLPopupInstance.rob_input_wid.text_input_wid.text,
              VSLPopupInstance.price_input_wid.text_input_wid.text,
              VSLPopupInstance.speed_input_wid.text_input_wid.text,
              VSLPopupInstance.consumption_input_wid.text_input_wid.text)
        VSLPopupInstance.dismiss()

    def AddElementDropDownOpen(self, AddElementButton):
        DropDownInstance = AddElementDropDown()
        DropDownInstance.open(AddElementButton)
        DropDownInstance.bind(
            on_select = lambda instance, element_type_selected: setattr(
                self, 'element_type_selected', element_type_selected
            )
        )

    def ListElementAdd(self, element_type_selected):
        if self.line_number < 9:
        # idea: make the pad-Widget a named class object and get
        # its property-height before adding an additional element,
        # then add only if available height exceeds the element height = 40
            ElementToAdd = ListElement()
            ElementToAdd.description_wid.text = element_type_selected
            self.root.list_wid.remove_widget(self.root.list_wid.children[0])
            self.root.list_wid.add_widget(ElementToAdd)
            self.root.list_wid.add_widget(Widget())
            self.line_number += 1

    def ListElementRemove(self, ElementToRemove):
        ElementToRemove.parent.remove_widget(ElementToRemove)
        self.line_number -= 1

    def Reset(self):
        self.root.list_wid.clear_widgets()
        self.root.list_wid.add_widget(Widget())
        self.root.dop_wid.text = 'DOP'
        self.line_number = 0

    def Calculate(self):
        self.root.dop_wid.text = '123456'


if __name__ == '__main__':
    CalculatorApp().run()