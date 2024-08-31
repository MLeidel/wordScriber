import webview
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import webbrowser
from spellchecker import SpellChecker

spell = SpellChecker()

current_file = ""  # tracks current file in use

# UNCOMMENT THIS FUNCTION TO WORK ON DUAL MONITORS (there is more)
def window_coord():
    px = window.x
    py = window.y
    geo = f"20x20+{px}+{py}"
    return geo

def on_closing():
    return True
    # Issues
    # IF USING SINGLE MONITOR SYSTEM delete 'return True' above and uncomment below
    # if messagebox.askokcancel("Save File?", "Really want to close this App?"):
    #     return True
    # else:
    #     return False

'''
API class to handle various functions
that typically could not be handled by a browser sponsored HTML GUI
because of restricted access to the user's system.
'''
class Api:

    def onClose(self):
        ''' immediate close no ask '''
        window.events.closing -= on_closing
        window.destroy()

    def getFileName(self):
        global current_file
        return current_file

    def open_file(self):
        ''' called from javascript '''
        root = tk.Tk()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.geometry(window_coord())  # COMMENT IF USING SINGLE MONITOR SYSTEM
        global current_file
        file_path = filedialog.askopenfilename(initialdir="./docs",
                                               title = "Open file",
                                               filetypes = (("HTML", "*.html"),
                                                            ("all files", "*.*")))
        root.destroy()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        if file_path:
            current_file = file_path
            with open(current_file, 'r') as file:
                return file.read()
        return ''

    def save_file(self, content):
        ''' called from javascript '''
        root = tk.Tk()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.geometry(window_coord())  # COMMENT IF USING SINGLE MONITOR SYSTEM
        global current_file
        file_path = filedialog.asksaveasfilename(initialdir="./docs",
                                                 defaultextension=".html",
                                                 initialfile="",
                                                 filetypes = (("HTML", "*.html"),
                                                            ("all files", "*.*")))
        root.destroy()  # remove if single monitor
        if file_path:
            current_file = file_path
            with open(file_path, 'w') as file:
                file.write(content)
            return current_file
        return ''

    def quick_save_file(self, content):
        global current_file
        file_path = current_file
        with open(file_path, 'w') as file:
            file.write(content)
        current_file = file_path
        return current_file

    def open_options(self):
        ''' called from javascript '''
        with open("options.dat", 'r') as file:
            lst = [line for line in file if not line.lstrip().startswith('=')]
            lst = [i.strip() for i in lst]  # strip end of lines
            return ','.join(lst)  # make a csv string
        return ''

    def open_editor(self):
        subprocess.Popen([tx, "./options.dat"])

    def open_filemgr(self):
        subprocess.Popen([fm, "./"])

    def open_browser(self):
        # launch current file in browser
        webbrowser.open(current_file)

    def open_spellcheck(self, content):
        # process sting of words and return results
        wlist = content.split()         # string to list
        words = spell.unknown(wlist)    # spell check the list
        strwords = "<br>"
        for word in words:              # concat spell output into one string
            strwords += word + "<br>"
            # Get the one `most likely` answer
            #   spell.correction(word)
            # Get a list of `likely` options
            strwords += str(spell.candidates(word))
            strwords += "<hr>"
        return strwords

# Create a webview window
if __name__ == '__main__':

    api = Api()

    opts = api.open_options().split(',')
    tx = opts[6]  # text editor
    fm = opts[7] # file manager

    window = webview.create_window('Word Scriber',
                     url='index.html',
                     width=650,
                     height=675,
                     js_api=api)

    window.events.closing += on_closing

    webview.start()
