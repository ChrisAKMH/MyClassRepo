print("ASKHSH 1")
class UpperString:
    def get_String(self, abc):
        self.abc = abc
        self.abc = input("Write something: ")
        return self.abc
    def print_String(self, abc):
        self.abc = abc
        textUpper = self.abc.upper()
        print(textUpper)
x = UpperString()
y = x.get_String("")
x.print_String(y)