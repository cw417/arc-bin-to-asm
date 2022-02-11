def parse_binary(num):
  """Parses string binary code and returns string assembly"""
  op = num[0:2]
  rd = f"%r{int(num[2:7],2)}"
  op3 = num[7:13]
  rs1 = f"%r{int(num[13:18],2)}"
  rs2 = f"%r{int(num[27:],2)}"
  imm = num[18]
  simm13 = int(num[19:], 2)

  imm_0 = f" {rs1}, {rs2}, {rd}"
  imm_1 = f" {rs1}, {simm13}, {rd}"

  #print(f"{op} {rd} {op3} {rs1} {imm} {simm13}")

  # Branch functions
  if op == '00':
    # Need to figure out how to deal with labels
    pass

  # Call functions
  elif op == '01':
    # will add call later
    pass

  # Arithmetic functions
  elif op == '10':
    # addcc
    if op3 == '010000':
      if imm == '0':
        return "addcc" + imm_0
      elif imm == '1':
        return "addcc" + imm_1
    # subcc
    if op3 == '010100':
      if imm == '0':
        return "subcc" + imm_0
      elif imm == '1':
        return "subcc" + imm_1
    #andcc
    if op3 == '010001':
      return "andcc" + imm_0
    #orcc
    if op3 == '010010':
      return "orcc" +imm_0
    #ornc
    if op3 == '010110':
      return "orncc" + imm_0
    # srl
    if op3 == '100110':
      if imm == '0':
        return "srl" + imm_0
      elif imm == '1':
        return "srl" + imm_1

  # Memory Functions
  elif op == '11':
    # ld
    if op3 == '000000':
      return f"ld [{simm13}], {rd}"
    # st
    elif op3 == '001000':
      return f"st {rd}, [{simm13}]"
  
def get_info():
  return input('What is the instruction? ')

if __name__ == '__main__':
  test = '11000010000000000010101110111000'.replace(" ", "")
  #info = get_info()
  #print(parse_binary(info))
  print(parse_binary(test))
