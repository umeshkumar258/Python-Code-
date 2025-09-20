a = "umesh"
b = 'umesh'
c = '''umesh'''

# all these output is same and all these considere is string


nameshort = a[0:3]  # a[:3] these are same
print(nameshort)

fullname = a[0:6]  # a[0:] these are same
print(fullname)

new = b[:]   # It prints full name 

print(new,type(new))

# sring is immutable it can't be changed
hot = a[:6]
print(type(hot),hot)

d = "ume"
best = a + b
print(best)
