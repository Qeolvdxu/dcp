#include <iostream>

int main(void)
{
	bool status = false;
	
	int k;
	std::cout << "Enter the number for k\n";
	std::cin >> k;

	int array [5];
	std::cout << "Enter 5 numbers with spaces in between\n";
	for (int i = 0; i < 5; i++)
	{
		std::cin >> array[i]; 
	}
		
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (array[i] + array[j] == k)
			status = true;
		}
	}
	
	if (status == true)
		std::cout << "True\n";
	else
		std::cout << "False\n";
	
	return 0;
}
