from nand import NAND_gate

def NOT_gate(a):
  if a:
    return 0
  return 1

# TEST CASE
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}".format(NOT_gate(1)))