#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: The head of the linked list.
 * @number: The integer to be added.
 *
 * Description: This function take in a pointer of a pointer to the head
 * of a singly sorted linked list and an integer. Then added the integer as a
 * new node.
 *
 * Return: A pointer to the new added node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow, *fast, *new_node;
	slow = *head;
	fast = (*head)->next;
	/** ALLOCATE MEMORY FOR THE NEW NODE */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	while (slow != NULL)
	{
		if (slow->n < number && fast->n > number)
		{
			new_node->n = number;
			slow->next = new_node;
			new_node->next = fast;
			return new_node;
		}
		slow = slow->next;
		fast = fast->next;
	}
	new_node->n = number;
	new_node->next = NULL;
	*head = new_node;
	return new_node;
}
