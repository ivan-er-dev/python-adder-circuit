from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

# ALU (Arithmetic Logic Unit)
# half adder
print("Half adder")
print("")
# o todos o uno -> true
# ninguno o mas de uno pero no todos -> false

s = 0
c = 0
def half_adder(a, b):
  global s
  global c

  if a != b:
    s = 1
  else:
    s = 0
  
  if a and b:
    c = 1
  else:
    c = 0

  return (s, c)

s
c

print("A: 0, B: 0 | Output: {0}".format(half_adder(0, 0)))
print("S: {0}".format(s))
print("C: {0}".format(c))
print("")
print("A: 0, B: 1 | Output: {0}".format(half_adder(0, 1)))
print("S: {0}".format(s))
print("C: {0}".format(c))
print("")
print("A: 1, B: 0 | Output: {0}".format(half_adder(1, 0)))
print("S: {0}".format(s))
print("C: {0}".format(c))
print("")
print("A: 1, B: 1 | Output: {0}".format(half_adder(1, 1)))
print("S: {0}".format(s))
print("C: {0}".format(c))

# full adder
print("")
print("Full adder")
print("")

s = 0
c_out = 0
def full_adder(a, b, c):
  global s
  global c_out

  if not a and not b and not c:
    s = 0
  if a:
    if b:
      s = 0
    if c:
      s = 0
    if not b:
      if not c:
        s = 1
  if b:
    if a:
      s = 0
    if c:
      s = 0
    if not a:
      if not c:
        s = 1
  if c:
    if a:
      s = 0
    if b:
      s = 0
    if not a:
      if not b:
        s = 1
  if a and b and c:
    s = 1
  
  if not a and not b and not c:
    c_out = 0
  if a:
    if b != c:
      c_out = 1
    if not b and not c:
      c_out = 0
  if b:
    if a != c:
      c_out = 1
  if c:
    if b != a:
      c_out = 1
  if a and b and c:
    c_out = 1

  return (s, c_out)

s
c_out

print("A: 0, B: 0, C: 0 | Output: {0}".format(full_adder(0, 0, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 0, B: 0, C: 1 | Output: {0}".format(full_adder(0, 0, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 0, B: 1, C: 0 | Output: {0}".format(full_adder(0, 1, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 0, B: 1, C: 1 | Output: {0}".format(full_adder(0, 1, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 0, C: 0 | Output: {0}".format(full_adder(1, 0, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 0, C: 1 | Output: {0}".format(full_adder(1, 0, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 1, C: 0 | Output: {0}".format(full_adder(1, 1, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 1, C: 1 | Output: {0}".format(full_adder(1, 1, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))

# ALU
# a bit called opcode
print("")
print("ALU")
print("")

s = 0
c_out = 0

def ALU(a, b, c, opcode):
  global s
  global c_out

  if opcode == 0:
    s, c_out = half_adder(a, b)
  if opcode == 1:
    s, c_out = full_adder(a, b, c)
  
  return (s, c_out)

print("A: 0, B: 0, C: 1, Opcode: 0 | Output: {0}".format(ALU(0, 0, 1, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 0, B: 0, C: 1, Opcode: 1 | Output: {0}".format(ALU(0, 0, 1, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 1, C: 1, Opcode: 0 | Output: {0}".format(ALU(1, 1, 1, 0)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")
print("A: 1, B: 1, C: 1, Opcode: 1 | Output: {0}".format(ALU(1, 1, 1, 1)))
print("S: {0}".format(s))
print("C Out: {0}".format(c_out))
print("")