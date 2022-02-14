import unittest
from main import parse_binary
class TestDisassembly(unittest.TestCase):

  def test_branch(self):
    be = "000 0001 010 0000000000000000001010"
    bneg = "000 0110 010 0000000000000000000011"
    ba = "000 1000 010 0000000000000000000010"
    self.assertEqual("be 10", parse_binary(be))
    self.assertEqual("bneg 3", parse_binary(bneg))
    self.assertEqual("ba 2", parse_binary(ba))

  def test_sethi(self):
    pass

  def test_call(self):
    pass

  def test_arithmetic(self):
    addcc = "10 00000 010000 00010 0 00000000 00011"
    subcc = "10 00000 010100 00101 0 00000000 00110"
    andcc = "10 00011 010001 00001 0 00000000 00010"
    orcc = "10 00001 010010 00001 0 00000000 00010"
    self.assertEqual("addcc %r2, %r3, %r0", parse_binary(addcc))
    self.assertEqual("subcc %r5, %r6, %r0", parse_binary(subcc))
    self.assertEqual("andcc %r1, %r2, %r3", parse_binary(andcc))
    self.assertEqual("orcc %r1, %r2, %r1", parse_binary(orcc))

  def test_memory(self):
    ld = "11 00001 000000 00000 1 0100000100100"
    st = "11 00011 000100 00000 1 0101111000100"
    self.assertEqual("ld [2084], %r1", parse_binary(ld))
    self.assertEqual("st %r3, [3012]", parse_binary(st))
    pass

if __name__ == "__main__":
  unittest.main()