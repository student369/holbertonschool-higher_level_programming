#include <stdio.h>
#include "listobject.h"
#include "object.h"
/**
 * print_python_list_info - prints some basic info about Python list.
 *
 * Return: Always 0.
 */
void print_python_list_info(PyObject *p)
{
	printf("%s", p->ob_type);
}
