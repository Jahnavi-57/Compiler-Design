# Simple Target Code Generator in Python

# Read filename of intermediate code
fname = input("Enter filename of the intermediate code (e.g., input.txt): ")

try:
    with open(fname, "r") as fp1, open("target.txt", "w") as fp2:
        for line in fp1:
            parts = line.strip().split()
            if not parts:
                continue  # skip empty lines
            op = parts[0]

            if op == "print":
                fp2.write(f"OUT {parts[1]}\n")

            elif op == "uminus":
                # Unary minus: uminus var result
                fp2.write(f"LOAD -{parts[1]},R1\nSTORE R1,{parts[2]}\n")

            elif op in "+-*/%":
                # Binary operations: op var1 var2 result
                fp2.write(f"LOAD {parts[1]},R0\nLOAD {parts[2]},R1\n")
                if op == "+": fp2.write("ADD R1,R0\n")
                elif op == "-": fp2.write("SUB R1,R0\n")
                elif op == "*": fp2.write("MUL R1,R0\n")
                elif op == "/": fp2.write("DIV R1,R0\n")
                elif op == "%": fp2.write("MOD R1,R0\n")
                fp2.write(f"STORE R0,{parts[3]}\n")

            elif op == "=":
                # Simple assignment: = var value
                fp2.write(f"STORE {parts[1]},{parts[2]}\n")

            elif op == "[]=":
                # Array assignment: []= array index value
                fp2.write(f"STORE {parts[1]}[{parts[2]}],{parts[3]}\n")

            elif op == "goto":
                # Unconditional jump: goto line label
                fp2.write(f"JMP {parts[1]},label#{parts[2]}\n")

            elif op == ">":
                # Conditional jump if greater: > var value label
                fp2.write(f"LOAD {parts[1]},R0\nJGT {parts[2]},label#{parts[3]}\n")

            elif op == "<":
                # Conditional jump if less: < var value label
                fp2.write(f"LOAD {parts[1]},R0\nJLT {parts[2]},label#{parts[3]}\n")

            else:
                fp2.write(f"# Unknown operation: {line}\n")

    # Print the generated target code
    print("\nGenerated target code:\n")
    with open("target.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print(f"Error: File '{fname}' not found!")
