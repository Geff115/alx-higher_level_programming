#include "lists.h"
/**
 * is_palindrome - This function checks if a
 * singly linked list is a palindrome.
 * I used an algorithm called: The Tortoise and the Hare method.
 * Time complexity of the program is O(n).
 * @head: This is the starting point of the linked list.
 * @slow: A pointer that is slow i.e The Tortoise.
 * @fast: A pointer that is fast i.e The Hare.
 *
 * Return: Always (0) success.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *current, *next;

	slow = *head;
	fast = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	prev = NULL;
	current = slow;
	next = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	while ((*head != NULL) && (prev != NULL))
	{
		if ((*head)->n == prev->n)
		{
			*head = (*head)->next;
			prev = prev->next;
			continue;
		}
		else
			return (0);
	}
	return (1);
}
