# encode 7 alphanumeric with alpha in the range A-N and numeric in the range 0-9 into 3 bytes
# 7 alphanumeric characters are encoded into 3 bytes
# 1st byte: 0x40 + (alpha1 - 0x41) * 10 + (numeric1 - 0x30)
# 2nd byte: 0x40 + (alpha2 - 0x41) * 10 + (numeric2 - 0x30)
# 3rd byte: 0x40 + (alpha3 - 0x41) * 10 + (numeric3 - 0x30)
# 4th byte: 0x40 + (alpha4 - 0x41) * 10 + (numeric4 - 0x30)
# 5th byte: 0x40 + (alpha5 - 0x41) * 10 + (numeric5 - 0x30)
# 6th byte: 0x40 + (alpha6 - 0x41) * 10 + (numeric6 - 0x30)
# 7th byte: 0x40 + (alpha7 - 0x41) * 10 + (numeric7 - 0x30)
# 8th byte: 0x40 + (alpha8 - 0x41) * 10 + (numeric8 - 0x30)