expr = input("Enter expression ending with $: ")
expr = expr.strip('$')

print("\nSymbol\tType")
for ch in expr:
    if ch.isalpha():
        print(f"{ch}\tIdentifier")
    elif ch in "+-*/=":
        print(f"{ch}\tOperator")
