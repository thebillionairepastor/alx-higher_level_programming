#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - unction in C that checks if a
 * singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int i = 0;
    int j;
    int count = 0;
	listint_t *front, *rear;

	while (i != count / 2)
	{
		front = rear = head;
		for (j = 0; j < i; j++)
		{
			front = front->next;
		}
		for (j = 0; j < count - (i + 1); j++)
		{
			rear = rear->next;
		}
		if (front->n != rear->n)
		{
			return (0);
		}
		else
		{
			i++;
		}
	}
	return (1);
}

/**
 * reverse_listint -  function that reverses a linked list.
 * @head: list header.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *first;
	listint_t *rest;

	if (*head == NULL)
		return (NULL);
	first = *head;
	rest = first->next;
	if (rest == NULL)
		return (NULL);
	reverse_listint(&rest);
	first->next->next = first;
	first->next = NULL;
	*head = rest;
	return (*head);
}
