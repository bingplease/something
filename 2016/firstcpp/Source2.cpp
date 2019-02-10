#include "stdafx.h"
//#include <string>
#include <string.h>
#include <string>
#include <math.h>
#include <list>

void test1()
{
	unsigned long num1;
	unsigned long num2;

	printf("Enter two numbers");

	scanf("%lu%lu", &num1, &num2);

	if (num1 == num2) {
		printf("%lu is equal to %lu\n", num1, num2);
	}

	if (num1 != num2) {
		printf("%lu is not equals to %lu\n", num1, num2);
	}

	if (num1 < num2) {
		printf("%lu is less than %lu\n", num1, num2);
	}

	if (num1 > num2) {
		printf("%lu is greater than %lu\n", num1, num2);
	}
}
void test3() {

	char shapetype[65536];

	while (true)
	{
		puts("Hex,Squ,Tri,Pen - enter x to exit");
		scanf("%s", &shapetype);


		if (strcmp(shapetype, "x") == 0)
			return;
		else if (strcmp(shapetype, "squ") == 0) {
			while (true)
			{
				puts("dia,rec,squ - enter q to return, x to exit");
				scanf("%s", &shapetype);

				if (strcmp(shapetype, "q") == 0)
					break;
				else if (strcmp(shapetype, "x") == 0)
					return;
				else if (strcmp(shapetype, "squ") == 0) {
					printf("* * * * \n*     * \n*     *\n* * * *\n");
				}
				else if (strcmp(shapetype, "rec") == 0) {
					printf("* * * * * *\n*         *\n* * * * * *\n");
				}
				else if (strcmp(shapetype, "dia") == 0) {
					printf(
						"   *   \n"
						"  * *  \n"
						" *   * \n"
						"*     *\n"
						" *   * \n"
						"  * *  \n"
						"   *   \n");
				}


			}
		}
		else if (strcmp(shapetype, "tri") == 0) {
			while (true)
			{
				puts("rig,equ,isc - enter q to return, x to exit");
				scanf("%s", &shapetype);
				if (strcmp(shapetype, "q") == 0)
					break;
				else if (strcmp(shapetype, "x") == 0)
					return;
				else if (strcmp(shapetype, "rig") == 0) {
					printf(
						"*        \n"
						"* *      \n"
						"*   *    \n"
						"*     *  \n"
						"* * * * *\n");
				}
				else if (strcmp(shapetype, "equ") == 0) {
					printf(
						"   *   \n"
						"  * *  \n"
						" *   * \n"
						"* * * *\n");
				}
				else if (strcmp(shapetype, "isc") == 0) {
					printf(
						"  *  \n"
						"  *  \n"
						" * * \n"
						" * * \n"
						"* * *\n");
				}
			}
		}
		else if (strcmp(shapetype, "pen") == 0) {
			printf(
				" * * *\n"
				" *     *\n"
				" *       *\n"
				" *     *\n"
				" * * *\n");
		}
		else if (strcmp(shapetype, "hex") == 0) {
			printf(
				"  * * *  \n"
				" *     * \n"
				"*       *\n"
				" *     * \n"
				"  * * *  \n");
		}
	}

}
void test4()
{
	unsigned int x = 1, total = 0, y;

		while (x <= 487)
		{
			y = x * x;
			printf("%d\n", y);
			total += y;
			++x;
		}

	printf("Total is %d\n", total);
}

void test5()
{
	int num1;
	int num2;
	unsigned long long int result;

	printf("Enter 2 numbers");
	scanf("%d%d", &num1, &num2);

	printf("res = %ld", pow(num1, num2));

	result = 1;
	for (int i = 0; i < num2; i++) {
		result = result*num1;
	}
	printf("%ld", result);

}
//void test6()
//{
//																																																																																													00000000
//																																																																																													 0      0
//																																																																																													  0      0
//																																																																																													   0	  0
//																																																																																														0	   0
//																																																																																														 0		0
//																																																																																														  0000000000000000000000000000000000000
//																																																																																														0                                      0000000
//																																																																																													0		                                        000000000
//																																																																																														0                                           00000000000
//																																																																																													0			                                    000000000
//																																																																																														0                                      0000000
//																																																																																														  0000000000000000000000000000000000000
//																																																																																														 0      0
//																																																																																														0      0
//																																																																																													   0      0
//																																																																																													  0      0
//																																																																																													 0      0
//																																																																																													00000000
//}
void test7() {
	
	std::list<std::string> things;
	things.push_back("apple");
	things.push_back("noodles");
	things.push_back("chicken");
	things.push_back("soup");


}



int main(void)
{
	//test1();
	//test2();
	//test3();
	//test4();
	//test5();
	//test6();
	test7();
}
