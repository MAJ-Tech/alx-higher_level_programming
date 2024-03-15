#include <stdio.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 is there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;
	/** THis is to **/
	if (slow == NULL || slow->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
