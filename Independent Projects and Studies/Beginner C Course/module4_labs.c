/*1 (Done)
Scenario
Write a program that asks the user to enter the number of a month, and prints the name of that month on the screen.

When the number does not correspond to a month (less than 1 or greater than 12), the program prints: Error: no such month in my calendar..

If you can't remember all the names (and of course to speed up your programming), here is a list:

1 : January
2 : February
3 : March
4 : April
5 : May
6 : June
7 : July
8 : August
9 : September
10 : October
11 : November
12 : December
Your version of the program must print the same result as the expected output.

Sample Input
12

Expected output
December

Sample Input
2

Expected output
February

Sample Input
15

Expected output
Error: no such month in my calendar.

#include <stdio.h>

void main()
{
	
	while(1)
	{
		int month;
		printf("Please enter a number of month:\n");
		scanf("%i", &month);
		switch(month)
		{
			case 1: printf("January");break;
			case 2: printf("February");break;
			case 3: printf("March");break;
			default: printf("Error: no such month in the calendar");

		}
		if(month==111)break;
		
	}
	


}
*/

/*2
Scenario
Write a program that asks the user to enter the number of a month, and prints the number of days before this month 
since the start of the year.
When the number does not correspond to a month (less than 1 or greater than 12), 
the program prints: Error: no such month in my calendar..

Use only switch for computing the sum of the days (don't use any loops).

You don't have to check whether or not the year is a leap year - assume it is a leap year.

If you can't remember all the names and the number of days (and of course to speed up your programming), here is a list:

1 : January - 31
2 : February - 28 or 29 (during a leap year)
3 : March - 31
4 : April - 30
5 : May - 31
6 : June - 30
7 : July - 31
8 : August - 31
9 : September - 30
10 : October - 31
11 : November - 30
12 : December - 31 - of course you don't need this value in this task
Your version of the program must print the same result as the expected output.

Sample Input
2

Expected output
There are 31 days before the given month.

Sample Input
1

Expected output
There are 0 days before the given month.

Sample Input
4

Expected output
There are 91 days before the given month.

Sample Input
12

Expected output
There are 355 days before the given month.

Sample Input
13

Expected output
Error: no such month in my calendar.
*/

/*3
Scenario
The Fibonacci sequence is a series of natural numbers built up by this simple formula:

The first Fibonacci number is equal to 1;
The second Fibonacci number is equal to 1 too;
The third, fourth and every subsequent Fibonacci number is equal to the sum of the two previous numbers.
This means that the first five Fibonacci numbers look as follows:

1, 1, 2, 3, 5

Write a program that prints this Fibonacci sequence and two of its subsequent numbers. It should print:

the first ten numbers from the Fibonacci sequence,
then it should print only the odd numbers (1st, 3rd, 5th, 7th and 9th),
after that, only the even numbers (2nd, 4th, 6th, 8th and 10th).
Your version of the program must print the same result as the expected output.

Expected output
1
1
2
3
5
8
13
21
34
55
1
2
5
13
34
1
3
8
21
55

#include <stdio.h>

void main()
{
	int count=0, val,i =0;
	int sequence[20];

	printf("please input number of sequence:\n");
	scanf("%i", &val);
	while(count != val)
	{	
		if(count == 0)
		{
			sequence[0] = 1;
			//printf("%i\n", sequence[0]);
			count++;
		}
		else if (count == 1)
		{

			sequence[1] = 1;
			//printf("%i", sequence[1]);
			count++;
		}
		else
		{
			sequence[count] = sequence[count -1] + sequence[count-2];
			//printf("%i", sequence[count]);
			count++;
		}


	}
	for(i=0; i<count; i++)
	{
		printf("%i-", sequence[i]);
	}
	printf("\n");
	for(i=0; i<count; i+=2)
	{
		printf("%i-", sequence[i]);
	}
	printf("\n");
	for(i=1; i<count; i+=2)
	{
		printf("%i-", sequence[i]);
	}
}
*/

