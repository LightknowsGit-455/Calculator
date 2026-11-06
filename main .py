import customtkinter as ctk

l=[["C", "^", "←", "÷"], ["7", "8", "9", "×"], ["4", "5", "6", "-"], ["1", "2", "3", "+"], ["%", "0", ".", "="]]

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("450x600")
        self.configure(bg="white")
        self.resizable(False, False)
        self.entry = ctk.CTkEntry(self, width=500, height=100, font=("Arial", 52), justify="right", state="readonly")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.result_displayed = False

        # Configure grid weights
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)



        # Create buttons
        for i in range(5):
            for j in range(4):
                if l[i][j]=="=":
                    self.create_button(l[i][j], i + 1, j, "red", "darkred")
                elif l[i][j] in ["+", "-", "×", "÷", "^", "C", "←"]:
                    self.create_button(l[i][j], i + 1, j, "gray", "darkgray")
                else:
                    self.create_button(l[i][j], i + 1, j, "lightgray", "gray")
        


    #A function to create buttons
    def create_button(self, text, row, column, fg_color, hover_color):
        button = ctk.CTkButton(self, text=text, command=lambda: self.button_click(text), font=("Arial", 54), fg_color=fg_color, hover_color=hover_color, corner_radius=0, text_color="black", border_width=1, border_color="black")

        button.grid(row=row, column=column, sticky="nsew")


    #A function to handle button clicks
    def button_click(self, text):
        self.entry.configure(state="normal")

        if self.result_displayed and text not in ["+", "-", "×", "÷", "="]:
            self.entry.delete(0, ctk.END)
            self.result_displayed = False

        try:
            self.entry.configure(state="normal")
            if text == "C":
                self.entry.delete(0, ctk.END)

            elif text == "=":    
                expression = self.entry.get().replace("×", "*").replace ("÷", "/").replace("^", "**")
                if expression.endswith("%"):
                    expression = expression[:-1] + "/100"
                else:
                    expression = expression.replace("%", "/100*")
                result = eval(expression)
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, str(result))
                self.result_displayed = True

            elif text == "%":
                current_text = self.entry.get()
                if current_text and not current_text.endswith("%"):
                    self.entry.insert(ctk.END, "%")
                    self.result_displayed = False



            elif text in ["+", "-", "×", "÷", "^"]:

                current_text = self.entry.get()

                operators = ["+", "-", "×", "÷", "^"]

                if any(current_text.endswith(op) for op in operators):

                    new_text = current_text[:-3]

                    self.entry.delete(0, ctk.END)
                    self.entry.insert(0, new_text + f" {text} ")
                    self.result_displayed = False

                else:
                    self.entry.insert(ctk.END, f" {text} ")
                    self.result_displayed = False

            elif text == "←":
                current_text = self.entry.get()
                if current_text.endswith(" "):
                    new_text = current_text[:-3]
                else:
                    new_text = current_text[:-1]
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, new_text)
                self.result_displayed = False

            else:
                self.entry.insert(ctk.END, text)
                self.result_displayed = False

            self.entry.configure(state="readonly")

        except Exception as e:
            self.entry.configure(state="normal")
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, "Error")
            self.entry.configure(state="readonly")
            self.result_displayed = True

        


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

