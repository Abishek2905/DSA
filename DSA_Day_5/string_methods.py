import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits) 
print(string.punctuation)
print(string.whitespace)


s = "Hello World"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())

s2 = " Hello "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())

s2 = s.split()
print(s2)
s2 = s.split('l')
print(s2)

s2 = s.replace("world", "Python")
print(s2)

print(s.find("World"))
print(s.find("Python"))

print(s.index("World"))

print(s.startswith("Hello"))
print(s.endswith("Hello"))

print(s.count('l'))

print('xyz'.isalpha())
print('xyz'.isdigit())
print('xyz123'.isalnum())

s3 = "Hello"
print(s3[1:4])
print(s3[:2])
print(s3[1:])
print(s3[::-1])
print(s3[::2])

