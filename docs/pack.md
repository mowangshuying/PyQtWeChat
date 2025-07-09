## 如何打包
终端进入env.

use python 3.9/3.8

打包的话，用nuitka更适合，对PySide支持更好。压缩后仅15MB左右。

pip install nuitka zstandard
* PyQt 26MB ==> 14.9MB
>python -m nuitka --onefile --windows-disable-console --enable-plugin=pyqt6 App.py
* PySide 34MB ==> 16.8MB
>python -m nuitka --onefile --windows-disable-console --enable-plugin=pyside6 --follow-import-to=need --output-dir=output App.py