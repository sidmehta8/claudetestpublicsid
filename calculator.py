class Calculator:
    def __init__(self):
        self.display = "0"
        self._stored = 0.0
        self._operator = None
        self._new_input = True

    def input_digit(self, digit: str):
        if self._new_input:
            self.display = digit
            self._new_input = False
        else:
            if self.display == "0":
                self.display = digit
            else:
                self.display = self.display + digit

    def input_decimal(self):
        if self._new_input:
            self.display = "0."
            self._new_input = False
        elif "." not in self.display:
            self.display += "."

    def input_operator(self, op: str):
        if self._operator and not self._new_input:
            self._compute()
        self._stored = float(self.display)
        self._operator = op
        self._new_input = True

    def equals(self):
        if self._operator is None:
            return
        self._compute()
        self._operator = None

    def _compute(self):
        try:
            current = float(self.display)
            if self._operator == "+":
                result = self._stored + current
            elif self._operator == "-":
                result = self._stored - current
            elif self._operator == "*":
                result = self._stored * current
            elif self._operator == "/":
                if current == 0:
                    self.display = "Error"
                    self._new_input = True
                    return
                result = self._stored / current
            else:
                return
            self.display = str(int(result)) if result == int(result) else str(result)
            self._new_input = True
        except Exception:
            self.display = "Error"
            self._new_input = True

    def clear(self):
        self.display = "0"
        self._stored = 0.0
        self._operator = None
        self._new_input = True

    def toggle_sign(self):
        if self.display == "Error":
            return
        val = float(self.display)
        val = -val
        self.display = str(int(val)) if val == int(val) else str(val)

    def percent(self):
        if self.display == "Error":
            return
        val = float(self.display) / 100
        self.display = str(int(val)) if val == int(val) else str(val)


import tkinter as tk

DARK_BG = "#1c1c1e"
DISPLAY_BG = "#1c1c1e"
BTN_DIGIT = "#333335"
BTN_FUNC = "#a1a1a3"
BTN_OP = "#ff9f0a"
BTN_ACTIVE = "#ffb340"
TEXT_COLOR = "white"
TEXT_FUNC = "black"


def build_ui(root: tk.Tk, calc: Calculator):
    root.title("Calculator")
    root.configure(bg=DARK_BG)
    root.resizable(False, False)

    display_var = tk.StringVar(value="0")

    def refresh():
        val = calc.display
        display_var.set(val if len(val) <= 12 else val[:11] + "…")

    display = tk.Label(
        root, textvariable=display_var, font=("SF Pro Display", 48, "normal"),
        bg=DISPLAY_BG, fg=TEXT_COLOR, anchor="e", padx=16, pady=8
    )
    display.grid(row=0, column=0, columnspan=4, sticky="ew")

    def make_cmd(fn):
        def cmd():
            fn()
            refresh()
        return cmd

    buttons = [
        ("AC",  BTN_FUNC,  TEXT_FUNC, 1, 0, make_cmd(calc.clear)),
        ("+/-", BTN_FUNC,  TEXT_FUNC, 1, 1, make_cmd(calc.toggle_sign)),
        ("%",   BTN_FUNC,  TEXT_FUNC, 1, 2, make_cmd(calc.percent)),
        ("÷",   BTN_OP,    TEXT_COLOR, 1, 3, make_cmd(lambda: calc.input_operator("/"))),
        ("7",   BTN_DIGIT, TEXT_COLOR, 2, 0, make_cmd(lambda: calc.input_digit("7"))),
        ("8",   BTN_DIGIT, TEXT_COLOR, 2, 1, make_cmd(lambda: calc.input_digit("8"))),
        ("9",   BTN_DIGIT, TEXT_COLOR, 2, 2, make_cmd(lambda: calc.input_digit("9"))),
        ("×",   BTN_OP,    TEXT_COLOR, 2, 3, make_cmd(lambda: calc.input_operator("*"))),
        ("4",   BTN_DIGIT, TEXT_COLOR, 3, 0, make_cmd(lambda: calc.input_digit("4"))),
        ("5",   BTN_DIGIT, TEXT_COLOR, 3, 1, make_cmd(lambda: calc.input_digit("5"))),
        ("6",   BTN_DIGIT, TEXT_COLOR, 3, 2, make_cmd(lambda: calc.input_digit("6"))),
        ("−",   BTN_OP,    TEXT_COLOR, 3, 3, make_cmd(lambda: calc.input_operator("-"))),
        ("1",   BTN_DIGIT, TEXT_COLOR, 4, 0, make_cmd(lambda: calc.input_digit("1"))),
        ("2",   BTN_DIGIT, TEXT_COLOR, 4, 1, make_cmd(lambda: calc.input_digit("2"))),
        ("3",   BTN_DIGIT, TEXT_COLOR, 4, 2, make_cmd(lambda: calc.input_digit("3"))),
        ("+",   BTN_OP,    TEXT_COLOR, 4, 3, make_cmd(lambda: calc.input_operator("+"))),
        (".",   BTN_DIGIT, TEXT_COLOR, 5, 2, make_cmd(calc.input_decimal)),
        ("=",   BTN_OP,    TEXT_COLOR, 5, 3, make_cmd(calc.equals)),
    ]

    for (text, bg, fg, row, col, cmd) in buttons:
        btn = tk.Button(
            root, text=text, font=("SF Pro Display", 22),
            bg=bg, fg=fg, activebackground=BTN_ACTIVE,
            relief="flat", width=4, height=2, command=cmd
        )
        btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    # Zero button spans 2 columns
    zero_btn = tk.Button(
        root, text="0", font=("SF Pro Display", 22),
        bg=BTN_DIGIT, fg=TEXT_COLOR, activebackground=BTN_ACTIVE,
        relief="flat", height=2, command=make_cmd(lambda: calc.input_digit("0"))
    )
    zero_btn.grid(row=5, column=0, columnspan=2, padx=1, pady=1, sticky="nsew")

    for col in range(4):
        root.columnconfigure(col, weight=1, minsize=72)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator()
    build_ui(root, calc)
    root.mainloop()
