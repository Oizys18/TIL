""" This is an AREA CALCULATOR """

print('The program is now ON')
option = input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C' or 'CIRCLE':
  #Calculating Circle Area
  print("Circle calculation")
  radius = float(input("Enter radius: "))
  area = 3.14159 * (radius**2)
  
  print(str(area))

elif option == 'T' or 'TRIANGLE':
  #Calculating Triangle Area
  print('Triangle Calculation')
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = 0.5 * base * height

  print(str(area))

else: 
  print("Wrong input, Please enter either C or T")
    
print("The program is now OFF, Restart for another Calculation")




