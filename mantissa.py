def mantissa(num,exp):
  """
  Takes in float number and integer exponent.
  Returns formatted IEEE-754 single precision floating point binary number.
  """

  # excess-127
  exp = int(exp) + 127

  # binary sections
  sign = 1 if (float(num) < 0) else 0
  exponent = bin(exp).replace("0b", "").zfill(8)
  fraction = str(num).strip("-+")[2:].ljust(23,'0')
  #fraction = fraction[2:].ljust(23,'0')
  #print(fraction)
  return f"{sign}  {exponent[0:4]} {exponent[4:]}  {fraction[0:3]} {fraction[3:7]} {fraction[7:11]} {fraction[11:15]} {fraction[15:19]} {fraction[19:]}"
  pass

def get_nums():
  """Get and return number and exponent input."""
  # Work in progress
  num = input("What is the number? ")
  exp = input("What is the exponent? ")
  if 'q' not in [num, exp]:
    #try:
    if int(exp) >= -126 and int(exp) <= 127:
      print("ok")
      print(float(num), int(exp))
      return float(num), int(exp)
    else:
      print("That is not a valid exponent")
      return 0, 0
  else:
    return ['q', 0]
  #except:
  #  print("error")
  #  return 0, 0
  

if __name__ == '__main__':
  print("Please enter a number and then exponent for the conversion.")
  print("Please include sign and decimal when entering.")
  print("You will enter the expoenent separately from the number.")
  print("Enter 'q' to exit.")
  num = (input("What is the number? "))
  exp = input("What is the exponent? ")
  while num != 'q' or exp != 'q':
    print(mantissa(num,exp))
    num = input("What is the number? ")
    exp = input("What is the exponent? ")
  # nums = get_nums()
  # while 'q' not in nums:
  # print(mantissa(nums[0], nums[1]))
  # nums = get_nums()