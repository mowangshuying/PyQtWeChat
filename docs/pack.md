## 如何打包

终端进入 env.

use python 3.9/3.8

打包的话，用 nuitka 更适合，对 PySide 支持更好。压缩后仅 15MB 左右。

pip install nuitka zstandard

- PyQt 26MB ==> 14.9MB
  > python -m nuitka --onefile --windows-disable-console --enable-plugin=pyqt6 App.py
- PySide 34MB ==> 16.8MB
  > python -m nuitka --onefile --windows-disable-console --enable-plugin=pyside6 --follow-import-to=need --output-dir=output App.py
