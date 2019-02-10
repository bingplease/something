#include "stdafx.h"


int main(void)
{
	char op;
	double int1 = 0;
	double int2 = 0;
	double awnser = 0;

	printf("Enter first number here\n");
	scanf("%lf", &int1);

	printf("Enter +,-,*,/\n");
	scanf("%c", &op);
	op = getchar();

	printf("Enter second number here\n");
	scanf("%lf", &int2);
	
	if (op == '+')
		awnser = int1 + int2;
	else if (op == '-')
		awnser = int1 - int2;
	else if (op == '*')
		awnser = int1 * int2;
	else if (op == '/')
		awnser = int1 / int2;
	printf("Awnser is %.3f\n", awnser);
	return 0;
}

