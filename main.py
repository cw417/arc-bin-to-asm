def parse_binary(num):
  """
  Parses binary or assembly code for ARC. Returns string assembly.
  
  @param {String} num  32-bit binary number, or ARC assembly code.
  @return {String}     Assembly instruction if given binary, and binary if given assembly.

  """

  # strip spaces
  num = num.replace(" ", "")

  # define instruction part intervals
  op = num[0:2]
  cond = num[3:7]
  rd = f"%r{int(num[2:7],2)}"
  op2 = num[7:10]
  op3 = num[7:13]
  rs1 = f"%r{int(num[13:18],2)}"
  rs2 = f"%r{int(num[27:],2)}"
  imm = num[18]
  imm22 = int(num[11:], 2)
  simm13 = int(num[19:], 2)
  disp30 = int(num[2:], 2)

  # format register output based on immediate
  imm_0 = f" {rs1}, {rs2}, {rd}"
  imm_1 = f" {rs1}, {simm13}, {rd}"

  # Branch functions
  if op == "00":
    # branch
    if op2 == "010":
      if cond == "0001":
         b_type = "be"
      elif cond== "0101":
        b_type = "bcs"
      elif cond == "0110":
        b_type = "bneg"
      elif cond == "0111":
        b_type = "bvs"
      elif cond == "1000":
        b_type = "ba"
      return f"{b_type} {imm22}"
    # sethi
    if op2 == "100":
      return f"sethi {imm22}, {rd}"

  # Call functions
  elif op == "01":
    # call
    return f"call {disp30}"

  # Arithmetic functions
  elif op == "10":
    # addcc
    if op3 == "010000":
      return "addcc" + imm_0 if imm == "0" else "addcc" + imm_1
    # subcc
    if op3 == "010100":
      return "subcc" + imm_0 if imm == "0" else "subcc" + imm_1
    #andcc
    if op3 == "010001":
      return "andcc" + imm_0
    #orcc
    if op3 == "010010":
      return "orcc" + imm_0
    #ornc
    if op3 == "010110":
      return "orncc" + imm_0
    # srl
    if op3 == "100110":
        return "srl" + imm_0 if imm == "0" else "srl" + imm_1
    if op3 == "111000":
      return f"jmpl {rs1}+{simm13}, {rd}"

  # Memory Functions
  elif op == "11":
    # ld
    if op3 == "000000":
      return f"ld {simm13}, {rd}"
    # st
    elif op3 == "000100":
      return f"st {rd}, {simm13}"
  
def parse_asm(asm):
  """Takes in string ARC assembly instruction, returns string binary equivalent"""
  # TODO:
  #  - Fix immediate parts of if loop
  binary_string = ""
  asm_array = asm.lower().split(" ")

  # Branch
  if asm_array[0] == "be":
    pass
  if asm_array[0] == "bcs":
    pass
  if asm_array[0] == "bneg":
    pass
  if asm_array[0] == "bvs":
    pass
  if asm_array[0] == "ba":
    pass

  # Arithmetic
  if asm_array[0] == "addcc":
    op = "10"
    op3 = "010000"
    rd = bin(int(asm_array[3].strip("%r,"))).replace("0b", "").zfill(5)
    rs1 = bin(int(asm_array[1].strip("%r,"))).replace("0b", "").zfill(5)
    if "%" not in asm_array[2]:
    # immediate
      imm = bin(int(asm_array[2].strip(","))).replace("0b", "").zfill(13)
      return f"{op} {rd} {op3} {rs1} 1 {imm}"
    else:
    # not immediate
      rs2 = bin(int(asm_array[2].strip("%r,"))).replace("0b", "").zfill(5)
      return f"{op} {rd} {op3} {rs1} 0 00000000 {rs2}"
  
  if asm_array[0] == "subcc":
    op = "10"
    op3 = "010100"
    rd = bin(int(asm_array[3].strip("%r,"))).replace("0b", "").zfill(5)
    rs1 = bin(int(asm_array[1].strip("%r,"))).replace("0b", "").zfill(5)
    if "%" not in asm_array[2]:
    # immediate
      imm = bin(int(asm_array[2].strip(","))).replace("0b", "").zfill(13)
      return f"{op} {rd} {op3} {rs1} 1 {imm}"
    else:
    # not immediate
      rs2 = bin(int(asm_array[2].strip("%r,"))).replace("0b", "").zfill(5)
      return f"{op} {rd} {op3} {rs1} 0 00000000 {rs2}"
  
  if asm_array[0] == "orcc":
    op = "10"
    op3 = "010010"
    rd = bin(int(asm_array[3].strip("%r,"))).replace("0b", "").zfill(5)
    rs1 = bin(int(asm_array[1].strip("%r,"))).replace("0b", "").zfill(5)
    if "%" not in asm_array[2]:
    # immediate
      imm = bin(int(asm_array[2].strip(","))).replace("0b", "").zfill(13)
      return f"{op} {rd} {op3} {rs1} 1 {imm}"
    else:
    # not immediate
      rs2 = bin(int(asm_array[2].strip("%r,"))).replace("0b", "").zfill(5)
      return f"{op} {rd} {op3} {rs1} 0 00000000 {rs2}"
  
  if asm_array[0] == "andcc":
    op = "10"
    op3 = "010001"
    rd = bin(int(asm_array[3].strip("%r,"))).replace("0b", "").zfill(5)
    rs1 = bin(int(asm_array[1].strip("%r,"))).replace("0b", "").zfill(5)
    if "%" not in asm_array[2]:
    # immediate
      imm = bin(int(asm_array[2].strip(","))).replace("0b", "").zfill(13)
      return f"{op} {rd} {op3} {rs1} 1 {imm}"
    else:
    # not immediate
      rs2 = bin(int(asm_array[2].strip("%r,"))).replace("0b", "").zfill(5)
      return f"{op} {rd} {op3} {rs1} 0 00000000 {rs2}"
  
  # Memory
  if asm_array[0] == "ld":
    op = "11"
    op3 = "000000"
    rd = bin(int(asm_array[2].strip("%r,"))).replace("0b", "").zfill(5)
    imm = bin(int(asm_array[1].strip("[],"))).replace("0b", "").zfill(13)
    return f"{op} {rd} {op3} 00000 1 {imm}"

  if asm_array[0] == "st":
    op = "11"
    op3 = "000100"
    rd = bin(int(asm_array[1].strip("%r,"))).replace("0b", "").zfill(5)
    imm = bin(int(asm_array[2].strip("[],"))).replace("0b", "").zfill(13)
    return f"{op} {rd} {op3} 00000 1 {imm}"

if __name__ == "__main__":
  print("Welcome to the ARC (Dis)assembler.")
  print("Enter 'q' at any time to quit.")
  print("This program converts between ARC binary and assembly instructions.")
  inp = input("What is the instruction? ")
  while inp != 'q':
    if len(inp) >= 32:
      print(parse_binary(inp))
    elif len(inp) < 32:
      print(parse_asm(inp))
    inp = input("\nWhat is the instruction? ")
  print("Exiting.")

