/*1
Scenario
Write a program that creates a chessboard, sets all the pieces on it and then displays the contents of the board.

Create a two-dimensional array, fill it with data and print a letter when a piece is on the field and a space when there is no piece. Store one letter for one piece.

For now, we don't need any information about the color of the pieces.

The starting positions (with letters which symbolize each piece) for all pieces are:

The rooks (R) are placed on the outside corners, right and left edge (white on the 1st and black on the 8th line).
The knights (N) are placed immediately inside of the rooks.
The bishops (B) are placed immediately inside of the knights.
The queen (Q) is placed on the central square of the same color as that of the player: white queen on the white square and black queen on the black square. Both stand on the d rank: white queen on the d1 field and black queen on the d8 field.
The king (K) takes the vacant spot next to the queen.
The pawns (P - not the official symbol, but you need to print something) are placed one square in front of all of the other pieces.
Your version of the program must print the same result as the expected output.

Expected output
RNBQKBNR
PPPPPPPP




PPPPPPPP
RNBQKBNR

*/

/*2
Scenario
Write a program that asks the user to enter a number, and prints which day of the week that number corresponds to. The days are indexed from 0 (Sunday) to 6 (Saturday).

Store the names of the days in an array and print the name of the day in two ways:

with pointer arithmetic;
with array indexing.
Before the program gets a value from the array, it must first check if the given day is greater than or equal to zero and less than 7. If not, it should print the message: Error, no such day..

Your version of the program must print the same result as the expected output.

Sample input
0

Sample output
Pointer version: Sunday
Array index version: Sunday

Sample input
5

Sample output
Pointer version: Friday
Array index version: Friday

Sample input
12

Sample output
Error, no such day.
*/

/*3
Scenario
Write a program that allocates memory of a size requested by the user.

This program requests a number from the user and checks if that number is less than 1 MB (1024*1024). If it's not, then the program prints the message: Too much memory requested..

In the next step, the program allocates a one-dimesional array of characters (char) and fills this array with characters from "A" to "Z" - the first element (index 0) contains "A", the 26th element (index 25) contains "Z", the 27th element (index 26) contains "A" and so on.

Then, the program prints the first 400 bytes of an array (or the whole array if it's smaller than 400 characters), 40 characters in each row.

To simplify the program, you can use the break or continue statements. Remember to free up the array memory at the end of the program.

Your version of the program must print the same result as the expected output.

Sample input
100

Expected output
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMN
OPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZAB
CDEFGHIJKLMNOPQRSTUV

Sample input
500

Expected output
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMN
OPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZAB
CDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOP
QRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCD
EFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQR
STUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF
GHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRST
UVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGH
IJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUV
WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJ

Sample input
1200500

Expected output
Too much memory requested.
*/

/*4
Scenario
Write a program that displays the multiplication table of a given size.

First, your program should ask the user to specify the size (height and weight are equal, so one number should be enough).

If the size is greater than 20, the program should print the message: Matrix too big..

Then it should allocate a matrix and fill this matrix with appropriate values (remember: the element of [0][0] should store the multiplication result of 1 and 1).

Then the program should print the multiplication table, four characters per cell. Finally, all memory must be freed.

Your version of the program must print the same result as the expected output.

Sample input
5

Expected output
       1   2   3   4   5
   1   1   2   3   4   5
   2   2   4   6   8  10
   3   3   6   9  12  15
   4   4   8  12  16  20
   5   5  10  15  20  25

Sample input
25

Expected output
Matrix too big.
*/

/*5
Scenario
Analyze the code we've provided in the editor. Write additional lines of code to call the functions defined.

Call the functions as many times as necessary and in the proper order so as to get the expected output.

Your version of the program must print the same result as the expected output.

Expected output
Hello!
Hello!
Hello!
It's me - another function.
Hello!
It's me - another function.

#include <stdio.h>

void hello()
{
	puts("Hello!");
}
void another()
{
	puts("It's me - another function.");
}

int main(void)
{
	/* your code 
	return 0;
}
*/

/*6
Scenario
Check the code in the editor. Add appropriate lines of code to call the functions defined in it.

Analyze what values both functions will return. Connect the function calls to obtain a proper result (the variable name should contain its expected value).

You can use as many different combinations as you want, but try to find a way to obtain the proper result with the smallest number of function calls.

Your version of the program must print the same result as the expected output.

Expected output
Five: 5
Six: 6
Seven: 7
Eight: 8
Nine: 9

#include <stdio.h>

int getValue(int paramA, float paramB)
{
	int result = 0;
	if (paramA>10)
	{
		result += 2;
	}
	else
	{
		result += 1;
	}
	if (paramB>5.5)
	{
		result += 4;
	}
	else
	{
		result += 3;
	}
	return result;
}

int getOneOrTwo(int param)
{
	if(param > 5)
		return 2;
	return 1;
}

int main(void)
{
	int fiveValue ; // your code 
	int sixValue ; // your code 
	int sevenValue ; // your code 
	int eightValue ; // your code 
	int nineValue ; // your code
	
	printf("Five: %d\n", fiveValue);
	printf("Six: %d\n", sixValue);
	printf("Seven: %d\n", sevenValue);
	printf("Eight: %d\n", eightValue);
	printf("Nine: %d\n", nineValue);
	return 0;
}
*/

