from app.core.machine import BaseMachine


class Form1Transition():
    
    def __init__(self) -> None:
        if not self._machine:
            self._machine = BaseMachine(self)
        return self

