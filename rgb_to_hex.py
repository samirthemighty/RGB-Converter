# RGB converter

print('Welcome to our Converter Application!\n')
user = int(input('Enter 1 if youd like to convevrt RGB to Hex\nEnter 2 if youd like to convert Hex to RGB\n'))
def convert(user):
  RGB = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
  if user == 1:
    final_hex = ''
    
    red = int(input('Enter how much red (first number): '))
    green = int(input('\nEnter how much green (first number): '))
    blue = int(input('\nEnter how much blue (first number): '))
    first_red = red//16
    
    second_red = RGB[int((red/16 - first_red)*16)]
    first_red = RGB[first_red]
    
    
    first_green = green//16
    second_green = RGB[int((green/16 - first_green)*16)]
    first_green = RGB[first_green]

    first_blue = blue//16
    second_blue = RGB[int((blue/16 - first_blue)*16)]
    first_blue = RGB[first_blue]

    final_hex += '\nFINAL HEX: #'+ str(first_red) + str(second_red) + str(first_green) + str(second_green) + str(first_blue) + str(second_blue)
    return final_hex
  if user == 2:
    hex = input('\nEnter your Hex value: ')
    if '#' in hex:
      hex = hex.replace('#','')
    hex1 = hex.upper()
    
    first_red = hex1[0]
    second_red = hex1[1]
    
    for i in range(0,16):
      if RGB[i] == first_red:
        first_red = i
    for i in range(0,16):
      if RGB[i] == second_red:
        second_red = i
    red  = int(first_red)*16 + int(second_red)

    
    first_green = hex1[2]
    second_green= hex1[3]
    
    for i in range(0,16):
      if RGB[i] == first_green:
        first_green = i
    for i in range(0,16):
      if RGB[i] == second_green:
        second_green = i
    green = int(first_green)*16 + int(second_green)
        
    
    first_blue = hex1[4]
    second_blue = hex1[5]
    
    for i in range(0,16):
      if RGB[i] == first_blue:
        first_blue = i
    for i in range(0,16):
      if RGB[i] == second_blue:
        second_blue = i
    blue = int(first_blue)*16 + int(second_blue)

    final_hex = f'\nYour hex: #{hex}'
    final_string = f'Your hex converted is: rgb({red},{green},{blue})'
    print(final_hex)
    return final_string
    
print(convert(user))
