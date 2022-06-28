import serial


# Bit representation:
# D3-D2-D1-D0-A2-A1-A0-Data_Startbit (two start bits required)
first_frame = 0b00010001
# Bit representation:
# D7-D6-D5-D4-A2-A1-A0-Data_Startbit (two start bits required)
second_frame = 0b00000001
# Combining the two frames to send in a single pyserial function call 
# so as to ensure no time difference between the two
data_stream = first_frame | (second_frame << 8)

print(first_frame, type(first_frame))
print(second_frame)
# Printing the data stream in binary showing 16bits 
print(f"{data_stream : 16b}")

connection = serial.Serial( 
                            port = 'COM5',
                            baudrate = 9600,
                            write_timeout = 0
                          )

result = connection.write(data_stream)