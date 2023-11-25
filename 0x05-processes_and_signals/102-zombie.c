#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop.
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - Entry point of the program.
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			/* Child process */
			exit(0);
		}
		else if (child_pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			/* Error handling */
			perror("fork");
			exit(1);
		}
	}

	/* Function to keep the program running */
	infinite_while();

	return (0);
}
