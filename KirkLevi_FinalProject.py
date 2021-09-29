from breezypythongui import EasyFrame

class BZ(EasyFrame):

    def __init__(self):
        #Window Creation
        EasyFrame.__init__(self, title = "BelowZero",
                           width = 600, height = 500)

        #Greeting
        self.addLabel(text = "Welcome! What kind of cone, ice cream, "
                             "and toppings do you want?",
                      row = 0,
                      column = 1)

        #Label, Button Group, Buttons for Cones
        self.addLabel(text="Cone",
                      row=1, column=0)
        self.coneGroup = self.addRadiobuttonGroup(row = 1,
                                                  column = 0,
                                                  rowspan = 3)
        defaultRB = self.coneGroup.addRadiobutton(text="Regular")
        self.coneGroup.setSelectedButton(defaultRB)
        self.coneGroup.addRadiobutton(text = "Waffle Cone")
        self.coneGroup.addRadiobutton(text="Bowl")

        # Label, Button Group, Buttons for Ice Cream
        self.addLabel(text="Ice Cream",
                      row=1, column=1)
        self.iceGroup = self.addRadiobuttonGroup(row=1,
                                                  column=1,
                                                  rowspan=3)
        defaultRB = self.iceGroup.addRadiobutton(text="Vanilla")
        self.iceGroup.setSelectedButton(defaultRB)
        self.iceGroup.addRadiobutton(text="Chocolate")
        self.iceGroup.addRadiobutton(text="Strawberry")

        # Label, Button Group, Buttons for Toppings
        self.addLabel(text="Toppings",
                      row=1, column=2)
        self.topGroup = self.addRadiobuttonGroup(row=1,
                                                  column=2,
                                                  rowspan=3)
        defaultRB = self.topGroup.addRadiobutton(text="Sprinkles")
        self.topGroup.setSelectedButton(defaultRB)
        self.topGroup.addRadiobutton(text="Chocolate Syrup")
        self.topGroup.addRadiobutton(text="Nuts")

        self.addButton(text = "Place Order", row = 3, column = 1,
                       columnspan = 3, command = self.placeOrder)
    def placeOrder(self):
        message = ""
        message += self.coneGroup.getSelectedButton()["text"] + "\n\n"
        message += self.iceGroup.getSelectedButton()["text"] + "\n\n"
        message += self.topGroup.getSelectedButton()["text"] + "\n\n"
        self.messageBox(title = "Your Order",
                        message = message)

#to run the window
def main():
    BZ().mainloop()

if __name__ == "__main__":
    main()