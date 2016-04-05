# Installation {#installation}

When we refer to "Python 3" in this book, we will be referring to any version of Python equal to or greater than version [Python {{ book.pythonVersion }}](https://www.python.org/downloads/).

## Installation on Windows

Visit https://www.python.org/downloads/ and download the latest version. At the time of this writing, it was Python 3.5.1 
The installation is just like any other Windows-based software.

CAUTION: Make sure you check option `Add Python 3.5 to PATH`.

To change install location, click on `Customize installation`, then `Next` and enter `C:\python35` as install location.

If not checked, check `Add Python to environment variables`. This does the same thing as `Add Python 3.5 to PATH` on the first install screen.

You can choose to install Launcher for all users or not, it does not matter much. Launcher is used to switch between different versions of Python installed.

If your path was not set correctly, then follow these steps to fix it. Otherwise, go to `Running Python prompt on Windows`.

NOTE: For people who already know programming, if you are familiar with Docker, check out [Python in Docker](https://hub.docker.com/_/python/) and [Docker on Windows](https://docs.docker.com/windows/).

### DOS Prompt {#dos-prompt}

If you want to be able to use Python from the Windows command line i.e. the DOS prompt, then you need to set the PATH variable appropriately.

For Windows 2000, XP, 2003 , click on `Control Panel` -> `System` -> `Advanced` -> `Environment Variables`. Click on the variable named `PATH` in the _System Variables_ section, then select `Edit` and add `;C:\Python35` (please verify that this folder exists, it will be different for newer versions of Python) to the end of what is already there. Of course, use the appropriate directory name.

<!-- The directory should match pythonVersion variable in book.json -->
For older versions of Windows, open the file `C:\AUTOEXEC.BAT` and add the line `PATH=%PATH%;C:\Python35` and restart the system. For Windows NT, use the `AUTOEXEC.NT` file.

For Windows Vista:

- Click Start and choose `Control Panel`
- Click System, on the right you'll see "View basic information about your computer"
- On the left is a list of tasks, the last of which is `Advanced system settings`. Click that.
- The `Advanced` tab of the `System Properties` dialog box is shown. Click the `Environment Variables` button on the bottom right.
- In the lower box titled `System Variables` scroll down to Path and click the `Edit` button.
- Change your path as need be.
- Restart your system. Vista didn't pick up the system path environment variable change until I restarted.

For Windows 7 and 8:

- Right click on Computer from your desktop and select `Properties` or click `Start` and choose `Control Panel` -> `System and Security` -> `System`. Click on `Advanced system settings` on the left and then click on the `Advanced` tab. At the bottom click on `Environment Variables` and under `System variables`, look for the `PATH` variable, select and then press `Edit`.
- Go to the end of the line under Variable value and append `;C:\Python35` (please verify that this folder exists, it will be different for newer versions of Python) to the end of what is already there. Of course, use the appropriate folder name.
- If the value was `%SystemRoot%\system32;` It will now become `%SystemRoot%\system32;C:\Python35` <!-- The directory should match pythonVersion variable in book.json -->
- Click `OK` and you are done. No restart is required, however you may have to close and reopen the command line.

### Running Python prompt on Windows

For Windows users, you can run the interpreter in the command line if you have [set the `PATH` variable appropriately](#dos-prompt).

To open the terminal in Windows, click the start button and click `Run`. In the dialog box, type `cmd` and press `[enter]` key.

Then, type `python` and ensure there are no errors.

## Installation on Mac OS X

For Mac OS X users, use [Homebrew](http://brew.sh): `brew install python3`.

To verify, open the terminal by pressing `[Command + Space]` keys (to open Spotlight search), type `Terminal` and press `[enter]` key. Now, run `python3` and ensure there are no errors.

## Installation on GNU/Linux

For GNU/Linux users, use your distribution's package manager to install Python 3, e.g. on Debian & Ubuntu: `sudo apt-get update && sudo apt-get install python3`.

To verify, open the terminal by opening the +Terminal+ application or by pressing `[Alt + F2]` and entering +gnome-terminal+. If that doesn't work, please refer the documentation of your particular GNU/Linux distribution. Now, run `python3` and ensure there are no errors.

You can see the version of Python on the screen by running:

<!-- The output should match pythonVersion variable in book.json -->
```
$ python3 -V
Python 3.5.1
```

NOTE: `$` is the prompt of the shell. It will be different for you depending on the settings of the operating system on your computer, hence I will indicate the prompt by just the `$` symbol.

CAUTION: Output may be different on your computer, depending on the version of Python software installed on your computer.

## Summary

From now on, we will assume that you have Python installed on your system.

Next, we will write our first Python program.
