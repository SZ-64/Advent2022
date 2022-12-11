import Utils
from Classes.Monkey import Monkey
from Classes.Monkey import Operations


monkeys = []

def parse_monkeys():
    lines = Utils.read_file_as_lines("Input\\11-12-22.txt")
    monkey_data_blocks = Utils.seek_until_blank_line(lines)
    for item in monkey_data_blocks:
        op = get_op(item[2][19:].split(" "))
        new_monkey = Monkey(
            int(item[0][7:][:1]),
            [int(n) for n in item[1][18:].split(',')],
            op[0],
            int(op[1]),
            int(item[3][21:]),
            int(item[4][29:]),
            int(item[5][30:])
        )
        #print(str(new_monkey))
        monkeys.append(new_monkey)


def get_op(op_tokens):
    match op_tokens[1]:
        case '+':
            return (Operations.ADD, op_tokens[2])
        case '*':
            if op_tokens[2].isdigit():
                return (Operations.MULT, op_tokens[2])
            else:
                return (Operations.MULT, 0)


def get_monkey_by_id(id):
    print(f"Looking for {id}")
    for monkey in monkeys:
        print(str(monkey))
        if monkey.id == id:
            return monkey


def part_one():
    for monkey in monkeys:
        
        while len(monkey.items) > 0:
            value = monkey.inspect_item(0)
            print(f"Inspected item {value}")
            value = monkey.apply_worry(value)
            print(f"Worried: {value}")
            value = monkey.apply_relief(value)
            print(f"Relieved: {value}")
            target = monkey.test_worry_level(value)
            print(f"Toss to monkey_true: {target}")
            get_monkey_by_id(target).items.append(value)
            print(f"Monkey {target} added item {value}")
    
    for m in monkeys:
        print(f"Monkey {m.id} has {m.items}")


def part_two():
    pass
        

def main():
    parse_monkeys()
    part_one()
    part_two()


if __name__ == '__main__':
    main()
