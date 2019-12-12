# Python 编码规范与风格


目录：

[TOC]


## 介绍

本规范基于[pep8](https://www.python.org/dev/peps/pep-0008/) 中包含的内容，修改了陈旧的规则，丰富了示例，以及结合平时开发工作中遇到的各种不规范操作，进行了总结形成。

在开源协同的大背景下，一些项目往往是多名开发者（同一组织或者不同组织）共同的智慧结晶。为使我们的工作成果能够更好地维护下去，需要大家共同遵守一些编码规范与风格。

## 代码布局

规范地代码布局有助于帮助开发者更容易地理解业务逻辑，请瑞雪编程，可持续开发。

### 缩进

对于每级缩进，统一要求使用4个空格。

续行，要求使用括号等定限界符，并且需要垂直对齐。

***正确示范***

```python
# 与定界（括号）符对齐
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 换行并增加4个额外的空格（一级缩进）
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 悬挂需要增加一级缩进
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

***错误示范***

```python

# 当不使用垂直对齐时，第一行不允许加参数
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 下面这种情况，需要增加额外的缩进，否则无法区分代码所在的缩进级别
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

```

如果包含定界符（括号，中括号，大括号）的表达式跨越多行，那么定界符的扩回符，可以放置与最后一行的非空字符对齐或者与构造多行的开始第一个字符对齐。

```python
# 与最后一行的非空字符对齐
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# 或者与开始构造多行的第一个字符对齐

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```


### if 判断语句的缩进

对于 If 判断，一般来说尽量不要放置过多的判断条件。
代码示例说明：

***正确示范***

```python
# 与定界符（括号）对齐，不需要额外的缩进
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# 增加注释，编辑器会提示语法高亮，有助于区分
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# 在续行中，增加额外的缩进级别
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

```



### 每行最大长度

每行最多不超过`120`个字符。每行代码最大长度限制的根本原因是过长的行会导致阅读障碍，使得缩进失效。

除了以下两种情况例外：
1. 导入模块语句
2. 注释中包含的URL

如果需要一个长的字符串，可以用括号实现隐形连接。

```python
x = ('This will build a very long long '
     'long long long long long long string')
```


### 操作符与操作数的位置

Python 没有三目操作符，对于二目操作符来说，操作符的摆放位置需要放在被操作数前面，如：


```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```


### 空行

* 模块中的一级函数和类定义之间，需要`空两行`。
* 类中函数定义之间，`空一行`。
* 可以在代码段中的`空一行`来区分不同业务逻辑块。
* 源文件末尾有且仅有`一行空行`。

```python

"""This is the example module.

This module does stuff.
"""


import os


def foo():
    pass


class MyClass():

    def __init__(self):
        pass

    def foo(self):
        pass


class AnotherClass(object):
    """Another class.

    This is some comments for another class
    """

    def __init__(self,
                 a,
                 b):
        if a > b:
            self._min = b
            self._max = a

        else:
            self._min = a
            self._max = b

        self._gap = self._max = self._min

    def foo(self):
        pass

```


### 源文件编码

源文件编码需统一使用utf8编码，以下内容需要增加到每一个python文件的头部。

```python
# -*- coding: utf-8 -*-
```

**避免不同操作系统对文件换行处理的方式不同，一律使用`LF`**


### 模块引用(import)

> 每个导入应该独占一行

***正确示范***

```python
import os
import sys
```
***错误示范***

```python
import os, sys
```

导入总应该放在文件顶部, 位于模块注释和文档字符串之后, 模块全局变量和常量之前. 导入应该按照从最通用到最不通用的顺序分组, 每个分组之间，需要空一行:

* 标准库导入
* 第三方库导入
* 本地导入

每种分组中, 应该根据每个模块的完整包路径按***字典序***排序, 并忽略大小写.

***正确示范***

```python
import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar
```

避免使用 `from <module> import *`，因为可能会造成命名空间的污染。


### 模块中的魔术变量(dunders)

对于两个`_` 开头和两个`_`结尾的变量，如 `__all__`, `__author`__, `__version__`等，应该放在模块文档之后，其他模块导入之前（`__future__` 除外）。Python 要求 `future` 导入必须出现在其他模块导入之前。

***正确示范***

```python
# -*- coding: utf-8 -*-
#
# Copyright @ 2020 Tencent.com
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```


## 注释
> 有效的注释有助于帮助开发者更快地理解代码，模块，函数，方法，以及行内注释的都有各自的风格。

所有`#`开头的注释，必须与所在的代码块同级，并置放在代码之上，且要求注释内容与`#`之间空一个空格。

需对外发布的public 模块，函数，类，方法等需要包含文档字符串。内部使用的方法，函数等，要求使用简单的注释描述功能。

### 文档字符串

文档字符串可以被pydoc 解析。第一行为文档名，空一行后，输入文档描述

```python
def foobar():
    """Return a foobang

    Optional plotz says to frobnicate the bizbaz first.
    """
```

[PEP 257](https://www.python.org/dev/peps/pep-0257/) 全面描述了文档字符串的风格。

### 块注释

对于复杂的操作，可以在代码之前写若干行注释，对简单的代码，可以放在行内，与代码离开至少2个空格。

```python
# this is a very complex operation, please
# read this carefully

if i & (i-1) == 0:
    # do my job ...

# 单行注释，为可读性，至少离开代码2个空格
x = x + 1                 # Compensate for border
```

### TODO, FIXME, NOTES

> 为临时代码使用TODO注释, 它是一种短期解决方案. 常见的IDE在提交代码时，会检查变更中包含了TODO并提醒开发者，防止提交是忘记还有未完成的代码.

TODO注释应该在所有开头处包含`TODO`字符串, 紧跟着是用括号括起来的你的名字, email地址或其它标识符. 然后是一个可选的冒号. 接着必须有一行注释, 解释要做什么. 主要目的是为了有一个统一的TODO格式, 这样添加注释的人就可以搜索到(并可以按需提供更多细节). 写了TODO注释并不保证写的人会亲自解决问题. 当你写了一个TODO, 请注上你的企业微信名。

```python
# TODO(zhangsan): Change this to use relations.
```

相同地，也可以留下`FIXME`, `NOTES` 注释。

```python
# FIXME(zhangsan): Please fix me here.

# NOTES(zhangsan): This is some notes.
```

### 函数，方法和类注释

一个函数或方法，如果可以直接被其他开发者使用，需要提供文档明确其含义，需要指出输入，输出，以及异常内容。
同样，函数方法以及类的注释，也会被pydoc解析。

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```


类应该在其定义下有一个用于描述该类的文档字符串. 如果类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```



## 字符串

> 即使参数都是字符串, 也要使用%操作符或者格式化方法格式化字符串. 不过也不能一概而论, 你需要在+和%之间权衡.

***正确示范***

```python
 x = '%s, %s!' % (imperative, expletive)
 x = '{}, {}!'.format(imperative, expletive)
 x = 'name: %s; score: %d' % (name, n)
 x = 'name: {}; score: {}'.format(name, n)
```

***错误示范***

```python
x = '%s%s' % (a, b)  # use + in this case
x = '{}{}'.format(a, b)  # use + in this case
x = imperative + ', ' + expletive + '!'
x = 'name: ' + name + '; score: ' + str(n)
```

避免在循环中用`+`和`+=`操作符来累加字符串. 由于字符串是不可变的, 这样做会创建不必要的临时对象, 并且导致二次方而不是线性的运行时间. 作为替代方案, 你可以将每个子串加入列表, 然后在循环结束后用 .join 连接列表. (也可以将每个子串写入一个 cStringIO.StringIO 缓存中.)

***正确示范***

```python
items = ['<table>']
for last_name, first_name in employee_list:
    items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
items.append('</table>')
employee_table = ''.join(items)
```

***错误示范***

```python
employee_table = '<table>'
for last_name, first_name in employee_list:
    employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
employee_table += '</table>'
```

在同一个文件中, 保持使用字符串引号的一致性. 使用单引号`'`或者双引号`"`引用字符串, 并在同一文件中一直沿用这种风格. 当字符串中包含单引号或者双引号时，为提高可读性，使用另外一种引号，代替转义字符。 

***正确示范***

```python
Python('Why are you hiding your eyes?')
Gollum("I'm scared of lint errors.")
Narrator('"Good!" thought a happy Python reviewer.')
```

***错误示范***

```python
Python("Why are you hiding your eyes?")
Gollum('The lint. It burns. It burns us.')
Gollum("Always the great lint. Watching. Watching.")
```

如果要引用的字符串为多行时，需要使用双引号引用字符串；`文档字符串（docstring）`必须使用三重双引号`"""`，避免在代码中使用三重引号`"""`，因为当使用三重引号时，缩进方式与其他部分不一致，容易引起误导。

***正确示范***

```python
print("This is much nicer.\n"
      "Do it this way.\n")
```

***错误示范***

```python
print("""This is pretty ugly.
Don't do this.
""")
```

检查前缀和后缀时，使用 `.startswith()` 和 `.endswith()` 代替字符串切片。

***正确示范***

```python
if foo.startswith('bar'):
```

***错误示范***

```python
if foo[:3] == 'bar':
```

## 文件和sockets

> 在文件和sockets结束时，显式的关闭它。

除文件外， sockets或其他类似文件的对象在没有必要的情况下打开，会有许多副作用，例如：

1. 它们可能会消耗有限的系统资源，如文件描述符。 如果这些资源在使用后没有及时归还系统，那么用于处理这些对象的代码会将资源消耗殆尽。
2. 持有文件将会阻止对于文件的其他诸如移动、删除之类的操作。
3. 仅仅是从逻辑上关闭文件和sockets，那么它们仍然可能会被其共享的程序在无意中进行读或者写操作。只有当它们真正被关闭后，对于它们尝试进行读或者写操作将会抛出异常, 并使得问题快速显现出来。

而且，幻想当文件对象析构时，文件和sockets会自动关闭，试图将文件对象的生命周期和文件的状态绑定在一起的想法, 都是不现实的。因为有如下原因：

1. 没有任何方法可以确保运行环境会真正的执行文件的析构. 不同的Python实现采用不同的内存管理技术, 比如延时垃圾处理机制. 延时垃圾处理机制可能会导致对象生命周期被任意无限制的延长.
2. 对于文件意外的引用,会导致对于文件的持有时间超出预期(比如对于异常的跟踪, 包含有全局变量等).

推荐使用 `with` 语句管理文件:

```python
with open("hello.txt") as hello_file:
    for line in hello_file:
        print(line)
```

对于不支持使用`with`语句的类似文件的对象,使用`contextlib.closing()`：

```python
import contextlib

with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
```

Legacy AppEngine 中Python 2.5的代码如使用`with`语句, 需要添加 "from __future__ import with_statement".


## 语句

> 通常每个语句应该独占一行

如果测试结果与测试语句在一行放得下，你也可以将它们放在同一行。如果是`if`语句, 只有在没有`else`时才能这样做。特别地，绝不要对 `try`/`except` 这样做，因为`try`和`except`不能放在同一行。


***正确示范***

```python
if foo: bar(foo)
```

***错误示范***

```  python
if foo: bar(foo)
else:   baz(foo)

try:               bar(foo)
except ValueError: baz(foo)

try:
  bar(foo)
except ValueError: baz(foo)
```

## 访问控制

> 在Python中，对于琐碎又不太重要的访问函数, 应该直接使用公有变量来取代它们，这样可以避免额外的函数调用开销。当添加更多功能时，也可以用属性(property)来保持语法的一致性。

如果访问复杂，或者变量的访问开销很显著，那么你应该使用像 `get_foo()` 和 `set_foo()` 这样的函数调用。如果之前的代码行为允许通过属性(property)访问，那么就不要将新的访问函数与属性绑定。 这样，任何试图通过老方法访问变量的代码就没法运行，使用者也就会意识到复杂性发生了变化。

## 命名
> module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.

应该避免的名称：

1. 单字符名称，除了计数器和迭代器。
2. 包/模块名中的连字符(-)
3. 双下划线开头并结尾的名称(Python保留，例如__init__)

命名约定

1. 所谓`内部(Internal)`表示仅模块内可用, 或者, 在类内是保护或私有的。
2. 用单下划线`(_)`开头表示模块变量或函数是protected的(使用from module import *时不会包含)。
3. 用双下划线`(__)`开头的实例变量或方法表示类内私有。
4. 将相关的类和顶级函数放在同一个模块里。不像Java，没必要限制一个类一个模块。
5. 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格)，但是模块名应该用小写加下划线的方式(如lower_with_under.py)。尽管已经有很多现存的模块使用类似于CapWords.py这样的命名，但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致，这会让人困扰。

Python之父Guido推荐的规范：

| Type       | Public               | Internal             |
| ---------- | -------------------- | -------------------- |
| Modules    | lower_with_under     | \_lower\_with\_under |
| Packages   | lower\_with\_under   |                      |
| Classes    | CapWords             | \_CapWords           |
| Exceptions | CapWords             |                      |
| Functions  | lower\_with\_under() | \_lower_with_under() |
| Global/Class Constants | CAPS\_WITH\_UNDER | \_CAPS\_WITH\_UNDER |
| Global/Class Variables | lower\_with\_under | \_lower\_with\_under |
| Instance Variables  | lower\_with\_under | \_lower\_with\_under (protected) or \_\_lower\_with_under (private) |
| Method Names | lower\_with\_under() | \_lower\_with_under() (protected) or \_\_lower_with_under() (private) |
| Function/Method Parameters  | lower\_with\_under |       |
| Local Variables | lower\_with\_under |                   |

## Main

> 即使是一个打算被用作脚本的文件, 也应该是可导入的. 并且简单的导入不应该导致这个脚本的主功能(main functionality)被执行, 这是一种副作用. 主功能应该放在一个main()函数中.

在Python中，pydoc以及单元测试要求模块必须是可导入的。你的代码应该在执行主程序前总是检查 `if __name__ == '__main__' `， 这样当模块被导入时主程序就不会被执行。

```python
def main():
      ...

if __name__ == '__main__':
    main()
```
所有的顶级代码在模块导入时都会被执行. 要小心不要去调用函数, 创建对象, 或者执行那些不应该在使用pydoc时执行的操作.

---------------------

## 其他建议

### 三目操作符

三元组判断，python 不支持三元操作符，但可使用如下方式，禁止使用复杂难懂的逻辑判断。

***正确示范***

```python
x = a if a >= b else b
```

***错误示范***

```python
x = a >= b and a or b
```

### None 条件的判断

为提升可读性，在判断条件中应使用 `is not`，而不使用 `not ... is`

***正确示范***

```python
if foo is not None:
```

***错误示范***

```python
if not foo is None:
```

### 使用 def 定义简短函数而不是使用 lambda

***正确示范***

```python
def f(x): return 2 * x
```
***错误示范***

```python
f = lambda x: 2 * x
```

使用def的方式有助于在trackbacks中打印有效的类型信息，是f类型而不是一个lambda类型的调用。


### 函数参数

函数参数中，不允许出现可变类型变量作为默认值。

***正确示范***

```python
def f(x=0, y=None, z=None):
    pass
```

***错误示范***

```python
def f(x=0, y=[], z={}):
    pass
```
错误

### 异常
- 异常类继承自 `Exception`，而不是 `BaseException`。
- 建议在代码中用异常替代函数的错误返回码。

***正确示范***

```python
def write_data():
    if check_file_exist():
        do_something()
    else:
        raise FileNotExist()
```

***错误示范***

```python
def write_data():
    if check_file_exist():
        do_something()
        return 0
    else:
        return FILE_NOT_EXIST
```

- 使用新版本抛出异常的方式，禁止使用废弃的方式

***正确示范***

```python
raise ValueError('message')
```

***错误示范***

```python
raise ValueError, 'message'
```


- 捕获异常时，需要指明具体异常，而不是捕获所有异常。除非已经在当前线程的最外层（记得还是要打印一条traceback）。

***正确示范***

```python
try:
    do_something()
except Exception as e:
    print(traceback.format_exc())
    do_handle_exception()
```

***错误示范***

```python
try:
    do_something()
except Exception:
    platform_specific_module = None
```


- 在 `except` 子句中重新抛出原有异常时，不能用 `raise e`，而是用 `raise`。

***正确示范***

```python
try:
    raise MyException()
except MyException as e:
    try_handle_exception()
    raise  # 可以保留原始的 traceback


try:
    raise MyException()
except MyException as e:
    raise AnotherException(str(e))  # 允许的，建议保留好之前的异常栈信息，用于定位问题
```

***错误示范***

```python
try:
    raise MyException()
except MyException as e:
    try_handle_exception()
    raise e  # 异常栈信息从这里开始，原始的raise异常栈信息消息
```

- 所有 `try`/`except` 子句的代码要尽可的少，以免屏蔽其他的错误

***正确示范***

```python
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```

***错误示范***

```python
try:
    # 范围太广
    return handle_value(collection[key])
except KeyError:
    # 会捕捉到 handle_value() 中的 KeyError
    return key_not_found(key)
```

### 返回值

- 函数或者方法在没有返回时要明确返回`None`。

***正确示范***

```python
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return Nonedef bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```

***错误示范***

```python
def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
```

### 条件表达式

- `if` 与 `else` 尽量一起出现，而不是全部都是`if`子句。
- 对于未知的条件分支或者不应该进入的分支，建议抛出异常，而不是返回一个值（比如说`None` 或`False`）

***正确示范***

```python
if condition:
    do_something()
else:
    # 增加说明注释
    pass


if condition:
    do_something()
# 这里增加注释说明为什么不用写else子句
# else:
#     pass


if condition:
    do_something()
else:
    do_else_something()
if another_condition:
    do_another_something()
else:
    raise MyException()  # 如果一定不会走到的条件，可以增加异常，防止将来未知的语句执行。
```

***错误示范***

```python
if condition:
    do_something()
if another_condition:  # 不能确定是否笔误为 elif ，还是开启全新一个if条件
    do_another_something()
else:
    do_else_something()
```



### 可以被忽略的变量

使用双下划线 `__` 来代表不需要的变量，单下划线 `_` 容易与 `gettext()` 函数的别名冲突。

***正确示范***

```python
path = '/tmp/python/foobar.txt'
dir_name, __ = os.path.split(path)
```



### True/False 布尔运算

- 不要用 `==` 与 `True`、 `False` 进行布尔运算
- 对序列（字符串、列表 、元组），空序列为 false 的情况

***正确示范***

```python
if greeting:
   pass

if not seq:
   pass

if seq:
   pass
```

***错误示范***

```python

if greeting == True
   pass

if greeting is True:  # Worse
   pass

if len(seq):
   pass

if not len(seq):
   pass
```
