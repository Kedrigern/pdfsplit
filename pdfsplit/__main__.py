#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tkinter import *
from tkinter import filedialog, messagebox
from argparse import ArgumentParser
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

def new_name(filename, from_page, last_page):
    """
    If input is input.pdf, 5, 9
    returns input-5-9.pdf
    """
    return filename.rsplit(".pdf")[0] + "-" + str(from_page) + "-" + str(last_page) + ".pdf"

def pdf_split(filename, from_page, last_page):
    outfile = new_name(filename, from_page, last_page)
    x = PdfReader(filename)
    y = PdfWriter()

    if int(last_page) > len(x.pages):
        raise IndexError("Out of range")

    for i in range(int(from_page), int(last_page)):
        y.addpage(x.pages[i])

    # y.trailer.Info = IndirectPdfDict(
    #     Title='your title goes here',
    #     Author='your name goes here',
    #     Subject='what is it all about?',
    #     Creator='some script goes here',
    # )

    y.write(outfile)


class Gui(Frame):

    def __init__(self, parent, from_page=None, last_page=None, filename = ""):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI(from_page, last_page, filename)

    def initUI(self, from_page, last_page, filename = ""):
        self.parent.title("PDF split")
        self.pack(fill=BOTH, expand=1)
        self.from_page = StringVar(value=from_page)
        self.last_page = StringVar(value=last_page)
        self.filename = filename
        self.blabel = StringVar()
        if self.filename:
            self.blabel.set(self.filename)
        else:
            self.blabel.set("Vyberte soubor ve formátu PDF")

        self.b1 = Button(self, textvariable=self.blabel, command=self.askopenfile).pack()
        Label(self, text = "Od strany:").pack()
        self.e1 = Entry(self, textvariable=self.from_page).pack()
        Label(self, text = "Do strany:").pack()
        self.e2 = Entry(self, textvariable=self.last_page).pack()
        Button(self, text = "Vyřízni", command=self.cut).pack()

    def askopenfile(self):
        self.filename = filedialog.askopenfilename(
            title = "choose your file",
            initialdir = os.path.expanduser('~'),
            filetypes = [("pdf files", "*.pdf")]
        )
        self.blabel.set(self.filename)

    def cut(self):
        try:
            f = int(self.from_page.get())-1
            t = int(self.last_page.get())
            if f >= t:
                raise IndexError()
            if f < 0:
                raise IndexError()
            if not os.path.isfile(self.filename):
                raise FileNotFoundError()
            pdf_split(self.filename, f, t)
        except(ValueError):
            print("Non int value")
            messagebox.showerror("Non int value")
            return
        except(IndexError):
            print("Index out of range")
            messagebox.showerror("Index out of range")
            return
        except(FileNotFoundError):
            print("File not found error")
            messagebox.showerror("File not found error")
            return

        self.quit()

def main():
    parser = ArgumentParser(description=__doc__, epilog='Author: ' + __author__ + ', version: ' + __version__)
    parser.add_argument('-g', '--gui', action='store_true', help="Run GUI")
    parser.add_argument('-f', '--first', default="", help="From page")
    parser.add_argument('-l', '--last', default="", help="Last page")
    parser.add_argument('infile', nargs='?', help='Input files')
    args = parser.parse_args()

    if args.gui:
        root = Tk()
        root.geometry("250x150+300+300")
        app = Gui(root, args.first, args.last)
        root.mainloop()
    else:
        if not args.infile:
            parser.print_usage()
        pdf_split(args.infile, args.first, args.last)

if __name__ == '__main__':
    main()
