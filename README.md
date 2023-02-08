# **ScheduleWorks**
A desktop application that can build a class schedule given time & day filters. 



# Requirements
### Manual Installations
-----
<a href="https://www.python.org/downloads/release/python-3100/" target="_blank">Python 3.10</a>

<a href="https://www.google.com/chrome/">Google Chrome</a>

<a href="https://www.oracle.com/java/technologies/downloads/">Java</a> (eventually)


### Command Prompt (Windows)
-----


Google Chrome
```Command Prompt
$Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "http://dl.google.com/chrome/install/375.126/chrome_installer.exe" -OutFile $Path\$Installer;
Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
```
<br />

Python


```Command Prompt
curl https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe -o python_install.exe;
%CD%\"python_install.exe;"
```
### *TO AVOID ISSUES ENSURE THAT YOU SELECT* "Add python.exe to PATH"



### Libraries
-----
The project is still in devolpment, to install the required tools to manually run, use below:
```bash
pip install -r requirements.txt
```
