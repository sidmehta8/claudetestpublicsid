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
            self.display = "0" if self.display == "0" else self.display
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
