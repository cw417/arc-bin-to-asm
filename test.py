import unittest
from main import parse_binary, parse_asm
class TestDisassembly(unittest.TestCase):

  def test_branch(self):
    be = "000 0001 010 0000000000000000001010"
    self.assertEqual("be 10", parse_binary(be))

    bneg = "000 0110 010 0000000000000000000011"
    self.assertEqual("bneg 3", parse_binary(bneg))

    ba = "000 1000 010 0000000000000000000010"
    self.assertEqual("ba 2", parse_binary(ba))

  def test_sethi(self):
    pass

  def test_call(self):
    pass

  def test_arithmetic(self):
    addcc = "10 00000 010000 00010 0 00000000 00011"
    self.assertEqual("addcc %r2, %r3, %r0", parse_binary(addcc))
    addcc_asm = "addcc %r2, %r3, %r0"
    self.assertEqual("10 00000 010000 00010 0 00000000 00011", parse_asm(addcc_asm))

    subcc = "10 00000 010100 00101 0 00000000 00110"
    self.assertEqual("subcc %r5, %r6, %r0", parse_binary(subcc))
    subbcc_asm = "subcc %r5, %r6, %r0"
    self.assertEqual("10 00000 010100 00101 0 00000000 00110", parse_asm(subbcc_asm))

    andcc = "10 00011 010001 00001 0 00000000 00010"
    self.assertEqual("andcc %r1, %r2, %r3", parse_binary(andcc))
    andcc_asm = "andcc %r1, %r2, %r3"
    self.assertEqual("10 00011 010001 00001 0 00000000 00010", parse_asm(andcc_asm))

    orcc = "10 00001 010010 00001 0 00000000 00010"
    self.assertEqual("orcc %r1, %r2, %r1", parse_binary(orcc))
    orcc_asm = "orcc %r1, %r2, %r1"
    self.assertEqual("10 00001 010010 00001 0 00000000 00010", parse_asm(orcc_asm))

  def test_memory(self):
    ld = "11 00001 000000 00000 1 0100000100100"
    self.assertEqual("ld [2084], %r1", parse_binary(ld))

    st = "11 00011 000100 00000 1 0101111000100"
    self.assertEqual("st %r3, [3012]", parse_binary(st))

if __name__ == "__main__":
  unittest.main()