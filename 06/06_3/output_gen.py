#output generator for 06_3

raw_input()
x = map(int, raw_input().split())
y = map(int, raw_input().split())
for v in sorted(x + y):
    print v,
