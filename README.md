# wordScriber

__HTML local document editor__  
Linux version

This project demonstrates how to create apps that 
combine a python module (tkinter) and an HTML GUI 
in an offline desktop situation. In this case the 
focus is on using HTML to edit, create and format,
HTML documents. Here pywebview provides communication between
Python/tkinter and HTML/Javascript.

There are certain limitations depending on the web engine
and API employed. Web engines used outside of an Internet 
browser may be missing features found in the browser versions.
In this example pywebview (_WebKitGTK_) is used in a linux environment.

In the Linux case (WebKitGTK) spell checking is absent. 
In the Windows version of this project pywebview
uses _WebView2_ (part of Edge). In Windows testing
spell checking does work in a limited fashion. 

Also this Linux version has some extra code 
to force the tkinter dialogs to open on the correct screen
of a dual monitor setup. If you are using a single monitor, 
then remove the indicated code from wsr.py.

As you may have realized, I'm not using the webview module
to bring Internet pages into a desktop environment. This project
could be easily modified to do that, and there are easier ways.
The purpose of this project is to demonstrate how the pywebview module 
provides communication between Python/tkinter and HTML/Javascript.

![alttext](images/wsr_git.png "wordScriber")

