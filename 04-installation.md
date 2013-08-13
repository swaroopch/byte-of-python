# Installation #

When we refer to "Python 3" in this book, we will be referring to any
version of Python equal to or greater than **3.3.2**.

## Installation on Windows ##

Visit <http://www.python.org/download/> and download the latest
version. The installation is just like any other Windows-based
software.

*Caution:* When you are given the option of unchecking any "optional"
 components, don't uncheck any.

### DOS Prompt ###

If you want to be able to use Python from the Windows command line
i.e. the DOS prompt, then you need to set the PATH variable
appropriately.

For Windows 2000, XP, 2003 , click on `Control Panel` --- `System` ---
`Advanced` --- `Environment Variables`. Click on the variable named
`PATH` in the 'System Variables' section, then select `Edit` and add
`;C:\Python33` (please verify that this folder exists, it will be
different for newer versions of Python) to the end of what is already
there. Of course, use the appropriate directory name.

For older versions of Windows, open the file `C:\AUTOEXEC.BAT` and add
the line '`PATH=%PATH%;C:\Python33`' (without the quotes) and restart
the system. For Windows NT, use the `AUTOEXEC.NT` file.

For Windows Vista:

1. Click Start and choose Control Panel
2. Click System, on the right you'll see "View basic information about
   your computer"
3. On the left is a list of tasks, the last of which is "Advanced
   system settings." Click that.
4. The Advanced tab of the System Properties dialog box is
   shown. Click the Environment Variables button on the bottom
   right.
5. In the lower box titled "System Variables" scroll down to Path and
   click the Edit button.
6. Change your path as need be.
7. Restart your system. Vista didn't pick up the system path
   environment variable change until I restarted.

For Windows 7:

1. Right click on Computer from your desktop and select properties or
   Click Start and choose Control Panel --- System and Security ---
   System. Click on Advanced system settings on the left and then
   click on the Advanced tab. At the bottom click on Environment
   Variables and under System variables, look for the PATH variable,
   select and then press Edit.
2. Go to the end of the line under Variable value and append
   `;C:\Python33`.
3. If the value was `%SystemRoot%\system32;` It will now become
   `%SystemRoot%\system32;C:\Python33`
4. Click OK and you are done. No restart is required.

### Running Python prompt on Windows ###

For Windows users, you can run the interpreter in the command line if
you have [set the `PATH` variable appropriately](#dos-prompt).

To open the terminal in Windows, click the start button and click
'Run'. In the dialog box, type `cmd` and press enter key.

Then, type `python` and ensure there are no errors.

## Installation on Mac OS X ##

For Mac OS X users, open the terminal by pressing `Command+Space` keys
(to open Spotlight search), type `Terminal` and press enter key.

Install [Homebrew](http://mxcl.github.com/homebrew/) by running:

~~~sh
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
~~~

Then install Python 3 using:

~~~sh
brew install python3
~~~

Now, run `python3` and ensure there are no errors.

## Installation on GNU/Linux ##

For GNU/Linux users, open the terminal by opening the `Terminal`
application or by pressing `Alt + F2` and entering `gnome-terminal`. If
that doesn't work, please refer the documentation or forums of your
particular GNU/Linux distribution.

Next, we have to install the `python3` package. For example, on Ubuntu,
you can use
[`sudo apt-get install python3`](http://packages.ubuntu.com/search?keywords=python3&searchon=names&suite=all&section=all).
Please check the documentation or forums of the GNU/Linux distribution
that you have installed for the correct package manager command to run.

Once you have finished the installation, run the `python3` and ensure
there are no errors.

You can see the version of Python on the screen by running:

~~~
$ python3 -V
Python 3.3.2
~~~

*Note:* `$` is the prompt of the shell. It will be different for you
depending on the settings of the operating system on your computer,
hence I will indicate the prompt by just the `$` symbol.

*Default in new versions of your distribution?:* Upcoming GNU/Linux
distributions such as
[Ubuntu 14.04 LTS are making Python 3 the default version](https://wiki.ubuntu.com/Python/3),
so check if it is already installed.

## Summary ##

From now on, we will assume that you have Python 3 installed on your
system.

Next, we will write our first Python 3 program.
