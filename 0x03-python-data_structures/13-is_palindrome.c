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
	listint_t **headr;
	listint_t *tmp;
	unsigned int n, sum1 = 0, sum2 = 0;

	current = *head;
	headr = head;
	n = 0;
	sum1 = 0;
	sum2 = 0;
	while (current != NULL)
	{
		sum1 += (current->n + n);
		current = current->next;
		n++;
	}
	tmp = reverse_listint(headr);
	n = (n - 1);
	while (tmp != NULL)
	{
		sum2 += (tmp->n + n);
		tmp = tmp->next;
		n--;
	}
	if (sum1 == sum2)
		return (1);
	else
		return (0);
}

/**
 * reverse_listint - Function to reverse a linked list.
 * @head: The linked list
 *
 * Return: the pointer to the first element
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp, *prev;

	prev = NULL;
	while (*head != NULL)
	{
		tmp = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = tmp;
	}
	*head = prev;
	return (*head);
}
