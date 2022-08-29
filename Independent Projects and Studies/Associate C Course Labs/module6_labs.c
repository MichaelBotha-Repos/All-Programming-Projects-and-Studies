/*1
Write a program that creates the first names and last names of four people and then prints them. 
Create the appropriate structure.
Then create one variable for each person, initialize their values with a constant 
value (from the code - don't interact with the user this time).

Finally, print each of them on a separate line.

Your version of the program must print the same result as the expected output.

Expected output
Mary Smith 
James Johnson
Patricia Williams
John Brown 
*/
/*
#include <stdio.h>
struct NAME
{
	char first[20];
	char last[20];

};

int main()
{
	struct NAME a = {"Mary", "Smith"}, b ={"James", "Johnson"}, c = {"Patricia", "Williams"}, d= {"John", "Brown"};
    struct NAME names[] = {a, b, c, d};

    for(int i=0; i<4; i++)
	{
		printf("%s %s\n", names[i].first, names[i].last);

	}

	return 0;

}
*/
/*2
Check the program in the editor. Add code to print all the neighbors in ascending and descending order. Use only pointers and loops 
(don't use the houseX variables).

Your version of the program must print the same result as the expected output.

Expected output
Ascending order:
1
3
5
7
Descending order:
7
5
3
1
*/
/*
#include <stdio.h>
#include <stdlib.h>

struct house
{
	int houseNumber;
	struct house *previous;
	struct house *next;
};

int main(void)
{
	struct house house1;
	struct house house2;
	struct house house3;
	struct house house4;
	house1.houseNumber = 1;
	house2.houseNumber = 3;
	house3.houseNumber = 5;
	house4.houseNumber = 7;
	house1.next = &house2;
	house2.next = &house3;
	house3.next = &house4;
	house4.next = NULL;
	house1.previous = NULL;
	house2.previous = &house1;
	house3.previous = &house2;
	house4.previous = &house3;
	struct house *firstHouse = &house1;
	struct house *lastHouse = &house4;
	struct house *current;
	
	current = firstHouse;

	printf("Ascending Order:\n");
	while(current != NULL)
	{
		printf("%i\n", current->houseNumber);
		current = current -> next;

	}
	printf("Descending Order:\n");
	current = lastHouse;
	while(current != NULL)
	{
		printf("%i\n", current->houseNumber);
		current =  current -> previous;
	}

	return 0;
}
*/


/*3
Write a program that creates a FIFO queue and prints some values. 
For this lab, use structures, pointers to structures and the malloc function.
Use the values from the array included in the code fragment. 
Create one element of a queue for one element of an array (there are ten elements).
After you have created the list, print the first five values of the queue and then the first seven values of the queue. 
Free up the memory.
After all the operations have been completed, print the message: Memory is freed..
Your version of the program must print the same result as the expected output.

Expected output
First 5 values
2
4
5
6
7
First 7 values
2
4
5
6
7
8
9
Memory is freed
*/
/*
#include <stdio.h>
#include <stdlib.h>

struct element
{
	int value;
	struct element *next;
};

int main(void)
{
	int values[10] = {2, 4, 5, 6, 7, 8, 9, 1, 3, 0};
	struct element *elem1, *elem2, *elem3, *elem4, *elem5, *elem6, *elem7, *elem8, *elem9, *elem10, *current;

	elem1 = (struct element *) malloc(sizeof(struct element));
	elem2 = elem1-> next = (struct element *) malloc(sizeof(struct element));
	elem3 = elem2-> next = (struct element *) malloc(sizeof(struct element));
	elem4 = elem3-> next = (struct element *) malloc(sizeof(struct element));
	elem5 = elem4-> next = (struct element *) malloc(sizeof(struct element));
	elem6 = elem5-> next = (struct element *) malloc(sizeof(struct element));
	elem7 = elem6-> next = (struct element *) malloc(sizeof(struct element));
	elem8 = elem7-> next = (struct element *) malloc(sizeof(struct element));
	elem9 = elem8-> next = (struct element *) malloc(sizeof(struct element));
	elem10 = elem9-> next = (struct element *) malloc(sizeof(struct element));
	elem10-> next = NULL;
	current = elem1;

	for(int i =0; i<10; i++)
	{
		current -> value = values[i];
		current = current -> next;

	}

	current = elem1;
	for(int j =0; j<5; j++)
	{
		printf("%i",current->value);
		current = current -> next;

	}


	return 0;
}
*/

