#include "lists.h"

/**
 * check_cycle - checks the cycle of the linked list
 * @list: the list for the link list
 * Return: returns 1 if there is a cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *one_node = list;
	listint_t *two_node = list;

	while (one_node && two_node && two_node->next)
	{
		one_node = one_node->next;
		two_node = two_node->next->next;
		if (one_node == two_node)
		{
			return (1);
		}
	}
	return (0);
}