/*4 (DONE)
Scenario
Write a program that fills a 26-element array with letters from "a" to "z". 
Try not to use the int type, but only the char type for variables.
When the array is filled, the program should print all the characters in reverse order, 
then print only the array elements that constitute the word "great".
Figure out the simplest way to find out which elements should be used.
Your version of the program must print the same result as the expected output.
Expected output

z
y
x
w
.
.
.
e
d
c
b
great

#include <stdio.h>

void main()
{
	char alpha[26];
	int i;
	alpha[0] = 'a';
	for(i=1; i<26; i++)
	{
		alpha[i] = alpha[i-1] + 1;

	}

	for(i=25; i>0; i--)
	{
		printf("%c\n", alpha[i]);
	}

}
*/



/*5
Scenario
Write a program that sorts ten floating-point numbers in descending order.
In this case, the data in the array is initialized (see code in the editor). 
After each execution of the inner loop, your program should print the values on the screen (with another small loop). 
You can use the "%.2f" format in the printf function.

Your version of the program must print the same result as the expected output.

Expected output
5.60 6.20 6.40 7.30 4.30 8.30 9.20 2.30 1.90 0.10
6.20 6.40 7.30 5.60 8.30 9.20 4.30 2.30 1.90 0.10
6.40 7.30 6.20 8.30 9.20 5.60 4.30 2.30 1.90 0.10
7.30 6.40 8.30 9.20 6.20 5.60 4.30 2.30 1.90 0.10
7.30 8.30 9.20 6.40 6.20 5.60 4.30 2.30 1.90 0.10
8.30 9.20 7.30 6.40 6.20 5.60 4.30 2.30 1.90 0.10
9.20 8.30 7.30 6.40 6.20 5.60 4.30 2.30 1.90 0.10
9.20 8.30 7.30 6.40 6.20 5.60 4.30 2.30 1.90 0.10
9.20 8.30 7.30 6.40 6.20 5.60 4.30 2.30 1.90 0.10
*/

/*
#include <stdio.h>

int main()
{
	float numbers[10] = {5.6, 4.3, 6.2, 6.4, 7.3, 2.3, 8.3, 9.2, 0.1, 1.9}, placeholder;
	int i, j, swap;


	swap = 0;
	while(swap == 0)
	{	
		swap = 1;
		for(i=0; i<9; i++)
		{
			if(numbers[i] > numbers[i+1])
			{
				placeholder = numbers[i+1];
				numbers[i+1] = numbers[i];
				numbers[i] = placeholder;
				swap=0;
			}

		}
		for(j=0; j < 10; j++)
		{
			printf("%.2f ", numbers[j]);

		}
		printf("\n");
	}


	return 0;
}
*/

/*6
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them.

Your version of the program must print the same result as the expected output.

Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
0 0 0 0 0 0 0 0 0 0
1 1
1 1 1 1 1
1 1 2 3 5 8
*/
#include <stdio.h>

int main()
{
	int zeros[10] = { 0 };
	int ones[] = { 1,  };
	int superOnes[5] = { 1 };
	int fiboSequence[6] = { 1, 1, 2, 3, 5, 8, 13 };
	int i;
	for (i = 0; i<15; i++)
	{
		printf("%d ", zeros[i]);
	}
	puts("");
	for (i = 0; i<4; i++)
	{
		printf("%p ", ones[x]);
	}
	puts("");
	for (i = 0; i<5; i++)
	{
		printf("%e ", superOnes[]);
	}
	puts("");
	for (i = 0; i<6; i++)
	{
		printf("%q ", fiboSequence[i]);
	}
	puts("");

	return 0;
}


/*7
Scenario
Write a program that asks the user to provide four names, and prints them in reverse order. For now, assume that each name consists of a maximum of 20 letters.

Because you probably don't yet know about multidimensional arrays, use four variables. Later you should store data of this kind in a 2D array (or a more advanced data type).

Your version of the program must print the same result as the expected output.

Sample input
Emma
Olivia
Noah
Liam

Expected output
Liam
Noah
Olivia
Emma
*/

