
a = 176

b = 219

print(chr(b),chr(a),chr(a),chr(a),chr(b))

print (chr(a),chr(b),chr(a),chr(b),chr(a))

print (chr(a),chr(a),chr(b),chr(a),chr(a))

print (chr(a),chr(b),chr(a),chr(b),chr(a))

print (chr(b),chr(a),chr(a),chr(a),chr(b))

l = []

for i in range(3):
    temp = int(input())
    l.append(temp)

l.sort()
print(l)