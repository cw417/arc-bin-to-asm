def parse_binary(num):
  """Parses string binary code and returns string assembly"""
  asm = ''
  op = num[0:2]
  rd = f"%r{int(num[2:7],2)}"
  op3 = num[7:13]
  rs1 = f"%r{int(num[13:18],2)}"
  rs2 = f"%r{int(num[27:],2)}"
  imm = num[18]
  simm13 = int(num[19:], 2)

  print(f"{op} {rd} {op3} {rs1} {imm} {simm13}")
  #rd_asm = "{0:0>5}".format(str(int(rd, 2)))
  rs1_asm = 'hi'

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
        return f"addcc {rs1}, {rs2}, {rd}"
      elif imm == '1':
        return f"addcc {rs1}, {simm13}, {rd}"
    # subcc
    if op3 == '010100':
      if imm == '0':
        return f"subcc {rs1}, {rs2}, {rd}"
      elif imm == '1':
        return f"subcc {rs1}, {simm13}, {rd}"
    #andcc
    #orcc
    #ornc

  # Memory Functions
  elif op == '11':
    # ld
    if op3 == '000000':
      asm += f"ld [{int(simm13, 2)}], %r{int(rd, 2)}"
    # st
    elif op3 == '001000':
      asm = f"st %r{int(rd, 2)}, [{int(simm13, 2)}]"
  

  return asm


def get_info():
  return input('What is the instruction? ')

if __name__ == '__main__':
  test = '10000000101000010010000000000011'
  #info = get_info()
  print(parse_binary(test))
