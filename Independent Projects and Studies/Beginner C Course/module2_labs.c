/*3(done)
Expected output
The value of half is: 0.500000
The value of Pi is: 3.1415113 
#include <stdio.h>
int main()
{
	float halfValue = 0.5;
	float piValue = 3.141511265;
	printf("The value of half is: %f\n", halfValue);
	printf("The value of Pi is: %f\n", piValue);
	return 0;
}
*/

/*4 (done)
Expected output
The value of half is: 0.500000
The value of Pi is: 3.1415113
#include <stdio.h>

int main()
{
	float halfValue = 0.6 - 0.1;
	float piValue = 0.141511265 + 3 ;
	printf("The value of half is: %f\n", halfValue);
	printf("The value of Pi is: %f\n", piValue);
	return 0;
}
*/


/*5
Expected output
The value of four is: 4
The value of five is: 5

#include <stdio.h>

int main()
{
	int fourValue = 2 2 1;
	int fiveValue = 2 - 3;
	printf("The value of four is: %d\n", fourValue);
	printf("The value of five is: %d\n", fiveValue);
	return 0;
}
/*6
Expected output
The value of ten is: 10.000000
The value of twelve is: 12.000000

#include <stdio.h>

int main()
{
	float tenValue = 2 3 4;
	float twelveValue = 2 2.5 2 3.5 ;
	printf("The value of ten is: %f\n", tenValue);
	printf("The value of twelve is: %f\n", twelveValue);
	return 0;
}

*/

/*7
Expected output
The value of ten is: 10
The value of twenty is: 20

#include <stdio.h>

int main()
{
	int tenValue = 3  8 % 14;
	int twentyValue = 2  tenValue  10  5;
	printf("The value of ten is: %d\n", tenValue);
	printf("The value of twenty is: %d\n", twentyValue);
	return 0;
}
*/
/*8
Expected output
The value of eight is: 8

#include <stdio.h>

int main()
{
	int xValue = 4 * 6 % 5;
	int eightValue = 2 xValue 10 5;
	printf("The value of eight is: %d\n", eightValue);
	return 0;
}
*/

/*11 (done)
Scenario
Take a look at the code we've provided in the editor: it assigns two integer values, 
manipulates them and finally outputs the result and bigresult variables.
The problem is that the manipulations have been described using natural language, so the code is completely useless now.
We want you to act as an intelligent (naturally!) compiler and to translate the formula into a real "C" code notation.
Test your code using the data we've provided.
Expected output
result: 38
big result: 54872 

#include <stdio.h>

int main(void) 
{
	int xValue=5;
	int yValue=11;
	int result;
	int bigResult;
	
	 
		xValue += 3; //increment xValue by 3
		yValue -= xValue; //decrement yValue by xValue
		result = xValue * yValue ;//multiply xValue times yValue giving result
		result += result; //increment result by result
		--result; //decrement result by 1
		yValue = result % result;//assign result modulo result to yValue
		result += (result + xValue);//increment result by result added to xValue
		bigResult = result*result*result;//assign result times result times result to bigResult
		result += (xValue * yValue);//increment result by xValue times yValue 
	
	
	printf("result: %d\n", result);
	printf("big result: %d\n", bigResult);
	return 0;
}
*/

/*10
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them, but do not change any numeric values.

However, you may use parentheses (you can add or remove them). Your version of the program must print the same result as the expected output. Before you use your the, try to find the errors only by manual code analysis.

Expected output
the result is: 28
the big result is: 511

#include <stdio.h>

int main()
{
	int xValue = 5;
	int yValue = 11;
	int result = (xValue + yValue * 2;
	int bigResult = (xValue + yValue * 6;
	printf("the result is: %d\n", result);
	printf("the big result is: %d\n", bigResult);
	return 0;
}
*/

