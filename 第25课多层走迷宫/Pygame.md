# Pygame - Color 颜色对象

Pygame 中的 Color 类用于表示屏幕背景、文本、形状和所有其他 Pygame 对象的颜色。 它通过传递红色、绿色、蓝色的颜色值和可选的代表不透明值的 alpha 值来构建。 这些值中的每一个都在 0 到 255 之间。

```
color = pygame.Color(r, g, b, a=255)
```

alpha 的默认值为 255，表示完全不透明。 可以访问和设置各个属性。

| pygame.Color.r | 获取或设置Color的红色值。                  |
| -------------- | ------------------------------------------ |
| pygame.Color.b | 获取或设置 Color 的绿色值。                |
| pygame.Color.b | Gets or sets the blue value of the Color.  |
| pygame.Color.a | Gets or sets the alpha value of the Color. |

也可以使用其他颜色模型，如 CMY、HSVA、HSLA 和 i1i2i3。

| pygame.Color.cmy    | 获取或设置 Color 的 CMY 表示法。 Cyan, Magenta, Yellow     |
| ------------------- | ---------------------------------------------------------- |
| pygame.Color.hsva   | 获取或设置 Color 的 HSVA 表示法。 Hue, Saturation, Value   |
| pygame.Color.hsla   | 获取或设置 Color 的 HSLA 表示。 Hue, Saturation, Lightness |
| pygame.Color.i1i2i3 | 获取或设置 Color 的 I1I2I3 表示。                          |

我们可以使用预定义的字符串常量来表示 RGBA 颜色组合。 下面列出了一些预定义的颜色 −

- 'black': (0, 0, 0, 255)
- 'blue': (0, 0, 255, 255),
- 'cyan': (0, 255, 255, 255),
- 'gold': (255, 215, 0, 255),
- 'gray': (190, 190, 190, 255),
- 'green': (0, 255, 0, 255),
- 'orange': (255, 165, 0, 255),
- 'purple': (160, 32, 240, 255),
- 'red': (255, 0, 0, 255),
- 'violet': (238, 130, 238, 255)
- 'yellow': (255, 255, 0, 255),
- 'white': (255, 255, 255, 255)

要获取所有预定义的颜色，请运行以下 for 循环 −

```
for k, v in THECOLORS.items():
   THECOLORS[unicode_(k)] = v
```

# Pygame - Event 事件对象

所有事件都是 pygame.event.EventType 类的实例。Pygame 识别以下事件类型 −

| 事件类型        | 属性              |
| :-------------- | :---------------- |
| QUIT            | None              |
| ACTIVEEVENT     | gain, state       |
| KEYDOWN         | unicode, key, mod |
| KEYUP           | key, mod          |
| MOUSEMOTION     | pos, rel, buttons |
| MOUSEBUTTONUP   | pos, button       |
| MOUSEBUTTONDOWN | pos, button       |
| JOYAXISMOTION   | joy, axis, value  |
| JOYBALLMOTION   | joy, ball, rel    |
| JOYHATMOTION    | joy, hat, value   |
| JOYBUTTONUP     | joy, button       |
| JOYBUTTONDOWN   | joy, button       |
| VIDEORESIZE     | size, w, h        |
| VIDEOEXPOSE     | None              |
| USEREVENT       | Code              |

# Pygame - 键盘事件

| pygame.key.get_pressed      | 获取所有键盘按键的状态        |
| --------------------------- | ----------------------------- |
| pygame.key.get_mods         | 确定哪些修饰键被按住          |
| pygame.key.set_repeat       | 控制如何重复按住键            |
| pygame.key.get_repeat       | 获取重复按住的键              |
| pygame.key.name             | 获取一个key标识符的名称       |
| pygame.key.key_code         | 根据键名获取key标识符         |
| pygame.key.start_text_input | 开始处理Unicode文本输入事件   |
| pygame.key.stop_text_input  | 停止处理 Unicode 文本输入事件 |

# Pygame - 鼠标事件

| pygame.key.get_pressed         | 获取鼠标按钮的状态         |
| ------------------------------ | -------------------------- |
| pygame.mouse.get_pos           | 获取鼠标光标位置           |
| pygame.mouse.get_rel           | 获取鼠标移动量             |
| pygame.mouse.set_pos           | 设置鼠标光标位置           |
| pygame.mouse.set_visible       | 隐藏或显示鼠标光标         |
| pygame.mouse.get_visible       | 获取当前鼠标光标的可见状态 |
| pygame.mouse.get_focused       | 检查显示器是否接收鼠标输入 |
| pygame.mouse.set_cursor        | 设置鼠标光标的图像         |
| pygame.mouse.set_system_cursor | 将鼠标光标设置为系统变体   |

# Pygame - 绘制形状

| 绘制一个矩形   | rect(surface, color, rect)                         |
| -------------- | -------------------------------------------------- |
| 绘制一个多边形 | polygon(surface, color, points)                    |
| 绘制一个圆     | circle(surface, color, center, radius)             |
| 绘制一个椭圆   | ellipse(surface, color, rect)                      |
| 绘制一个椭圆弧 | arc(surface, color, rect, start_angle, stop_angle) |
| 绘制一条直线   | line(surface, color, start_pos, end_pos, width)    |
