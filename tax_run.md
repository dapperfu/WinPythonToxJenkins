Sample tox run output:

```
C:\WinPythonToxJenkins>tox
GLOB sdist-make: C:\WinPythonToxJenkins\setup.py
py27 inst-nodeps: C:\WinPythonToxJenkins\.tox\dist\ping-0.1.zip
py27 installed: colorama==0.3.7,ping==0.1,py==1.4.32,pytest==3.0.5
py27 runtests: PYTHONHASHSEED='678'
py27 runtests: commands[0] | py.test
============================= test session starts =============================
platform win32 -- Python 2.7.12, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: C:\WinPythonToxJenkins, inifile:
collected 2 items

tests\test_01.py ..

========================== 2 passed in 0.04 seconds ===========================
py34 inst-nodeps: C:\WinPythonToxJenkins\.tox\dist\ping-0.1.zip
py34 installed: colorama==0.3.7,ping==0.1,py==1.4.32,pytest==3.0.5
py34 runtests: PYTHONHASHSEED='678'
py34 runtests: commands[0] | py.test
============================= test session starts =============================
platform win32 -- Python 3.4.4, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: C:\WinPythonToxJenkins, inifile:
collected 2 items

tests\test_01.py ..

========================== 2 passed in 0.08 seconds ===========================
py35 inst-nodeps: C:\WinPythonToxJenkins\.tox\dist\ping-0.1.zip
py35 installed: colorama==0.3.7,ping==0.1,py==1.4.32,pytest==3.0.5
py35 runtests: PYTHONHASHSEED='678'
py35 runtests: commands[0] | py.test
============================= test session starts =============================
platform win32 -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: C:\WinPythonToxJenkins, inifile:
collected 2 items

tests\test_01.py ..

========================== 2 passed in 0.06 seconds ===========================
py36 create: C:\WinPythonToxJenkins\.tox\py36
py36 installdeps: pytest
py36 inst: C:\WinPythonToxJenkins\.tox\dist\ping-0.1.zip
py36 installed: colorama==0.3.7,ping==0.1,py==1.4.32,pytest==3.0.5
py36 runtests: PYTHONHASHSEED='678'
py36 runtests: commands[0] | py.test
============================= test session starts =============================
platform win32 -- Python 3.6.0b3, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: C:\WinPythonToxJenkins, inifile:
collected 2 items

tests\test_01.py ..

========================== 2 passed in 0.05 seconds ===========================
___________________________________ summary ___________________________________
  py27: commands succeeded
  py34: commands succeeded
  py35: commands succeeded
  py36: commands succeeded
  congratulations :)

C:\WinPythonToxJenkins>
```