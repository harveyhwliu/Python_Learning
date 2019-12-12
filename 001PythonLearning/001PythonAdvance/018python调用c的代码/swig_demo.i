%module swig_demo

%{
#define SWIG_FILE_WITH_INIT
#include <time.h>
#include "swig_demo.h"
%}

int fact(int n);
int my_mod(int x, int y);
char *get_time(void);
