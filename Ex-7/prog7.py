#M.Jahnavi, CH.EN.U4CSE22033
n = int(input("Enter the Number of Values: "))
ops = []
for i in range(n):
    l = input("left: ")
    r = input("right: ")
    ops.append((l, r))

print("Intermediate Code")
for l, r in ops:
    print(f"{l}={r}")

# Dead Code Elimination
used = set()
for _, r in ops:
    used.update([c for c in r if c.isalpha()])
pr = [(l, r) for l, r in ops if l in used or l == ops[-1][0]]

print("\nAfter Dead Code Elimination")
for l, r in pr:
    print(f"{l}\t={r}")

# Common Subexpression Elimination
seen = {}
opt = []
for l, r in pr:
    if r in seen:
        old = seen[r]
        for i, (x, y) in enumerate(opt):
            opt[i] = (x, y.replace(l, old))
    else:
        seen[r] = l
        opt.append((l, r))

print("Eliminate Common Expression")
for l, r in opt:
    print(f"{l}\t={r}")

print("Optimized Code")
for l, r in opt:
    print(f"{l}={r}")
