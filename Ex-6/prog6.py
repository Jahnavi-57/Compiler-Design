expr=input("Enter Expression:\n")
ops=['+','-','*','/']
tmp=ord('Z')
print("Intermediate Code:")
for op in ops:
    while op in expr:
        p=expr.index(op)
        i=p-1
        while i>=0 and expr[i] in ops+['=','$']:i-=1
        l=expr[i]
        j=p+1
        while j<len(expr) and expr[j] in ops+['=','$']:j+=1
        r=expr[j]
        print(f"{chr(tmp)}:{l}{op}{r}")
        expr=expr[:i]+chr(tmp)+expr[j+1:]
        tmp-=1
if '=' in expr:
    l,r=expr.split('=')
    print(f"{r}:{l}")
else:
    print(f"Result: {expr}")