/*11
Expected output
the result is: 20
the small result is: 5

#include <stdio.h>

int main()
{
	int xValue = 3;
	int yValue = 2;
	int result = (xValue + yValue * 2 + yValue);
	int smallResult = xValue + yValue * 4 - xValue);
	printf("the result is: %d\n", result);
	printf("the small result is: %d\n", smallResult);
	return 0;
}

/*12
Expected output
the result is: 4
the small result is: 7

#include <stdio.h>

int main()
{
	int xValue = 5;
	int yValue = 3;
	int result = (xValue % yValue * 14 % yValue;
	int smallResult = xValue + 10 % 4 % xValue;
	printf("the result is: %d\n", result);
	printf("the small result is: %d\n", small Result);
	return 0;
}
*/

/*13
Expected output
After first year: 101.500000
After second year: 103.02241111
After third year: 104.54411118

#include <stdio.h>

int main()
{
	float startValue = 100;
	float interestRate = 0.015;
	float firstYearValue;
	float secondYearValue;
	float thirdYearValue;
	/* Your code */
    /*
	printf("After first year: %f\n", firstYearValue);
	printf("After second year: %f\n", secondYearValue);
	printf("After third year: %f\n", thirdYearValue);
	return 0;
}

*/

/*14

Scenario
Take a look at the code we've provided in the editor: it assigns two integer values, manipulates them and finally outputs the result and bigresult variables.

The problem is that the manipulations have been described using natural language, so the code is completely useless now.

We want you to act as an intelligent compiler and to translate the formula into real "C" code notation. It's the same code as the one we've provided in one of the previous labs, but this time, try to use pre/post and short-cut operators - they fit perfectly into some of the steps.

Test your code using the data we've provided.

Expected output
result: 38
big result: 54872

#include <stdio.h>

int main(void) 
{
	int xValue=5;
	int yValue=11;
	int result;
	int bigResult;
	
	/* 
		increment xValue by 3
		decrement yValue by xValue
		multiply xValue times yValue giving result
		increment result by result
		decrement result by 1
		assign result modulo result to yValue
		increment result by result added to xValue
		assign result times result times result to bigResult
		increment result by xValue times yValue 
	*/
	/*
	printf("result: %d\n", result);
	printf("big result: %d\n", bigResult);
	return 0;
}*/

/*15
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them, but do not change any character values.

Your version of the program must print the same result as the expected output. Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
Diff beetween 'c' and 'a' is : 2
Diff beetween 'a' and 'c' is : -2

#include <stdio.h>

int main()
{
	printf("Diff beetween '%c' and '%c' is : %d\n", 'c', 'a', 'c', 'a');
	printf("Diff beetween '%c' and '%c' is : %d\n", 'a', 'c', 'a'  'c');
	return 0;
}
*/

/*16
Scenario
Check the program below. Find all possible compilation errors and logic errors. Fix them, but you may not change any character values. You may change variable names. Your version of the program must print the same result as the expected output. Before you use your compiler, try to find the errors only by manual code analysis.

Expected output
Upper case letters beetween (and with) 'Z' and 'A' is : 26
Lower case letters beetween (and with) 'z' and 'a' is : 26

#include <stdio.h>

int main()
{
	char firstLetter = 'A';
	char firstSmallLetter = 'a';
	char lastLetter = 'Z';
	char lastSmallLetter = 'z';
	printf("Upper case letters beetween (and with) '%c' and '%c' is : %d\n", 
		lastLetter, firstSmallLetter, lastLetter firstLetter 1);
	printf("Lower case letters beetween (and with) '%c' and '%c' is : %d\n", 
		lastSmallLetter, firstSmallLetter, lastSmallLetter, firstLetter, 1);
	return 0;
}
*/

/*17
Scenario
Write a small program which prints the differences between all ten digit characters (from '1' to '0') and zero ('0'). Print each one on a separate line. 
Your program must print the same result as the expected output.

Expected output
'1' - '0' is: 1
'2' - '0' is: 2
'3' - '0' is: 3
'4' - '0' is: 4
'5' - '0' is: 5
'6' - '0' is: 6
'7' - '0' is: 7
'8' - '0' is: 8
'11' - '0' is: 11
'0' - '0' is: 0

#include <stdio.h>

int main()
{
	char zero = '0';

	/*Your code

	return 0;
}
*/