/*7
Scenario
Check the program in the editor. Write a body of functions where indicated in order to obtain the correct result.

The function getMaxOfThreeshould return the largest number among three given numbers.

Your version of the program must print the same result as the expected output.

Expected output
Ten: 10.00
Biggest value: 556.40

#include <stdio.h>

double getMaxOfThree(double paramA, double paramB, double paramC)
{
	/* your code 
}

int main(void)
{
	double tenValue = getMaxOfThree(5, 9, 10);
	double bigValue = getMaxOfThree(555.4, 555.3, 556.4);
	printf("Ten: %.2f\n", tenValue);
	printf("Bigest value: %.2f\n", bigValue);
	return 0;
}
*/

/*8
Scenario
Check the program in the editor. Write a function that is a simpler version of the power function. It takes two parameters, one of type double and one of type int.

The first argument is the base and the second is the exponent. You can use a forloop to multiply the first argument as many times as the second argument says.

Because it's a simple version, you are only required to handle positive integers and 0. Separate the declaration of the function from its full definition.

Your version of the program must print the same result as the expected output.

Expected output
Thirty five: 25.0000
Pi squared: 9.8696
Pi cubed: 31.0063
Not so big number: 62.8206
Million: 1000000.0000

#include <stdio.h>

// your code 

int main(void)
{
	double twentyFiveValue = power(5.0, 2);
	double piSquaredValue = power(3.14159265, 2);
	double piCubedValue = power(3.14159265, 3);
	double bigPower = power(1.23, 20);
	double millionValue = power(10, 6);
	printf("Thirty five: %.4f\n", twentyFiveValue);
	printf("Pi squared: %.4f\n", piSquaredValue);
	printf("Pi cubed: %.4f\n", piCubedValue);
	printf("Not so big number: %.4f\n", bigPower);
	printf("Million: %.4f\n", millionValue);
	return 0;
}
/* your code 
*/

/*9
Scenario
Check the program in the editor. Write a body of functions to obtain the correct result.

The function getValue must return:

25 - when paramA is greater than or equal to 5 and paramB is greater than or equal to 2.5;
30 - when paramA is greater than or equal to 5 and paramB is less than 2.5;
30 - when paramA is less than 5 and paramB is greater than or equal to 2.5;
35 - when paramA is less than 5 and paramB is less than 2.5.
The function getExclusive must return:

2 - when one and only one of the given values is equal to 2;
0 - in all other cases.
Your version of the program must print the same result as the expected output.

Expected output
Thirty five: 35
Thirty: 30
Thirty: 30
Twenty: 25
Two: 2
Zero: 0

#include <stdio.h>

int getValue(int paramA, float paramB);
int getExclusive(int paramA, int paramB);

int main(void)
{
	int thirtyFiveValue = getValue(4, 2.4);
	int thirtyValue1 = getValue(4, 2.6);
	int thirtyValue2 = getValue(6, 2.4);
	int twentyValue = getValue(6, 2.6);
	int twoValue = getExclusive(2, 1);
	int zeroValue = getExclusive(2, 2);

	printf("Thirty five: %d\n", thirtyFiveValue);
	printf("Thirty: %d\n", thirtyValue1);
	printf("Thirty: %d\n", thirtyValue2);
	printf("Twenty: %d\n", twentyValue);
	printf("Two: %d\n", twoValue);
	printf("Zero: %d\n", zeroValue);
	return 0;
}
/* your code 
*/

/*10
Scenario
Check the program in the editor. We've removed all the variable names from the function declaration and body. Complete this code with your variable names.

This function compares two strings and it returns:

-1 - when the first string is before the second string in alphabetical order;
0 - when the contents of both strings are exactly the same;
1 when the first string is after the second string in alphabetical order;
Your version of the program must print the same result as the expected output.

Expected output
result1: -1
result2: 1
result3: 0
result4: -1

#include <stdio.h>

int stringCompare(char *, char *)
{
	int ;
	for (=0 ; [] != 0 && [] != 0 ; ++)
	{
		if([]>[])
		{
			return 1;
		}
		else if ([] < [])
		{
			return -1;
		}
	}
	if ([] == 0)
	{
		if ([] == 0)
			return 0;
		else
			return -1;
	}
	else
		return 1;
}

int main(void)
{
	int result1 = stringCompare("AAA", "BBB");
	int result2 = stringCompare("AAC", "AAB");
	int result3 = stringCompare("AAC", "AAC");
	int result4 = stringCompare("AAC", "AACC");
	printf("result1: %d\n", result1);
	printf("result2: %d\n", result2);
	printf("result3: %d\n", result3);
	printf("result4: %d\n", result4);
	return 0;
}
*/
