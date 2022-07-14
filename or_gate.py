from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate

def OR_gate(a, b):
  if a or b:
    return 1
  else:
    return 0

# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(OR_gate(1, 1)))