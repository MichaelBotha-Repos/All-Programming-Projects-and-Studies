first_frame = 0b00010001
second_frame = 0b00000001
data_stream = first_frame | (second_frame << 8)


print(first_frame)
print(second_frame)
print(f"{data_stream : 16b}")
