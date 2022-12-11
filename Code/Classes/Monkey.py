from enum import Enum

import math


class Operations(Enum):
    ADD = "+"
    MULT = "*"
    SQUARE = "^2"

class Monkey:
    
    def __init__(self, id, items, op, constant, test, monkey_true, monkey_false) -> None:
        self.id = id
        self.items = items
        self.op = op
        self.constant = constant
        self.test = test
        self.moneky_true = monkey_true
        self.monkey_false = monkey_false
        self.inspection_count = 0
    
    def __str__(self) -> str:
        return f"Monkey {self.id}:\n\tItems: {self.items}\n\tOp: new = old {self.op.value} {self.constant}\n\tTest: divisible by {self.test}\n\tIf true: throw to monkey {self.moneky_true}\n\tIf false: throw to monkey {self.monkey_false}"
    
    def __repr__(self) -> str:
        return f"Monkey {self.id}:\n\tItems: {self.items}\n\tOp: new = old {self.op.value} {self.constant}\n\tTest: divisible by {self.test}\n\tIf true: throw to monkey {self.moneky_true}\n\tIf false: throw to monkey {self.monkey_false}"

    def inspect_item(self, item_index):
        self.inspection_count += 1
        return self.items.pop(item_index)

    def apply_worry(self, value):
        worry_value = 0
        match self.op:
            case Operations.ADD:
                worry_value = value + self.constant
            case Operations.MULT:
                worry_value = value * self.constant
            case Operations.SQUARE:
                worry_value = value * value
        return worry_value
    
    def apply_relief(self, value):
        return math.floor(value / 3)
    
    def test_worry_level(self, value):
        if value % self.test == 0:
            return self.moneky_true
        else:
            return self.monkey_false