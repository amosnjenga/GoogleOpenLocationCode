from openlocationcode import openlocationcode


#Get Plus Code
address_code = openlocationcode.encode(-1.109804,36.634250)
print(address_code)

#Get Coordinates from Plus code
coords = openlocationcode.decode(address_code)
print(coords)

#trim the first characters from a code
shortened_code = openlocationcode.shorten(address_code,-1.109804,36.634250)
print(shortened_code)