/*4
Write a function that computes the square of a given floating-point number and returns its value. 
Separate the declaration of the function from its full definition.

Write a test code to test the function with some values. Do not limit yourself only to those values we've provided you.

Expected output
square of 2.00 is 4.00
square of 6.00 is 36.00
square of 2.50 is 6.25
square of 12.12 is 146.89
square of 345.68 is 119493.29
*/
/*
#include <stdio.h>

float square(float val)
{
	return (val * val);
}

int main()
{
	float values[] = {2, 6, 2.5, 12.12, 345.68};

	for(int i=0; i < 5; i++)
	{
		printf("square of %.2f is %.2f \n", values[i], square(values[i]));

	}

	return 0;
}

*/

/*5
Write a function that checks whether or not a given string is a valid IP address (in human-readable form, of course). 
This function should return 1 if the address is valid, and 0 if not.

Your function should check if:

there are four parts in the string, separated by dots;
each part contains only digits,
each number is in the range of 0 to 255, inclusive.
For converting string fragments to integer values you can use the strtol, atoi or sscanf functions. 
Separate the declaration of the function from its full definition.

Write a second function that calls the first one and then prints an appropriate message: 
127.0.0.1 is a valid IP address or a.b.c.d is not a valid IP address.

Write a test code to test the function with some values - call a second function. 
Do not limit yourself only to those values we've provided you.

Expected output
127.0.0.1 is a valid IP address
127.0.01 is not a valid IP address
127.0..1 is not a valid IP address
127.zero.0.1 is not a valid IP address
127.297.0.1 is not a valid IP address
127.2555.0.1 is not a valid IP address
*/
/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int check_valid_ip(char ip_str[])
{
	char octet[4], *octet_ptr;
	int ip[4], cntr=0;

	octet_ptr = ip_str;

	for(int i=0; i<15; i++)
	{
		if(ip_str[i]== 46)
		{
			strncpy(octet, octet_ptr , &ip_str[i] - octet_ptr);
			ip[cntr] = atoi(octet);
			if(ip[cntr]<0 || ip[cntr]>255)
			{
				return 0;
			}
			octet_ptr = &ip_str[i] + 1;
			cntr++;
		}
		else if(ip_str[i]== 0)
		{
			strncpy(octet, octet_ptr , &ip_str[i] - octet_ptr);
			ip[i] = atoi(octet);
			cntr++;
			break;
		}
	}
	if(cntr!= 4)
	{
		return 0;
	}

	return 1;
}

void check_response(char ip_str[])
{
	int result = check_valid_ip(ip_str);

	if(result ==1)
	{
		printf("%s is a valid ip address", ip_str);

	}
	else
	{
		printf("%s is not a valid ip address", ip_str);

	}


}
int main()
{	
	char ip_str[16]; 
	int result;
	

	printf("Please enter an IP address:\n");
	scanf("%s", ip_str);
	check_response(ip_str);
	
	return 0;
}
*/

/*6
Write a function that checks which of two given matrices is greater. 
To simplify the function parameter list, you can assume that both matrices are equal in size and are square.

This function should return:

1 if the first matrix is greater than the second;
-1 if the first matrix is smaller than the second;
0 if both matrices are equal - this means they have exactly the same values.
For this task, we assume that a matrix is smaller than another matrix when the first element which is different is smaller in that matrix.

We analyze matrices from left to right and from top to bottom. 
Separate the declaration of the function from its full definition.

Write a second function that calls the first one and then prints an appropriate message: matrixA is smaller than matrixB, 
matrixA is greater than matrixB, or Both matrices are equal.

Write a code to test it with some values - create three matrices, fill them with values and compare them in all possible (six) cases. 
Call a second function. As always, do not limit yourself only to the cases already given.

Note: you can use a single pointer to int type to pass the array.

Expected output
Both matrices are equal.
matrixA is smaller than matrixB
matrixA is greater than matrixB
Both matrices are equal.
matrixA is smaller than matrixB
matrixA is greater than matrixB
*/
/*
#include <stdio.h>

int matrix_analyser(int * m1, int * m2)
{
	for(int i=0; i<9; i++)
	{
		printf("%i --> %i",*(m1+i), *(m2+i));
		if(*(m1+i) > *(m2+i))
		{
			return 1;
		}
		else if (*(m1+i) < *(m2+i))
		{
			return -1;
		}

	}

	return 0;

}

int main()
{
	int matrix_a[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
	int matrix_b[3][3] = {{1,2,1}, {4,5,6}, {7,8,9}};
	int result;

	result = matrix_analyser(matrix_a, matrix_b);
	printf("%i", result);

	return 0;
}
 
*/

