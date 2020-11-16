
weight= input("Whats your weight? ")
unit= input("(L)bs or (K)g: ")
if unit.upper()=='L':
  converted= float(weight)*0.45
  print(f"you are {converted} kilos")
else:
    converted= float(weight)/0.45
    print(f"you are {converted} pounds")
