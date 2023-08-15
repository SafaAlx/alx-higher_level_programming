#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - function thet prints some basic
 *                                                   info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python list = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((pyListObjet *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n",elem, Py_TYPE(PyList_Getltem(p, elem)
}
