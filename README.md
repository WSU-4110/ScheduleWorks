# **ScheduleWorks**

<p align="center">
<img  src="https://github.com/WSU-4110/ScheduleWorks/blob/main/schedule-works-fe/src/main/resources/ScheduleWorksLogo.png" width=65% height=65%>
</p>


A desktop application that can build a class schedule using your WSU DegreeWorks account. 

# Installation
1. Download the repository into C:\Program Files\ using admin. (unzip if you need to)
2. Right click the ScheduleWorks folder and select properties.
3. Click on security.
4. Click Edit.
4. Enable Full Access for users and click apply.
5. Run ScheduleWorks.exe and enjoy!

# Contributors
1. Mazen Mirza
2. Aafnan Mahmood
3. Mizanul Haque
4. Faizan Bhatti
5. Christopher Forkin


# Requirements
Installation can be either through a terminal or by directly downloading the required software
### Direct Installations
-----
<a href="https://www.python.org/downloads/release/python-3100/" target="_blank">Python 3.10</a>

<a href="https://www.google.com/chrome/">Google Chrome</a>

<a href="https://www.oracle.com/java/technologies/downloads/">Java</a>

<a href="https://gluonhq.com/products/javafx/">JavaFX</a>



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
Install the required tools to manually run, use below:
```bash
pip install -r requirements.txt
```
