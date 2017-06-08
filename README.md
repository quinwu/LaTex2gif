# LaTex2gif
### 为什么会有这个项目

用Markdown + LaTex 写一些带有数学公式的文档的时候，会面临着Github or Gitlab无法渲染LaTex公式的问题，使得漂亮的LaTex公式不能显示在页面上。

当你使用Chrome浏览器的时候，可以选择[GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)插件来解决。

除此之外，还可以选择将LaTex公式转化给图片格式插入到Markdown文件中。通过使用如下的LaTex图片API来解决

```![](http://latex.codecogs.com/gif.latex? )
![](http://latex.codecogs.com/gif.latex? )
```

将编辑好LaTex公式的Markdown文件转化为上述图片格式的Markdown文件较为繁琐，因此写下这个Python脚本来完成转化的过程。

### 如何使用

- 将LaTex2gif.py与需要转化的*.md文件放在同一目录下，执行脚本即可。
- 执行命令 `python LaTex2gif.py`
- 当前目录下自动生成的README.md文件即为所生成的文件。

### BUG

如果您在使用的过程中发现了其他的Bug或者有其他更好的意见建议可以选择提交Issues 或者选择与我联系 [wukuan1995@gmail.com](mailto:wukuan1995@gmail.com)
