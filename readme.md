## 项目札记
1. `textwrap`模块对于格式化输出很有用，尤其是命令行程序。
2. Python通过使用try...except语句提供了一种非常优雅的方式来处理这种情况。这是基于请求原谅比允许更容易（Easier to Ask for Forgiveness thanPermission，EAFP）的原则。
3. 抽象基类最大的一个区别是不能被实例化，但这并不是唯一的区别。抽象基类强制要求派生类实现基类中定义的具体方法。这类似于在定义接口，不需要实例化，只需要一个契约，而且可以通过抽象方法精确控制哪些部分需要被重写。
4. `finally`语句通常被用来在离开函数之前做一些清理任务，一个使用示例就是用来关闭数据库或者文件的连接。为了在Python中实现这个目的，你也可以使用`with`声明。finally语句块是很强的，即使在`except`块中强制return，它还是会被执行。