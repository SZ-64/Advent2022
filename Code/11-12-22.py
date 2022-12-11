import Utils
import sys
from Classes.Monkey import Monkey
from Classes.Monkey import Operations


sys.set_int_max_str_digits(0)

rounds_one = 20
rounds_two = 10000
monkeys = []

def reset():
    monkeys.clear()

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
        monkeys.append(new_monkey)


def get_op(op_tokens):
    match op_tokens[1]:
        case '+':
            return (Operations.ADD, op_tokens[2])
        case '*':
            if op_tokens[2].isdigit():
                return (Operations.MULT, op_tokens[2])
            else:
                return (Operations.SQUARE, 0)


def get_monkey_by_id(id):
    for monkey in monkeys:
        if monkey.id == id:
            return monkey


def part_one():
    for _ in range(rounds_one):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                value = monkey.inspect_item(0)
                value = monkey.apply_worry(value)
                value = monkey.apply_relief(value)
                target = monkey.test_worry_level(value)
                get_monkey_by_id(target).items.append(value)
    
    inspection_map = {}
    for m in monkeys:
        inspection_map[m.id] = m.inspection_count
    
    print(sorted(list(inspection_map.values()), reverse=True))



def part_two():
    factor = 1
    for monkey in monkeys:
        factor *= monkey.test

    for counter in range(rounds_two):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                value = monkey.inspect_item(0)
                value %= factor
                value = monkey.apply_worry(value)
                target = monkey.test_worry_level(value)
                get_monkey_by_id(target).items.append(value)
    
    inspection_map = {}
    for m in monkeys:
        inspection_map[m.id] = m.inspection_count
    
    print(sorted(list(inspection_map.values()), reverse=True))
        

def main():
    parse_monkeys()
    part_one()
    reset()
    parse_monkeys()
    part_two()


if __name__ == '__main__':
    main()
