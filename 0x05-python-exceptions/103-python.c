#include <Python.h>

/**
 * print_python_list - the func prints info about python lists
 * @p: PyObject
 * Return: returns void
*/

void print_python_list(PyObject *p)
{
	PyObject *obj;
	PyListObject *list;
	Py_ssize_t len, idx;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	len = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (idx = 0; idx < len; idx++)
	{
		obj = list->ob_item[idx];
		printf("Element %ld: %s\n", idx, object->ob_type->tp_name);
		if (PyBytes_Check(obj))
		print_python_bytes(obj);
	}
}


/**
 * print_python_bytes - the func prints info about python lists
 * @p: PyObject
 * Return: returns void
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	char *string;
	Py_ssize_t len, idx;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	len = bytes->ob_base.ob_size;
	string = bytes->ob_sval;
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", string);
	if (len > 10)
		len = 10;
	else
		len++;
	printf("  first %ld bytes: ", len);
	for (idx = 0; idx < len; idx++)
	{
		printf("%02hhx", string[idx]);
		if (idx == (len - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - the func prints info about python lists
 * @p: PyObject
 * Return: returns void
*/
void print_python_float(PyObject *p)
{
	PyFloatObject *floats;
	char *str;
	double value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	floats = (PyFloatObject *)p;
	value = floats->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
