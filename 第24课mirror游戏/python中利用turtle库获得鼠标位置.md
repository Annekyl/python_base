# python中利用turtle库获得鼠标位置

## 实时获取鼠标位置

`turtle` 库本身不提供直接的方法来实现这一功能。只可以使用 `turtle` 的画布 `canvas` 对象来访问更底层的 `TKinter` 方法，从而实现实时追踪鼠标位置的功能。

```python
import turtle

def motion(event):
    x, y = event.x, event.y
    print(f"鼠标位置：{x}, {y}")

screen = turtle.Screen()
canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)	# <Motion> 是 Tkinter 中用于表示鼠标移动的事件类型的标准字符串,将鼠标移动事件（<Motion>）与一个名为 motion 的函数绑定在一起

screen.mainloop()
```

介绍:`TKinter` 是 Python 的一个标准 GUI (图形用户界面) 库，用于创建桌面应用程序。它是一个轻量级的、简单易用的工具，适合快速开发桌面应用程序。`TKinter` 提供了各种控件（如按钮、标签、文本框等），以及用于组织这些控件的容器（如框架和窗口）。它支持事件驱动编程，这意味着您可以定义事件处理函数来响应用户操作（如点击按钮、键盘输入等）。而`turtle` 的绘图窗口实际上是在 `TKinter` 的基础上创建的。因此，可以利用 `TKinter` 的一些方法来扩展 `turtle` 的功能

## 点击获取鼠标位置

主要使用`onclick`和`onescreenclick`函数来获取点击时鼠标位置

## 1.`onescreenclick`

`onscreenclick`隶属于turtle模块。所以函数调用只能是`turtle.onscreenclick()`。

`onscreenclick`是一个监听器的角色，用来监听当鼠标在画布上按下事件，一旦事件发生，就会调用以函数参数形式传入的处理函数。

`onscreenclick`调用处理函数时，会给处理函数传入发生鼠标点击的坐标位置


```python
import turtle
def show(x,y):
    print(x,y)
 
wn = turtle.Screen()
wn.listen()
wn.onscreenclick(show)
turtle.done()
```

## 2.`onclick`

```python
import turtle

# screen object
wn = turtle.Screen()


# method to perform action


def fxn(x, y):
    turtle.goto(x, y)
    turtle.write(str(x) + "," + str(y))


# onclick action
wn.onclick(fxn)
turtle.done()

```

## 3.注意事项

​	在`csdn`上面查阅资料的时候,会有部分博客说这两个函数其实有一定的区别,但是经过我的研究我***暂时认为***这应该是某些博客的作者写错了导致的,我认为就是一模一样的,上面两个函数`wn.onclick(fxn)`处可以用`wn.onscreenclick(fun)`函数来平替,`wn.onscreenclick(show)`也可以用`wn.onclick(show)`来平替,是没什么区别的,

## 4.深入研究

接下来我再来深入研究一下这两个函数到底为什么我说他们没有区别

我们利用`pycharm`的查找功能可以在官方文档里面看见

![image-20231122222523927](https://raw.githubusercontent.com/nahida77/IMG/main/image-20231122222523927.png)

![image-20231122222507633](https://raw.githubusercontent.com/nahida77/IMG/main/image-20231122222507633.png)

![image-20231122222514007](https://raw.githubusercontent.com/nahida77/IMG/main/image-20231122222514007.png)

这个地方是`onclick()`函数在`turle.py`的官方文件中的原型,现提供翻译如下

```python
def onclick(self, fun, btn=1, add=None):
    """将 fun 绑定到画布的鼠标点击事件上。

    参数：
    - fun：带有两个参数的函数，表示画布上被点击点的坐标。
    - btn：鼠标按钮的编号，默认为 1。
    - add：字符串，表示事件绑定的附加选项，默认为 None。

    示例（对于命名为 screen 的 TurtleScreen 实例）：

    >>> screen.onclick(goto)
    >>> # 随后点击 TurtleScreen 将使乌龟移动到点击的点。
    >>> screen.onclick(None)
    """
    self._onscreenclick(fun, btn, add)

```

`onclick`函数的原型定义,他隶属于类`TurtleScreen`,在该类的结束声明了`onscreenclick`函数就等于`onclick`函数,这是我说这两个函数相等的第一个原因,我们再深入研究一下,发现`TurtleScreen`又是`TurtleScreenBase`的子类,我们转到`TurtleScreenBase`类中去,就会发现这样的两个内部函数(在python中,在函数名前打_这个下划线的函数的意思是内部函数,在类外部无法调用,子类可调用,相当于c++类中的protected,但这在自己开发的程序中并不会被视为与c++的protected部分一样的硬性保护区域)

#### `_onclick`函数



#### `_onscreenclick`函数



这两个内部函数我们阅读一下英文注释会发现其实是有区别的,第一个函数是在指定turtle上面点击才会生效触发fun函数,第二个内部函数在屏幕画布内点击任何一点都会触发fun函数,并且如果在`_``onscreenclick`调用的时候点击的是turtle,那么会先调用`_``onclick`事件,再调用_`onscreenclick`事件,那么由此来看这两个函数的内部函数还是有区别的,总结一下这两个内部函数的区别

### 两个函数的区别：



1. **绑定对象不同**：`_onclick` 用于绑定一个函数到特定 turtle 对象上的鼠标点击事件。而 `_onscreenclick` 用于绑定一个函数到整个画布（屏幕）上的鼠标点击事件。
2. **事件触发的顺序**：如果在一个 turtle 上进行了点击，会首先触发 `_onclick` 事件（如果这个 turtle 上绑定了事件的话），然后再触发 `_onscreenclick` 事件。这意味着 `_onclick` 更具体，用于单个 turtle 对象，而 `_onscreenclick` 更广泛，适用于整个画布。
3. **内部实现**：在 `_onclick` 中，事件绑定到一个特定的 `item`（即 turtle 对象），而在 `_onscreenclick` 中，事件直接绑定到画布（`self.cv`）。这体现了它们操作的对象级别上的不同。

但是我们在`onclick`函数中又会发现在最底下有这句话

![image-20231122222457887](https://raw.githubusercontent.com/nahida77/IMG/main/image-20231122222457887.png)

他在最底下又调用了_`onscreenclick`函数,又说明了说明 `onclick` 方法的设计目的是为了让用户能够方便地绑定函数到整个画布的点击事件，而不是仅限于特定的 turtle 对象。那么综上所述,`onclick`函数和`onscreenclick`函数其实是没有区别的