# wordScriber

__HTML local document editor__  
Linux version

This project demonstrates how to create apps that 
combine a python module (tkinter) and an HTML GUI 
in an offline desktop situation. In this case the 
focus is on using HTML to edit, create, and format
HTML documents. Here pywebview provides communication between
Python/tkinter and HTML/Javascript.

There are certain limitations depending on the web engine
and API employed. Web engines used outside of an Internet 
browser may be missing features found in the browser versions.
For Linux pywebview uses _WebKitGTK_ to render HTML in a
an HTML _contentEditable_ block.

In the Linux case (_WebKitGTK_) spell checking is absent. 
In the Windows version of wordScriber pywebview
uses _WebView2_ (part of Edge) which does provide
spell checking in a limited way. 

[If you're using dual monitors there is code
in __wsr.py__ that can be un-commented to fix the problem
of dialogs opening on the second monitor (tkinter problem.)]

The purpose of this project is to demonstrate how the pywebview module 
provides communication between Python/tkinter and HTML/Javascript.

![alttext](images/wsr_git.png "wordScriber")

