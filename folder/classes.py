class codespace:

    def __init__(self, string):
        self.string = string
        
    def codenetra(self):
        return self.string

class_obj = codespace(string="This class is created by the codenetra")
print(f"Running .... {class_obj.codenetra()}")