/*7
Write a program that allows the user to pass the parameters to be executed and compute the results of some mathematical operations.

Your program should support the following operations:

add
sub
mul
All operations require additional two arguments. Some examples of program calls inlude:

program.exe add 1 3
program.exe sub 2 3
program.exe mul 2 5
When there are no parameters, the parameters contain the wrong numbers or a parameter is invalid, the program should print the message: Wrong parameters (or you can think about your own message with regard to the proper form of program execution).

The first parameter must be one of the three previous strings, while the second and third parameters must be integer numbers. To find out which of the commands has been passed, you may use the strcmp function.

Your version of the program must print the same result as the expected output.

This is one of the tasks which can only be executed in your personal environment. If you use an IDE, you can check the options of debug/execute to pass the arguments.

You don't always need to run the program from outside the IDE.

Sample input
add 1 3

Expected output
add 1 3: 4

Sample input
sub 2 3

Expected output
sub 2 3: -1

Sample input
mul 2 5

Expected output
mul 2 5: 10
*/
/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int add(int val1, int val2)
{
	return (val1+val2);
}
int sub(int val1, int val2)
{
	return (val1-val2);
}
int mul(int val1, int val2)
{
	return (val1*val2);
}

int main(int argc, char *argv[])
{
	char val1[5], val2[5];
	char val1_int, val2_int;
	if(argc > 1)
	{
		strcpy(val1, argv[2]);
		strcpy(val2, argv[3]);
		val1_int = atoi(val1);
		val2_int = atoi(val2);


		if(!(strcmp(argv[1], "mul")))
		{
			printf("Multiply");
			printf(" :%i", mul(val1_int, val2_int));
		}
		else if(!(strcmp(argv[1], "add")))
		{
			printf("Add");
			printf(" :%i", add(val1_int, val2_int));
		}
		else if(!(strcmp(argv[1], "sub")))
		{
			printf("Subtract");
			printf(" :%i", sub(val1_int, val2_int));
		}
		else
		{
			printf("Incorrect operation");

		}

	}
	return 0;
}
*/

/*8
Write a program that prints two triangles: one is a normal triangle consisting of backslashes and the other is a Floyd's triangle.

Remember to escape the backslash with a backslash (not a play on words!).

A Floyd's triangle consisting of numbers in consecutive order: in the first row, we have only one number:
 1; in the second row, two numbers: 2 3; in the third row: 4 5 6 and so on.

Your program should ask the user for the size of both triangles (just one number - the triangles should be the same size).

After that, your program should print both triangles. To print the Floyd's triangle, you may use the "%3d" format in the printf function.

Divide your program into files: one file for the classic triangle function, one for the Floyd's triangle function, 
one header file with the prototypes of both functions, and finally a file with the main function.

Practice adding and removing files from your program/project/solution. 
If you can, test it in different environments (different OS/different IDE/no IDE).

Your version of the program must print the same result as the expected output.

Note: not all online compilers allow you to create a project of many files.

Sample input
15

Expected output
\
\\
\\\
\\\\
\\\\\
\\\\\\
\\\\\\\
\\\\\\\\
\\\\\\\\\
\\\\\\\\\\
\\\\\\\\\\\
\\\\\\\\\\\\
\\\\\\\\\\\\\
\\\\\\\\\\\\\\

  1
  2    3
  4    5   6
  7    8   9  10
  11  12  13  14  15
  16  17  18  19  20  21
  22  23  24  25  26  27  28
  29  30  31  32  33  34  35  36
  37  38  39  40  41  42  43  44   45
  46  47  48  49  50  51  52  53   54   55
  56  57  58  59  60  61  62  63   64   65   66
  67  68  69  70  71  72  73  74   75   76   77   78
  79  80  81  82  83  84  85  86   87   88   89   90   91
  92  93  94  95  96  97  98  99  100  101  102  103  104  105

Sample input
5

Expected output
\
\\
\\\
\\\\

  1
  2   3
  4   5   6
  7   8   9  10

#include <stdio.h>
// your code that includes a header

int main()
{
	// your code 
	return 0;
}
// other files with your code 
*/