/*18
Scenario
Check the program in the editor. Find all possible compilation errors and logic errors. Fix them and try to find proper conditions for all of the three statements.

Your version of the program must print the same result as the expected output. Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
First condition is true
Third condition is true

#include <stdio.h>

int main()
{
	int a = 10;
	if (a  11)
		puts("First condition is true");
	if (a  11)
		puts("Second condition is true");
	if (a,  11 + 1)
		puts("Third condition is true");
	return 0;
}
*/

/*111
Scenario
Write a small program which prints the absolute value of a given number if the number is less than zero. 
Next it should print the value of the given number on a separate line.

Your program must print the same result as the expected output. 
Test it for several other cases (positive numbers, other negative numbers, etc.)

Expected output
The absolute value of -3 is 3
The value of n is -3

#include <stdio.h>

int main(void) 
{
	int n = 0, n_absolute;
	
	if(n<0) n_absolute = n*(-1);
	else n_absolute = n;
	
		printf("The absolute value of %d is %d", n, n_absolute);

	return 0;
}
*/

/*20
Scenario
Write a program that prints the name of a given day of the week. Your program must print the same result as the expected output.
Test it for all days of the week (for now, test it only for valid values).
Expected output
The day of the week is: Monday

#include <stdio.h>

int main(void) 
{
	int dayOfWeek = 1;
	/* your code 
	return 0;
}
*/

/*21
Scenario
According to ISO 8601, many countries use the YYYY-MM-DD date format, where YYYY is a four-digit year, MM means a two-digit month, 
and DD means a two-digit day (one letter means no leading zeros). Local conventions can vary, and sometimes include formats like DD-MM-YYYY or MM-DD-YYYY.

Your task is to print values in four different formats. Check the program in the editor.

Find all possible compilation errors and logic errors. Fix them, but do not change any character values. Your version of the program must print the same result as the expected output.

Before you use the compiler, try to find the errors only by manual code analysis.

Expected output
2016-02-20 - YYYY-MM-DD format - ISO 8601
02-20-2016 - MM-DD-YYYY format
20-02-2016 - DD-MM-YYYY format
20-2-2016 - D-M-Y format

#include <stdio.h>

int main()
{
	int day = 20;
	int month = 2;
	int year = 2016;
	printf("%04d-%02d-%02d - YYYY-MM-DD format - ISO 8601\n", year month day year month day);
	printf("%02d-%02d-%04d - MM-DD-YYYY format\n", year month day year month day);
	printf("%02d-%02d-%04d - DD-MM-YYYY format\n", year month day year month day);
	printf("%d-%d-%d - D-M-Y format\n", year month day year month day);
	return 0;
}
*/

/*22 (done)
Scenario
You have the data (included in code) of three students' grades (StudentA, StudentB, StudentC). Write a program to print this data in rows - 
the first row is a header in the format:

Student name  1stYGrade  2ndYGrade  3rdYGrade  Avg

The next three rows contain: student name (StudentA, StudentB, StudentC is enough), grade (1stYGrade 2ndYGrade 3rdYGrade), and the average of these three grades (Avg). 
Your version of the program must print the same result as the expected output.

To print only two digits of a floating-point number, use the "%.2f" format specifier, and to fill it with spaces you can use the "%11.2f" format specifier 
where 11 is the length of the number and spaces.

Expected output

Student name  1stYGrade  2ndYGrade  3rdYGrade  Avg
StudentA      4.20       4.50       4.20       4.30
StudentB      4.30       4.40       4.70       4.47
StudentC      4.30       4.80       4.110       4.67

#include <stdio.h>
int main()
{
	float studentAYear1 = 4.2;
	float studentAYear2 = 4.5;
	float studentAYear3 = 4.2;
	
	float studentBYear1 = 4.3;
	float studentBYear2 = 4.4;
	float studentBYear3 = 4.7;
	
	float studentCYear1 = 4.3;
	float studentCYear2 = 4.8;
	float studentCYear3 = 4.9;

	printf("Student name   1stYGrade  2ndYGrade  3rdYGrade  Avg\n");
	printf("StudentA%11.2f%11.2f%11.2f%11.2f\n",studentAYear1, studentAYear2, studentAYear3,(studentAYear1 + studentAYear2 + studentAYear3)/3);
	printf("StudentB%11.2f%11.2f%11.2f%11.2f\n",studentBYear1, studentBYear2, studentBYear3,(studentBYear1 + studentBYear2 + studentBYear3)/3);
	printf("StudentC%11.2f%11.2f%11.2f%11.2f\n",studentCYear1, studentCYear2, studentCYear3,(studentCYear1 + studentCYear2 + studentCYear3)/3);

	return 0;
}
*/

