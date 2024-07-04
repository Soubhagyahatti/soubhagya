import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        frame.pack(side=tk.TOP)
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=0, bg="#eee", justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '=',
            '0', '.', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            if button == "=":
                btn = tk.Button(self.buttons_frame, text=button, fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click_button("="))
            else:
                btn = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda x=button: self.click_button(x))
            
            btn.grid(row=row_val, column=col_val, padx=1, pady=1)

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click_button(self, item):
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == '←':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


