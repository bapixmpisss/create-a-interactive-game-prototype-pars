# 3s0u_create_a_intera.py

import tkinter as tk
from tkinter import messagebox

class GamePrototypeParser:
    def __init__(self, master):
        self.master = master
        master.title("Interactive Game Prototype Parser")
        master.geometry("800x600")

        self.parser_output = tk.Text(master, width=80, height=20)
        self.parser_output.pack(padx=10, pady=10)

        self.input_label = tk.Label(master, text="Enter game script:")
        self.input_label.pack(padx=10, pady=10)

        self.input_field = tk.Text(master, width=80, height=10)
        self.input_field.pack(padx=10, pady=10)

        self.parse_button = tk.Button(master, text="Parse Script", command=self.parse_script)
        self.parse_button.pack(padx=10, pady=10)

    def parse_script(self):
        script = self.input_field.get("1.0", "end-1c")
        try:
            # Simple parser logic, you can replace this with your own parser algorithm
            lines = script.split("\n")
            parsed_script = ""
            for line in lines:
                if line.startswith("say"):
                    parsed_script += line[3:] + "\n"
                elif line.startswith("move"):
                    parsed_script += "Moving to " + line[5:] + "\n"
                else:
                    parsed_script += "Unknown command: " + line + "\n"
            self.parser_output.delete("1.0", "end")
            self.parser_output.insert("1.0", parsed_script)
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
my_gui = GamePrototypeParser(root)
root.mainloop()