
class fraction:
    def __init__(self,n1,d1,n2,d2):
        self.f_numerator = n1 #صورت
        self.f_denominator = d1 #مخرج
        self.s_numerator = n2
        self.s_denominator = d2
    def add (self):
        a = (self.f_numerator*self.s_denominator)+(self.f_denominator*self.s_numerator)
        b=  self.f_denominator*self.s_denominator
        print ("Javabe Jam do kadr hast:",a,"/",b)
    def sub (self):
        a = (self.f_numerator*self.s_denominator)-(self.f_denominator*self.s_numerator)
        b=  self.f_denominator*self.s_denominator
        print ("Javabe Tafrigh do kadr hast:",a,"/",b)
    def mul (self):
        a = self.f_numerator*self.s_numerator
        b=  self.f_denominator*self.s_denominator
        print ("Javabe zarbe do kadr hast:",a,"/",b)
    def div (self):
        a = self.f_numerator*self.s_denominator
        b=  self.f_denominator*self.s_numerator
        print ("Javabe zarbe do kadr hast:",a,"/",b)
    def show (self):
        def show(self):
        while(True):
            if self.numerator % 2 == 0 and self.denominator % 2 == 0:
                self.numerator = self.numerator/2
                self.denominator =   self.denominator/ 2

            elif self.numerator % 3 == 0 and self.denominator % 3 == 0:
                self.numerator = self.numerator/ 3
                self.denominator =   self.denominator/  3

            elif self.numerator % 5 == 0 and self.denominator % 5 == 0:
                self.numerator = self.numerator/ 5
                self.denominator =   self.denominator/  5

            elif self.numerator % 7 == 0 and self.denominator % 7 == 0:
                self.numerator = self.numerator/ 7
                self.denominator =   self.denominator/  7
            
            else:
                break

nemooneh = fraction (4,2,3,2)#صورت و مخرج اول، صورت و مخرج دوم
nemooneh.add()
nemooneh.sub()
nemooneh.mul()
nemooneh.div()
