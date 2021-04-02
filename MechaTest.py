from tkinter import *
import Archivo as leer
import datetime

def main():

    #Clase principal de la aplicacion
    class Application(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.grid()
            master.columnconfigure(0, weight = 1)
            master.rowconfigure(0, weight = 1)
            self.Inicio()
            master.title("MechaTest")
    
        #Funcion principal para instansear todos los elementos y variables globales
        def Inicio(self):

            self.IniciarVariables()

            


            #Set text Panel for text
            self.textPanel = Text(self, height = 7, width = 60, bd = 5, wrap = WORD)
            self.textPanel.insert(END, self.lista, 'color')
            self.textPanel.config(font=("Serif", 20, "italic"))
            self.textPanel.grid(row = 0, column = 0, columnspan = 4)

            #Set scoreBoardKeyStrokes
            self.scoreKeyStrokesLabel = Label(self, height = 7, width = 15, bd = 1)
            self.scoreKeyStrokesLabel.grid(row = 1, column = 0, sticky = W)
            
            #Set scoreBoardWords
            self.scoreWordsLabel = Label(self, height = 7, width = 15, bd = 1)
            self.scoreWordsLabel.grid(row = 1, column = 1, sticky = W)

            #Set scoreBoardErrors
            self.scoreErrorLabel = Label(self, height = 7, width = 60, bd = 1)
            self.scoreErrorLabel.grid(row = 1, column = 2, columnspan = 4, sticky = W)

            #Set entry widget
            self.textEntry = Entry (self, textvariable = self.mi_variable, width = 15)
            self.textEntry.config(font = ("Serif", 30, "italic"))
            self.textEntry.grid(row = 2, column = 0, columnspan = 5, pady = 15)

            #Set end program Button
            self.endButton = Button(self, height = 3, width = 5)
            self.endButton.config(font = ("Serif", 12, "italic"))
            self.endButton['text'] = "Salir"
            self.endButton["command"] = self.master.destroy
            self.endButton.grid(row = 4, column = 3, sticky = E)
           
            #set reset Button
            self.resetButton = Button(self, height = 3, width = 5)
            self.resetButton.config(font = ("Serif", 12, "italic"))
            self.resetButton['text'] = "Reset"
            self.resetButton["command"] = self.reset
            self.resetButton.grid(row = 4, column = 0, sticky = W)
            

        
        def IniciarVariables(self):
            self.lista = []
            self.lista = leer.LeerArchivo()
            #print(self.lista)

            self.auxList = self.lista.copy()
            self.variableInico = 0
            self.primerSpace = False
            self.getCoordinates = 0
            self.testInicio = "1.0"
            self.testFinal = "1" + "." + str(len(self.auxList[0]))

            self.mi_variable = StringVar()
            self.mi_variable.trace_add('write', self.my_callback)
            
            self.rightWords = 0
            self.wrongWords = 0


        def my_callback(self, var, indx, mode):
            self.pattern = self.mi_variable.get()
            #self.setScore()           
            #verifica que la lista sea diferente a null
            
            bandCheckList = self.checkList()
            if bandCheckList:
                
                if self.auxList[0].startswith(self.pattern):
                    print("doing nice")
                    self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                    self.textPanel.tag_config(self.pattern, foreground = "white")
        
                else:
                    self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                    self.textPanel.tag_config(self.pattern, foreground = "red")

                print(self.pattern)

                if " " in self.pattern:
                    self.CompareKeyStrokes()


            
            else:
                print("Done...")
        
            self.setScore()


        def CompareKeyStrokes(self):
            if self.auxList[0] == self.pattern[:-1]:
                print("Bien escrio")
                self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                self.textPanel.tag_config(self.pattern, foreground = "green")
                self.rightWords += 1
            else:
                self.textPanel.tag_add(self.pattern, self.testInicio, self.testFinal)
                self.textPanel.tag_config(self.pattern, foreground = "red")
                self.wrongWords += 1

            self.mi_variable.set('')
            self.Avanza()


        def setScore(self):
            if len(self.auxList) == 1 and "." in self.pattern:
                print("ultima frase y termino :]")
                print(self.auxList[0])

                if self.auxList[0] == self.pattern:
                    print("Bien escrio")
                    self.textPanel.tag_add(self.pattern, self.testInicio, END)
                    self.textPanel.tag_config(self.pattern, foreground = "green")
                    self.rightWords += 1
                else:
                    self.textPanel.tag_add(self.pattern, self.testInicio, END)
                    self.textPanel.tag_config(self.pattern, foreground = "red")
                    self.wrongWords += 1

                print("Palabras correctas", self.rightWords)
                print("Palabras incorrectas", self.wrongWords)

                self.scoreWordsLabel['text'] = "Correct Words: \n",str(self.rightWords)
                self.scoreErrorLabel['text'] = "Wrong words: \n",str(self.wrongWords)

        def Avanza(self):
            self.getCoordinates += len(self.auxList[0]) + 1
            
            del self.auxList[0]

            if self.auxList:
                self.testInicio = "1" + "." + str(self.getCoordinates)
                self.auxiliar = len(self.auxList[0]) + 1
                calc = (self.getCoordinates) + self.auxiliar
                self.testFinal = "1" + "." + str(calc - 1)
                self.primerSpace = True
            else:
                print("List empy... Done...") 

        def checkList(self):
            if self.auxList:
                return True
            else:
                return False

        def reset(self):
            self.IniciarVariables()
            self.Inicio()
            self.textPanel.delete("1.0",END)
            self.textPanel.insert(END, self.lista, 'color')


    """
    Inicio de toda la instancia general
    """
    root = Tk()
    #root.geometry("1000x600")
    app = Application(master = root)
    app.mainloop()
    
if __name__ == '__main__':
    main()
    


