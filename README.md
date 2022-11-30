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
将 PDF 文件转化为可编辑的 Excel 表格。

## 截图展示
![demo](demo.png)

## 使用方法
### 配置
1. 首先需要注册华为云账户，开通[通用表格识别](https://console.huaweicloud.com/ocr/?region=cn-east-3#/ocr/overview)，点击开通服务即可。
   + 注意，这里可以选择「区域」，例如上述链接默认为 `cn-east-3`。
2. 获取访问密钥：「控制台」-> 鼠标悬停用户名，点击「我的凭证」->「控制台」->「访问密钥」->「新增访问密钥」，按提示完成操作，下载得到密钥文件，使用编辑器打开即可。
3. 将 Access Key ID，Secret Access Key 以及你选择的区域（例如 `cn-east-3`）填入应用的配置页面即可。

### 转换
1. 首先点击`选择文件`选择待处理的 PDF 文件。
2. 填写`起始页`和`结束页`，`结束页`填 `0` 表示处理后续所有页面。
3. 填写`选择角度`，PDF 文件中表格顺时针旋转多少度就这里就选择多少度。
4. 之后点击`开始转换`，生成好的文件将在软件根目录下，文件名由你选择的文件的文件名以及页面范围组成。

## 打包流程
```bash
pip install -r requirements.txt
pyuic5 -o ui.py main.ui
pyrcc5 -o resource_rc.py resource.qrc 
pyinstaller --noconsole -F ./main.py --icon icon.png -n pdf2excel.exe
```

## 其他
[PDF icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/pdf)
