#include <Python.h>

/**
 * print_python_list_info - func that prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: returns void
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int size, alloc_space, i;

	size = PyList_Size(p);
	alloc_space = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc_space);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
