import tkinter as tk
from tkinter import ttk

def apply_styles(app):
    style = ttk.Style()
    
    style.configure('TButton',
                    font=('Helvetica', 8),
                    padding=10,
                    background='darkblue',
                    foreground='blue')
    style.map('TButton',
              background=[('active', 'darkblue')],
              foreground=[('active', 'blue')])

    style.configure('TLabel',
                    font=('Helvetica', 14),
                    background='lightblue')
    
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    
    return style
