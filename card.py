class Card:
    def __init__(self, color, icon, stick):
        self.color = color
        self.value = 0  
        self.icon = icon
        self.stick = stick
        self.visibility = True

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value

    def getIcon(self):
        return self.icon
    def setIcon(self, icon):
        self.icon = icon

    def getStick(self):
        return self.stick
    def setStick(self, stick):
        self.stick = stick
        
    def setVisibility(self, visibility):
        self.visibility = visibility
    def getVisibility(self):
        return self.visibility 
        
    def getCard(self):
        if self.color == "red":
            redIcon =  "\033[91m{}\033[0m".format(self.icon)
            redValue = "\033[91m{}\033[0m".format(self.value)
            if self.visibility == True:
                card = ("[{}|{}]".format(redIcon, redValue))
            elif self.visibility == False:
                card = ("\033[91m[*|*]\033[0m")
                
        else:
            blueIcon =  "\033[94m{}\033[0m".format(self.icon)
            blueValue = "\033[94m{}\033[0m".format(self.value)  
            if self.visibility == True:
                card = ("[{}|{}]".format(blueIcon, blueValue))
            elif self.visibility == False:
                card = ("\033[94m[*|*]\033[0m")
            
        return card
    
        
  


            