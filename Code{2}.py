import sys
def bytes_arr(val):
    hexarr = bytearray.fromhex(val[2:])
    str_val = ''.join(format(x, '02x') for x in hexarr)
    print("BYTE form:", hexarr)
    length = len(hexarr)
    print("NUM_OF_BYTES: ", length)

    return str_val

def down(val):
  Littleend = bytearray.fromhex(val[2:])
  Littleend.reverse()

  str_LE = ''.join(format(x, '02x') for x in Littleend)
  return str_LE

def up(value):
    bits = 16
    val = int(value, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

def from_down_to_hex(Littleend):
    print("From little -> Hex: ", hex(Littleend))
def from_up_to_hex(big_endian):
    print(f"From Big endian to HEX: {hex(big_endian)}")
while True:
    value = str(input("Enter HEX number -> "))
    if value == "exit":
        sys.exit()
    bytesArray = bytes_arr(value)
    Littleend = down(value)
    big_end = up(value)
    print("LITTLEEND HEX: ", Littleend )
    print("Littleend-> ", int(Littleend, 16))
    print("big_end -> ", big_end)
    from_down_to_hex(int(Littleend,16))
    from_up_to_hex(big_end)
    input("Press any key to continue...")
