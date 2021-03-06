# GUI Automation
> Creators: Craig Sandlin, Mason Currie, Sean Summers, Anthony Connor

> Project Description: Automation tool designed to relieve the user from repetitive tasks. Works across all applications; from websites to spreadsheets, file explorer, and everything inbetween. A friendly excel UI allows those without programming knowledge to automate any task that includes clicking, typing, select all, backspace, enter, wait, and more! 

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
> The motivation: The mother of all invention- necessity. I, Craig Sandlin, was required to do electrical measurements on lighting fixtures to characterize the product before approbation listing with UL and/or Intertek. The sample size for this testing was sometimes upward of 70 discrete measurements. The changes that needed to be made to the software were repetitive and regular. If only I could program the inputs ahead of time! But alas, the software was propriatery and no API was available. It is tasks like these where this software really shines. With some upfront setup the entire process could be automated. Even allowing measurements to be taken over night which improved throughput!

## Screenshots
file:///.file/id=6571367.125785890
![Example screenshot](./img/screenshot.png)

## Technologies
* Python 3 - version 3.5
* Excel - version Latest

## Setup
Describe how to install / setup your local environement / add link to demo version.

deleteAllFiles will need the send2trash module installed - which can be installed with pip install Send2Trash

renamePython is setup to rename files with the naming format "x - x - #1.ext" 

need excel, pycharm for code editing./ local environment needs pyautogui and may need pip to install pyautogui on certain machines. demo version is accessible though the example.xlsm

## Code Examples
Show examples of usage:
`example of the interactivity with excel`
*Sub PythonMousePosition()

Dim objShell As Object
'''initialize the array as a string'''
Dim PythonExe, PythonScript, arg, formattedArg As String

Set objShell = VBA.CreateObject("Wscript.Shell")

PythonExe = """C:\Users\craig\AppData\Local\Programs\Python\Python38\python.exe"""

PythonScript = """C:\Users\craig\PycharmProjects\CS3398-Vulcans-S2020\MousePosition.py"""

objShell.Run PythonExe & PythonScript, 6


End Sub
'''initialize the funtion to allow interaction with excel as a gui'''
'''format to run explicitly thru the file paths on craig's laptop'''
Sub PythonGUIControl()

Dim objShell As Object
'''initialize this array as a string'''
Dim PythonExe, PythonScript, arg, formattedArg As String

Set objShell = VBA.CreateObject("Wscript.Shell")

PythonExe = """C:\Users\craig\AppData\Local\Programs\Python\Python38\python.exe"""

PythonScript = """C:\Users\craig\PycharmProjects\CS3398-Vulcans-S2020\ExcelUI.py"""

'arg = ThisWorkbook.Sheets("Sheet2").Range("A3").Value
'arg = "Hello World!"
'formattedArg = """" & """" & """" & arg & """" & """" & """"

'formattedArg = """C:\\Users\\CraigSandlin\\Documents\\CS3398-Vulcans-S2020\example.xlsm"""

objShell.Run PythonExe & PythonScript, 6


End Sub

Sub test()
MsgBox "Hello World"
*End Sub

## Features
List of features ready and TODOs for future development
* Interactivity through excel
* Mouse Pixel Position Display
* Clicking and Typing Automation
* Automated website login

To-do list:
* Wow improvement to be done 1
* Wow improvement to be done 2

## Status
Project is: In progress
*Update by Craig Sandlin: The second sprint has been completed. Thus far, we have completed the base functionality of the gui automation tool. My contribution is in ownership of the ProcedureLoad.py and ProcedureSave.py files. It's function is to load and save procedures related to the keyboard and mouse emulation feature.Next step will be to integrate the puzzle pieces from the team into one user interface and to look at refactoring the code.

*Update by Anthony Connor: The second sprint has been completed. Thus far, we completed more base functions of automation tool. My contribution is in the ownership of the wifi_login.py and config.py. Its function is to automate a login into a desired network using mouse/keyboard emulation along with locating images on the scrren.

*Update by Sean Summers: My contribution in the first sprint was introducing some feature ideas and then writing a script called rename.py which is in our master branch. The script allows the user to rename a large amount of files in order to sort them better. It will also later be used as a part of another feature to rename/parse them so duplicates can be deleted.

*Update by Mason Currie: My contribution in the second sprint was the automated website login feature. The feature prompts the user for a url link, and their login credentials. It then opens a chrome browser, navigates to link, and proceeds to "sign in" to the users account. My next step is to integrate this feature into our excel GUI, and fix any bugs that may occur.

## Inspiration
Add here credits. Project inspired by..., based on...

## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!
