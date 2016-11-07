#outputgen 10-1
n, q = map(int, raw_input().split())
arr = map(int, raw_input().split())
qrr = map(int, raw_input().split())
for q in qrr:
    if q in arr:
        print arr.index(q),
    else:
        print -1,
