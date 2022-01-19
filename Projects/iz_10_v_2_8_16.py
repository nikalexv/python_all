def trans_10_to_base(num, base=2):
    res = ''
    while num:
        num, d = divmod(num, base)
        sd = str(d) if d < 10 else str(chr(ord('A')+d-10))
        res = sd + res
    return res

print(trans_10_to_base(513))