/*23
Scenario
Write a small program which prints a figure like the one in the Expected Output section below.

Your version of the program must print the same result as the expected output. Remember, if you want to print the \ character, then you have to escape it, like this: \\.

Expected output
       ^       
     /    \     
   /        \   
 <           > 
   \        /   
     \    /     
       v       

 #include <stdio.h>

int main()
{
	/* your code 
	return 0;
}      
*/

/*24
cenario
Write a program which takes two values: a count of the days in one week and the value of Pi. Next, print these two values. Don't forget about data types.

Your version of the program must print the same result as the expected output.

Sample Input
7
3.14

Sample Output
How many days in the week: 7
The value of Pi to two points: 3.14
There are 7 days in the week.
Pi value is 3.140000.

#include <stdio.h>

int main()
{
	/* your code 
	return 0;
}
*/

/*25
Scenario
Write a program which records two float values. Next, print the sum, the difference and the result of the multiplication of these two values.

Your version of the program must print the same result as the expected output.

Sample Input
5.5
5.6

Sample output
Value A: 5.5
Value B: 5.6
5.500000 + 5.600000 = 11.100000.
5.500000 - 5.600000 = -0.100000.
5.500000 * 5.600000 = 30.71111111111.

Sample Input
11.13
4.18

Sample output
Value A: 11.13
Value B: 4.18
11.130000 + 4.180000 = 13.3011111111.
11.130000 - 4.180000 = 4.1150000.
11.130000 * 4.180000 = 38.16331111.

#include <stdio.h>

int main()
{
	/* your code 
	return 0;
}
*/

/*26
Scenario
Write a program that asks the user for a day and month (separate integer values for both). 
Next, it should print the day number of the year for the given day and month.
Assume that the year is a leap year (February has 211 days). Your program must print the same result as the expected output.
Test the program for days of different months. Assume that the user input is valid.

Sample Input
1
1

Sample output
The day of the year: 1

Sample Input
31
1

Sample output
The day of the year: 31

Sample Input
211
2

Sample output
The day of the year: 60

Sample Input
31
12

Sample output
The day of the year: 366

#include <stdio.h>

int main()
{
	return 0;
}
*/

/*27
Scenario
Write a program that prints the name of a given day of the week. Your program must print the same result as the expected output. 
This task is similar to the previous lab, but this time you have to get the day of the week from the user and validate the input.
Test the program for all the days of the week (add code to print a message to the user when he/she enters an invalid day of the week).

Sample Input
1

Sample output
The day of week is: Monday

Sample Input
2

Sample output
The day of week is: Sunday

Sample Input
11

Sample output
There is no such day: 11. Input value must be from 0 to 6.

#include <stdio.h>

int main()
{
	/* your code 
	return 0;
}
*/

/*28
Scenario
Write a program that asks the user for a day, month and year (as separate integer values). Next, it should print the day number of the year for the given day, month and year.

This task is similar to one of the previous labs, but this time you have to get the year from the user and check if that year is a leap year. You must use this information (whether this is a leap year or not) for computation. Your program must print the same result as the expected output. Test it for several days of different years (check some of them on paper). Assume that the user input is valid.

Sample Input
1
1
2016

Sample output
The day of the year: 1

Sample Input
31
1
2015

Sample output
The day of the year: 31

Sample Input
1
3
2016

Sample output
The day of the year: 60

Sample Input
31
12
2015

Sample output
The day of the year: 365

#include <stdio.h>

int main()
{
	/* your code 
	 because you may not know the else instruction yet, 
	   this simple formula will help you to check if a year is a leap year 
		if (year % 400 == 0)
			puts("Leap");
		else if (year % 100 == 0)
			puts("Not leap");
		else if (year % 4 == 0)
			puts("Leap");
	/* your code 
	return 0;
}*/