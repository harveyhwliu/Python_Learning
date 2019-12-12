#include <Python.h>
//Python.h头文件中包含了所有需要的类型(Python对象类型的表示)和函数定义(对Python对象的操作)

//编写将要在Python调用的函数, 函数传统的命名方式由{模块名}_{函数名}组成，所以我们将其命名为addList_add
//参数类型为PyObject类型结构(同时也表示为元组类型，因为Python中万物皆为对象，所以我们先用PyObject来定义)
static PyObject* addList_add(PyObject* self, PyObject* args){

    PyObject * listObj;

    //传入的参数则通过PyArg_ParseTuple()来解析。
    //第一个参数是被解析的参数变量。第二个参数是一个字符串，告诉我们如何去解析元组中每一个元素。
    //字符串的第n个字母正是代表着元组中第n个参数的类型。例如，"i"代表整形，"s"代表字符串类型, "O"则代表一个Python对象。
    //接下来的参数都是你想要通过PyArg_ParseTuple()函数解析并保存的元素。这样参数的数量和模块中函数期待得到的参数数量就可以保持一致，并保证了位置的完整性。
    /*
    例如，我们想传入一个字符串，一个整数和一个Python列表，可以这样去写
        int n;
        char *s;
        PyObject* list;
        PyArg_ParseTuple(args, "siO", &n, &s, &list);
    */
    if (! PyArg_ParseTuple( args, "O", &listObj ))
        return NULL;
    long length = PyList_Size(listObj);
    int i, sum =0;
    for (i = 0; i < length; i++) {
        //通过循环列表，使用PyList_GetItem(list, index)函数来获取每个元素。这将返回一个PyObject*对象。
        PyObject* temp = PyList_GetItem(listObj, i);
        //既然Python对象也能表示PyIntType，我们只要使用PyInt_AsLong(PyObj *)函数便转成C中的long对象
        long elem = PyInt_AsLong(temp);
        sum += elem;
    }
    //总和将被转化为一个Python对象并通过Py_BuildValue()返回给Python代码，这里的i表示我们要返回一个Python整形对象
    return Py_BuildValue("i", sum);

}

//This is the docstring that corresponds to our 'add' function.
static char addList_docs[] =
"add(  ): add all elements of the list\n";

/* This table contains the relavent info mapping -
   <function-name in python module>, <actual-function>,
   <type-of-args the function expects>, <docstring associated with the function>
 */
static PyMethodDef addList_funcs[] = {
    {"add", (PyCFunction)addList_add, METH_VARARGS, addList_docs},
    {NULL, NULL, 0, NULL}

};

/*
   填写想在模块内实现函数的相关信息表，每行一个函数，以空行作为结束 - 最后的模块初始化块签名为PyMODINIT_FUNC init{模块名}。
   <模块名>, <相关信息表>, <模块的文档>
 */
PyMODINIT_FUNC initaddList(void){
    Py_InitModule3("addList", addList_funcs,"Add all ze lists");

}

