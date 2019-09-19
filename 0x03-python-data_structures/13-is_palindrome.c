#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: The linked list
 * Author: Jose Calderon <jose.calderon@holbertonschool.com>
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	listint_t *tmp;
	int *numbers;
	unsigned int n, i = 0, sum = 0;

	current = *head;
	tmp = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	numbers = (int *)malloc(sizeof(int) * n);
	while (tmp != NULL)
	{
		numbers[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (i = 0; i < n; i++)
	{
		if (numbers[i] == numbers[((n - 1) - i)])
		{
			sum -= -1;
		}
	}
	free(numbers);
	if (sum == n)
		return (1);
	else
		return (0);
}
