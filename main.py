import time


generation = 10
axiom = 'A'
char_1, rule_1 = 'A', 'AB'
char_2, rule_2 = 'B', 'A'


def apply_rules(axiom):
    res = ''
    for char in axiom:
        if char == char_1:
            res += rule_1
        else:
            res += rule_2

    return res

for gen in range(1, generation+1):
    print(f'generation: {gen}: {axiom}')
    time.sleep(1)
    axiom = apply_rules(axiom)