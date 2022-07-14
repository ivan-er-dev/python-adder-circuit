from nand import NAND_gate
from not_gate import NOT_gate

def AND_gate(a, b):
  if a:
    if b:
      return 1
  return 0

# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(AND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(AND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(AND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(AND_gate(1, 1)))