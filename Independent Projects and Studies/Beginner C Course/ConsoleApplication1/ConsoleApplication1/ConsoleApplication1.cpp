# include <stdio.h>

int main()
{
	int val, ln, hn;

	printf("Please enter a number smaller than 256:\n");
	scanf("%d", &val);

	ln = val & 15;
	hn = (val & 240) >> 4;

	printf("H nibble: %d\nL nibble %d", hn, ln);

	return 0;
}