import PyQt5.QtWidgets as qtw 

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # For adding Title in MainWindow 
        self.setWindowTitle('My Calculator')
        # For setting a window shape veticale or horizontal we will use QVBoxLayout and QHBoxLayout respectively
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        
        
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
          
        #  Buttons  
        self.result_field = qtw.QLineEdit()
        btn_result   = qtw.QPushButton("Enter", clicked = self.func_result)
        btn_clear    = qtw.QPushButton("Clear", clicked = self.clear_calc)
        
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))      
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))      
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))      
        btn_plus  = qtw.QPushButton('+', clicked = lambda:self.func_press('+')) 
        btn_minus = qtw.QPushButton('_', clicked = lambda:self.func_press('-'))
        btn_mult  = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_divd  = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))
         
    #     #  Adding the buttons to the Layout
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_0,5,0,1,3)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_minus,3,3)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_divd,5,3)
        self.layout().addWidget(container)
        
    def func_result(self):
        expression = self.result_field.text()
        eval(expression)
        result_fin = eval(expression)
        self.result_field.setText(str(result_fin))   
         
        
    def clear_calc(self):
        self.result_field.clear()
    
    def num_press(self, event):
        self.result_field.setText(self.result_field.text() + str(event))

    def func_press(self, event):        
         self.result_field.setText(self.result_field.text() + str(event))
         
             
         
app = qtw.QApplication([])
mw  = MainWindow()
app.exec_()        