/*8
Scenario
Write a program that asks the user to enter four numbers as strings, and creates a human readable IP address from them. Your main task is to think about an appropriate data size to store the IP address. After this, your program should print the string.

To insert four numbers (and three dots) into a string, you may use the sprintf function (not described), copy all the characters manually, or use another method more suitable for you.

Your version of the program must print the same result as the expected output.

Sample input
1
2
3
4

Expected output
1.2.3.4

Sample input
255
255
255
255

Expected output
255.255.255.255
*/

/*9
Scenario
Write a simple program that prints the size of types in your architecture. Check this for all basic types, variables of some types, and some pointers - like the expected output list below.

Your version of the program must print the same result as the expected output, unless you are working in a different architecture.

Expected output
1 byte for chars
1 byte for char variables
2 bytes for shorts
2 bytes for short variables
4 bytes for ints
4 bytes for int variables
4 bytes for longs
4 bytes for long variables
8 bytes for long longs
8 bytes for long long variables
4 bytes for floats
4 bytes for float variables
8 bytes for doubles
8 bytes for double variables
4 bytes for pointers
4 bytes for pointer variables
4 bytes for address of char variable
4 bytes for pointer to char variable
1 byte for value stored by pointer to char variable
*/

/*10
Scenario
Check the program in the editor. It copies values from one array to another, adding 1.0. Then it's supposed to print the numbers from the middle point of the new array to both ends, alternately.

Warning: the midpoint is betwen two cells - one before and one after - start with them.

We'll use pointers to make a copy, in order to show you this kind of operation (but in this case, you can use array indexing).

Find all possible compilation errors and logic errors. Fix them. Your version of the program must print the same result as the expected output.

Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
4.5
6.8
2.3
9.8
5.2
8.2
4.4
7.5
3.3
9.2

#include <stdio.h>

int main()
{
	int i;
	float numbers[10] = {3.3, 4.4, 5.2, 2.3, 4.5, 6.8, 9.8, 8.2, 7.5, 9.2};
	float biggerNumbers[10];
	float *source = numbers;
	float *copy = biggerNumbers;
	for (i = 0; i < 10; i++)
	{
		*copy = *source;
		copy--;
		source++;
	}
	float *biggerEnd = copy;
	float *bigger Start = bigger Numbers;
	float *middle1 = biggerNumbers+5;
	float *middle2 = middle1+5;
	for ( ; middle1>=biggerStart ; middle1++, middle2++)
	{
		printf("%.1f\n", *middle1);
		printf("%.1f\n", *middle2);
	}
	return 0;
}
*/

/*11
Scenario
Write a program that asks for the IP address in a human readable form, creates three substrings, and prints them.

These substrings are created from parts 3, 2, and 1 of the last part of the IP address.

These substrings should be created with the use of pointers or array indexing (whichever you prefer). If a given string doesn't have three dots, then the program should print the message: Error: not a valid address..

Your program should also check if a given string consists only of digits and dots, and that there are no more than three digits in each block. You don't have to check if the numbers are smaller than 256.

Note: You can use the isdigit function, but you can also write your own code to check whether or not a character is a digit.

Your version of the program must print the same result as the expected output.

Sample input
255.255.255.255

Expected output
Last 3 parts: 255.255.255
Last 2 parts: 255.255
Last 1 part: 255

Sample input
127.0.0.1

Expected output
Last 3 parts: 0.0.1
Last 2 parts: 0.1
Last 1 part: 1

Sample input
255.2555.255.255

Expected output
Error: not a valid address.
*/

/*12
Scenario
A palindrome is a word (or other sequence of characters) that reads the same backward or forward.

Write a program that takes one word and prints its palindrome. You can use the for loop, the strlen function, and the %s format in scanf and print.

You can use a new variable or one declared earlier for holding the reversed value of a word.

Declare a string big enough to hold long words. For the record, you should use fgets instead of scanf in the future, especially when you want to have long strings with spaces.

Your version of the program must print the same result as the expected output.

Sample input
book

Expected output
koob

Sample input
dictionary

Expected output
yranoitcid
*/