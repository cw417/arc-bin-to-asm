def parse_binary(num):
  """Parses string binary code and returns string assembly"""

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

  #print(f"{op} {rd} {op3} {rs1} {imm} {simm13}")

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
    # will add call later
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

  # Memory Functions
  elif op == "11":
    # ld
    if op3 == "000000":
      return f"ld [{simm13}], {rd}"
    # st
    elif op3 == "000100":
      return f"st {rd}, [{simm13}]"
  
def get_info():
  return input("What is the instruction? ")

if __name__ == "__main__":
  test = ""
  print(parse_binary(test))
