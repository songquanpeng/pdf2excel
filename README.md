# PDF 转 Excel
> 将 PDF 文件转化为 Excel 表格

<p>
  <a href="https://raw.githubusercontent.com/songquanpeng/pdf2excel/main/LICENSE">
    <img src="https://img.shields.io/github/license/songquanpeng/pdf2excel?color=brightgreen" alt="license">
  </a>
  <a href="https://github.com/songquanpeng/pdf2excel/releases/latest">
    <img src="https://img.shields.io/github/v/release/songquanpeng/pdf2excel?color=brightgreen&include_prereleases" alt="release">
  </a>
  <a href="https://github.com/songquanpeng/pdf2excel/releases/latest">
    <img src="https://img.shields.io/github/downloads/songquanpeng/pdf2excel/total?color=brightgreen&include_prereleases" alt="release">
  </a>
</p>

可在 [Release 页面](https://github.com/songquanpeng/pdf2excel/releases)下载最新版本（Windows，macOS，Linux）。

## 功能
TODO

## 截图展示
![demo](demo.png)

## 使用方法
### Windows 用户  
直接双击 pdf2excel.exe 运行。

### macOS 用户
1. 给执行权限：`chmod u+x pdf2excel-macos`；
2. 之后直接双击运行 pdf2excel-macos 或在终端中运行都可。

### Linux 用户
同上，区别在于文件名换成 `pdf2excel`。

## 打包流程
```bash
pip install -r requirements.txt
pyuic5 -o ui.py main.ui
pyrcc5 -o resource_rc.py resource.qrc 
pyinstaller --noconsole -F ./main.py --icon icon.png -n pdf2excel.exe
```

## 其他
[PDF icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/pdf)
