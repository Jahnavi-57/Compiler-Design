#CH.EN.U4CSE22033,M.Jahnavi
# LL(1) Parser in Python

# Parsing table (like in C code)
# Grammar:
# e -> t b
# b -> + t b | ε
# t -> f c
# c -> * f c | ε
# f -> i | ( e )

table = {
    ("e", "i"):  "tb",
    ("e", "("): "tb",

    ("b", "+"): "+tb",
    ("b", ")"): "n",
    ("b", "$"): "n",

    ("t", "i"): "fc",
    ("t", "("): "fc",

    ("c", "+"): "n",
    ("c", "*"): "*fc",
    ("c", ")"): "n",
    ("c", "$"): "n",

    ("f", "i"): "i",
    ("f", "("): "(e)"
}

def parse(input_str):
    # Add end marker
    input_str += "$"
    stack = ["$", "e"]
    i = 0

    print("Stack\tInput")
    print("-----\t-----")

    while stack:
        print("".join(stack), "\t", input_str[i:])

        top = stack.pop()
        curr = input_str[i]

        if top == curr:        # match
            i += 1
        elif top == "n":       # epsilon
            continue
        elif (top, curr) in table:
            prod = table[(top, curr)]
            for symbol in reversed(prod):
                stack.append(symbol)
        else:
            print("ERROR")
            return
    print("SUCCESS")

# Example usage
expr = "i+i*i"   # input string (id = 'i')
parse(expr)
