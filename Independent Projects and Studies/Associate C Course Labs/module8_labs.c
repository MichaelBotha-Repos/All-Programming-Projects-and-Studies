/*1
Do you remember Lab 6.1.8.11? Take the sources from that lab and modify them. Add #define and #ifndef in the header file (triangles.h) to avoid multiplied compilations.

Add a macro to log information to the screen, call this macro before each function call, and pass the name of the function into the macro. The macro should get the line and file name from the other macros.

Your version of the program must print the same result as the expected output.

Sample input
5

Expected output
In line 13, file path\main.c, before the normalTriangle function

\
\\
\\\
\\\\
In line 15, file path\main.c, before the floydsTriangle functionv

   1
   2   3
   4   5   6
   7   8   9  10

Sample input
3

Expected output
3
In line 13, file path\main.c, before the normalTriangle function

\
\\
In line 15, file path\main.c, before the floydsTriangle function

   1
   2   3
*/

/*2
Write a function that checks whether or not a given string is a valid IP address (in human-readable form, of course). This function should return 1 if the address is valid, and 0 if not.

Your function should check if:

there are four parts in the string, separated by dots;
each part contains only digits;
each number is in the range of 0 to 255, inclusive.
For converting string fragments to integer values, you can use the strtol, atoi or sscanf functions.

Separate the declaration of the function from its full definition.

Write a second function that calls the first one and then prints an appropriate message: 127.0.0.1 is a valid IP address or a.b.c.d is not a valid IP address.

Write a code to test it with values - call the second function. Do not limit yourself only to those values that we have given to you.

We did a similar task in Lab 6.1.6.9. The only difference between this lab and that one is that here you need to define all the constants (even one-character constants!) with preprocessor defines.

You should also give them appriopriate names. After the whole process, you can (because you are an advanced user now) judge which option is better: to change all the possible constants or to leave some of them in their natural form.

Expected output
127.0.0.1 is a valid IP address
127.0.01 is not a valid IP address
127.0..1 is not a valid IP address
127.zero.0.1 is not a valid IP address
127.297.0.1 is not a valid IP address
127.2555.0.1 is not a valid IP address

#include <stdio.h>

// your code 

int main()
{
	// your code 
	return 0;
}
// your code 
*/