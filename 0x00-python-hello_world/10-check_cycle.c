#include "lists.h"

/**
 * check_cycle - check a cycle in the linked list
 * @list: The linked list to check
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);
	listint_t *c = list, *n = list;

	c = c->next;
	n = n->next->next;
	while (n && n->next)
	{
		if (c == n)
			return (1);
		c = c->next;
		n = n->next->next;
	}

	return (0);
}
