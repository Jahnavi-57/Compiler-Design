def eliminate_left_recursion(g):
    ng = {}
    for nt, prods in g.items():
        alpha, beta = [], []
        for p in prods:
            (alpha if p[0] == nt else beta).append(p[1:] if p[0] == nt else p)
        if alpha:
            ntp = nt + "'"
            ng[nt] = [b + [ntp] for b in beta]
            ng[ntp] = [a + [ntp] for a in alpha] + [["ε"]]
        else:
            ng[nt] = prods
    return ng

def left_factoring(g):
    changed = True
    while changed:
        changed, ng = False, {}
        for nt, prods in g.items():
            pref = {}
            for p in prods: pref.setdefault(p[0], []).append(p)
            if any(len(v) > 1 for v in pref.values()):
                changed = True; ntp = nt + "'"; ng[nt] = []
                for k, v in pref.items():
                    if len(v) > 1:
                        ng[nt].append([k, ntp])
                        ng[ntp] = [p[1:] or ["ε"] for p in v]
                    else: ng[nt].append(v[0])
            else: ng[nt] = prods
        g = ng
    return g

def show(g):
    for nt, p in g.items():
        print(nt, "->", " | ".join(" ".join(x) for x in p))

# Example
grammar = {
    "E": [["E", "+", "T"], ["T"]],
    "T": [["T", "*", "F"], ["F"]],
    "F": [["(", "E", ")"], ["id"]]
}

print("Original:"); show(grammar)
grammar = eliminate_left_recursion(grammar)
print("\nNo Left Recursion:"); show(grammar)
grammar = left_factoring(grammar)
print("\nAfter Left Factoring:"); show(grammar)
