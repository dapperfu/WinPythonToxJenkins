# WinPython & Tox

These instructions will show you how to use [``tox``](https://tox.readthedocs.io/en/latest/) on Windows to test against multiple versions of Python. Set up correctly you will be able to test against Python versions 2.7, 3.4, 3.5 & 3.6 on Windows.

## Setup

### Python

### WinPython.

While I personally prefer to develop on \*NIX systems, in my corporate engineering day job Windows was a necessity. Most of the Python I wrote was targeting use on Windows 7 and 10.

There are multiple ways to [install multiple versions of Python](http://lmgtfy.com/?q=how+to+install+multiple+versions+of+python+on+windows) on Windows. I've tested some of them and prefer to use [WinPython](https://winpython.github.io/).

- No admin privledges required. In a corporate environment with locked down permissions this makes deployment and upgrading much easier.
- It's Portable. You can move the install folders around without breaking the individual Python 'installs'.

#### Getting WinPython

For these instructions I will use Zero versions because they are small in size and tox will handle installing packages in the respective virtual environments.

The latest WinPython releases can be found on their releases page:

**https://github.com/winpython/winpython/releases/**

1. Download the versions of Python you wish to test against. Most Windows 7 machines will be 64-bit. ([Here is how to check if you are unsure](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq))

   ![](images/ZeroDownload.png)

2. When all desired versions are downloaded, install them into the same folder. For my example I will use ```C:\WinPython\```.

   When you are done you should have a folder that looks like this with all of the different versions of WinPython inside of it.

   ![](images/2017-01-14 22_20-000024.png)
	
3. Pick one version of WinPython to be main version of Python. This will be the 'driving' version of Python which will have [``tox``](https://tox.readthedocs.io/en/latest/) installed.

   In this example I am using WinPython version 3.5.*
   
   Open the ``WinPython Command Prompt`` and run ``pip install tox``.

   ![](images/2017-01-16 15_08-000031.png)
   
4. For all versions of Python you will need to rename the ``python.exe`` to a version specific name so that ``tox`` can differentiate between them. The ``python.exe`` is found inside of the ``python-#.#.#`` folder inside of the WinPython

   For example with WinPython 2.7:

   **Before**:
   
   ![](2017-01-16 20_15-000036.png) 
   
   **After**:
   
   ![](images/2017-01-16 20_15-000037.png)
   
   Repeat this for all of the other versions of WinPython you have installed. For the main version of Python, copy and paste the executables and rename the copies. (So that both a ``python.exe`` and ``python#.#.exe`` exist in the same folder.)
   
   At the end you should end up with a folder structure that looks like this:
      
   ![](images/2017-01-16 21_30-000038.png)


## ``tox``

Minimal version of ``tox.ini`` for your project. This example uses [```pytest```](http://doc.pytest.org/en/latest/) to run the tests.

    # content of: tox.ini , put in same dir as setup.py
    [tox]
    envlist = py27,py34,py35,py36
    
    [testenv]
    deps=pytest
    commands=py.test


## Execution

1. Open the ``WinPython Command Prompt`` for your main version of Python.
 
2. Navigate to your project root.

3. Run ``tox``. ```tox``` will create a virtual environment for each version of Python and run the tests in each of them. For this project the results should look similar to this:

   ![](images/2017-01-16 22_02-000039.png)
