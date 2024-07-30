import tkinter as tk
from tkinter import ttk

def apply_styles(app):
    style = ttk.Style()
    
    # Configure style for buttons
    style.configure('TButton',
                    font=('Helvetica', 8),
                    padding=10,
                    background='darkblue',
                    foreground='blue')
    style.map('TButton',
              background=[('active', 'darkblue')],
              foreground=[('active', 'blue')])

    # Configure style for labels
    style.configure('TLabel',
                    font=('Helvetica', 14),
                    background='lightblue')
    
    # Ensure the frame expands and centers content
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    
    return style
