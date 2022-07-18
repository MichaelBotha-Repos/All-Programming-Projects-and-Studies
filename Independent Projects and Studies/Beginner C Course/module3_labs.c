/*1
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them, and try to find proper conditions for all of the three statements.

Your version of the program must print the same result as the expected output. Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
First condition is true
Second condition is false
Third condition is true

#include <stdio.h>

int main(void)
{
	int a = 10;
	
	if (a  9)
		puts("First condition is true");
	else
		puts("First condition is false");
	
	if (a  9)
		puts("Second condition is true");
	else
		puts("Second condition is false");
	
	if (a isequal 9 + 1)
		puts("Third condition is true");
	else
		puts("Third condition is false");
	return 0;
}
*/

/*2
Scenario
The most popular, human-readable way to write an IP (to be precise, IPv4) is to write four numbers separated with dots (e.g., 127.0.0.1). 
But an IP address can also be written as a 32-bit number.
To get this form, you must multiply all the parts of the IP number by powers of 256 (256*256*256, 256*256, 256 and 1 - don't use precomputed versions).
Write a program that asks the user to provide four numbers, and then checks if these numbers are more than or equal to 0, and less than or equal to 255.
Next, the program should write both forms of the IP address: the human-readable one and the 32-bit-number one.
Use the unsigned long int type; to print it, use the "%lu" format in the printf function.
If any of the address parts doesn't meet the given criteria (0<=x<=255), print only this simple error message: Inccorect IP Address..

Your version of the program must print the same result as the expected output.

Sample Input
127
0
0
1

Expected output
Human-readable IP address is: 127.0.0.1
IP address as a 32-bit number: 2130706433 

Sample Input
192
168
1
1

Expected output
Human-readable IP address is: 192.168.1.1
IP address as a 32-bit number: 3232235777 

Sample Input
1
268
1
1

Expected output
Incorrect IP Address.
*/

#include <stdio.h>

void main()
{
	int octet, answer;
	unsigned long ip;

	for(int i= 4 ; i > 0; i--)
	{	
		printf("Please input %i octet:\n", i );
		scanf("%i", &octet);
		if(octet<0 || octet>255)
		{
			printf("incorrect ip address");

		}
		else
		{
			ip = (ip << 8) | octet;

		}

	}
 	printf("IP address as 32-bit number: %lu", ip);
	printf("Human-readable IP address: %lu.%lu.%lu.%lu", (ip&4278190080)>>24, (ip&16711680)>>16, (ip&65280)>8, ip&255);

}

/*3
Scenario
Write a program that takes one floating-point number, converts it to an integer number, and then prints a description of the given number. Descriptions for numbers:

numbers greater than or equal to 1 and less than 2 - Very bad.
numbers greater than or equal to 2 and less than 3 - Bad.
numbers greater than or equal to 3 and less than 4 - Neutral.
numbers greater than or equal to 4 and less than 5 - Good.
numbers greater than or equal to 5 and less than 6 - Very good.
When a number is out of the given range (1<=x<6), the program should print nothing.

Your version of the program must print the same result as the expected output.

Sample Input
1.5

Expected output
Very bad

Sample Input
2.9

Expected output
Bad

Sample Input
4.77

Expected output
Good
*/

/*4
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them.

Your version of the program must print the same result as the expected output.

Before you use the compiler, try to find the errors only by manual code analysis. Use the converted number to check how to round a float number.

Expected output
Five is: 5
Rounded to seven: 7

#include <stdio.h>

int main(void)
{
	float notExactFive = 5.4;
	float notExactNumber = 6.7;
	int exactFive;
	int roundedNumber;
	if notExactNumber - notExactNumber > 0.5
	{
		roundedNumber = (int)notExactNumber + 1;
	}
	else
	{
		roundedNumber = int notExactNumber;
	}
	exactFive = (int)notExactFive;
	printf("Five is: %f\n", exactFive);
	printf("Rounded to seven: %d\n", roundedNumber);
	return 0;
}
*/

/*5
Scenario
Write a program that takes two integer numbers and prints their sum. Do this until the user enters 0 (zero) (but print the last sum).

Additionally, if the user inputs 99 as the first number and 0 as the second number, just print Finish., and end the program.

Use the while loop in your code.

Your version of the program must print the same result as the expected output.

Sample Input
1
1
2
0

Expected output
Sum: 2
Sum: 2

Sample Input
1
5
99
0

Expected output
Sum: 6
Sum: 99
Finish.
*/

/*6
Scenario
Write a program that asks the user to enter a number. Then:

the program should print the number of lines corresponding to the number inputted;
each line should contain the number of pairs of characters *# equal to the number of this line.
The outputted "drawing" should be similar to the right half of a pyramid.

Your version of the program must print the same result as the expected output. To do this lab, you must use two do-while loops.

However:

when the user inputs a number less than or equal to 1, the program should print only one line;
When the user inputs a number greater than 20, the program should print only twenty lines.
Sample Input
3

Expected output
*#
*#*#
*#*#*#

Sample Input
5

Expected output
*#
*#*#
*#*#*#
*#*#*#*#
*#*#*#*#*#

Sample Input
0

Expected output
*#

*/

/*7
Scenario
Write a program that asks the user to enter a number, and prints twice as many lines as the number inputted.

The first half of every other line contains one * character at the start, as many spaces as the number of this line (line numbers count from 0 in this task) and one * character at the end of the line. The second half is a mirror reflection of the first.

The outputted "drawing" should be similar to an arrowhead.

Your version of the program must print the same result as the expected output. To do this task, you should use two outer for loops and two inner for loops.

You shouldn't use any special formatting in the printf to print the spaces - just use the for loop.

Two exceptions:

when the user inputs a number less than or equal to 1, the program doesn't print any line.
when the user inputs a number greater than 20, the program prints only forty lines.
Sample input
3

Expected output
**
* *
*  *
*  *
* *
**

Sample input
9

Expected output
**
*   *
*    *
*     *
*      *
*       *
*        *
*         *
*          *
*          *
*         *
*        *
*       *
*      *
*     *
*    *
*   *
**
*/

/*8
Scenario
Write a program that computes and prints whether or not a given year is a leap year.

A leap year is a year that is exactly (without a remainder) divisible by four, except for years that are exactly divisible by 100, but these years are leap years if they are exactly divisible by 400.

Use the modulo operator and some logic operators in your program and try to write only one condition (of course you can now use the else keyword).

Your version of the program must print the same result as the expected output.

Sample input
2010

Expected output
2010 is not a leap year.

Sample input
2015

Expected output
2015 is not a leap year.

Sample input
2000

Expected output
2000 is a leap year.

Sample input
1900

Expected output
1900 is not a leap year.
*/

/*9
Scenario
A nibble is just a four-bit aggregation - we can also call it a half-byte.

Sometimes we use the terms low nibble and high nibble to denote nibbles containing less significant bits (low nibble - L) and more significant bits (high nibble - H) within a byte.

Write a program that asks the user for one integer number smaller than 256, and prints both nibbles of the number. You don't have to verify the input.

Your version of the program must print the same result as the expected output.

Sample input
255

Expected output
H nibble: 15
L nibble: 15

Sample input
63

Expected output
H nibble: 3
L nibble: 15

Sample input
11

Expected output
H nibble: 0
L nibble: 11
*/
