#include <stdio.h>
#include <string.h>

struct bitfield
{
    unsigned int byte1: 8;
    unsigned int byte2: 8;
    unsigned int byte3: 8;
    unsigned int byte4: 8;
}my_bitfield;

union bitfield_option
{
    unsigned int bitfield_int;
    struct bitfield bitfield_bytes;
}my_union;

int main(void)
{
    my_bitfield.byte1 = 8;
    my_bitfield.byte2 =16;
    my_bitfield.byte3 = 32;
    my_bitfield.byte4 = 64;
    my_union.bitfield_bytes = my_bitfield;

    unsigned int *bitfield_ptr = &my_bitfield.byte1;

    printf("%d", my_union.bitfield_int);
    
}