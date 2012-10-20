# Installation

## For Linux and BSD users

If you are using a distribution of Linux such as Ubuntu, Fedora, OpenSUSE, Debian, CentOS or {put your choice here}, or a BSD system such as FreeBSD, then it is most likely you already have Python installed on your system.

To test if you have Python already installed on your BSD or Linux box, open a shell program (like `gnome-terminal`) and enter the command `python -V` as shown below.

~~~
$ python -V
Python 2.7.2
~~~

*Note:* `$` is the prompt of the shell. It will be different for you depending on the settings of the operating system on your computer, hence I will indicate the prompt by just the `$` symbol.

If you see some version information like the one shown above, then you have Python installed already.

However, if you get a message like this one:

~~~
$ python -V
bash: python: command not found
~~~

Then you don't have Python installed. This is highly unlikely but possible.

In this case, you have two ways of installing Python on your system.

- Install the binary packages using the package management software that comes with your OS, such as `apt-get` in Ubuntu/Debian and other Debian-based distros, `yum` in Fedora, `pkg_add` in FreeBSD, etc. Note that you will need an internet connection to use this method. Alternatively, you can download the binaries from somewhere else and then copy to your computer and install it.
- You can compile Python from the [source code](http://www.python.org/download/) and install it. The compilation instructions are provided at the website.

## For Windows Users

Visit <http://www.python.org/download/> and download the latest version. The installation is just like any other Windows-based software.

*Caution:* When you are given the option of unchecking any "optional" components, don't uncheck any! Some of these components can be useful for you, especially IDLE.

An interesting fact is that majority of Python downloads are by Windows users. Of course, this doesn't give the complete picture since almost all Linux users will have Python installed already on their systems by default.

### DOS Prompt

If you want to be able to use Python from the Windows command line i.e. the DOS prompt, then you need to set the PATH variable appropriately.

For Windows 2000, XP, 2003 , click on `Control Panel` --- `System` --- `Advanced` --- `Environment Variables`. Click on the variable named `PATH` in the 'System Variables' section, then select `Edit` and add `;C:\Python27` to the end of what is already there. Of course, use the appropriate directory name.

For older versions of Windows, open the file `C:\AUTOEXEC.BAT` and add the line '`PATH=%PATH%;C:\Python27`' (without the quotes) and restart the system. For Windows NT, use the `AUTOEXEC.NT` file.

For Windows Vista:

#. Click Start and choose Control Panel
#. Click System, on the right you’ll see “View basic information about your computer”
#. On the left is a list of tasks, the last of which is “Advanced system settings.” Click that.
#. The Advanced tab of the System Properties dialog box is shown. Click the Environment Variables button on the bottom right.
#. In the lower box titled “System Variables” scroll down to Path and click the Edit button.
#. Change your path as need be.
#. Restart your system. Vista didn’t pick up the system path environment variable change until I restarted.

For Windows 7:

#. Right click on Computer from your desktop and select properties or Click Start and choose Control Panel --- System and Security --- System. Click on Advanced system settings on the left and then click on the Advanced tab. At the bottom click on Environment Variables and under System variables, look for the PATH variable, select and then press Edit. 
#. Go to the end of the line under Variable value and append `;C:\Python27`.
#. If the value was `%SystemRoot%\system32;` It will now become `%SystemRoot%\system32;C:\Python27`
#. Click ok and you are done. No restart is required.

## For Mac OS X Users

Mac OS X Users will find Python already installed on their system. Open the `Terminal.app` and run `python -V` and follow the advice in the above Linux and BSD section.

## Summary

For Linux and BSD systems, you probably already have Python installed on your system.  Otherwise, you can install it using the package management software that comes with your distribution. For a Windows system, installing Python is as easy as downloading the installer and double-clicking on it. From now on, we will assume that you have Python installed on your system.

Next, we will write our first Python program.
