import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import numpy as np
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
import os

from read_edf import read_edf_file
from predictions import pre_processing, predict_hfo, post_processing
from saving import save_bipolar_signal, save_markers

# Set BIPOLAR_DATA to True if your data is already in bipolar format
BIPOLAR_DATA = True

class InstructionApp:
        
    def __init__(self, root):
        self.root = root
        self.root.title("HFO detector")
        self.root.geometry("280x240")
        self.instruction_label = tk.Label(root, text="Please choose a .edf file", padx=10, pady=10)
        self.instruction_label.pack()
        self.choose_file_button = tk.Button(root, text="Choose File", command=self.choose_file, width=12)
        self.choose_file_button.pack(padx=10, pady=5)

        self.analyse_button = tk.Button(root, text="Analyse Signal", command=self.analyse_signal, state='disabled', width=12)
        self.analyse_button.pack(padx=10, pady=5)

        self.save_results_button = tk.Button(root, text="Save Results", command=self.save_results, state='disabled', width=12)
        self.save_results_button.pack(padx=10, pady=5)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = Progressbar(root, orient='horizontal', mode='determinate', variable=self.progress_var)
        self.progress_bar.pack(fill='x', padx=10, pady=5)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_all, width=12)
        self.clear_button.pack(padx=10, pady=5)

        self.signal = None
        self.channels = None
        self.sr = 0
        self.PREDr = None
        self.PREDfr = None
        self.markers = None
        
    def update_progress_bar(self, value):
        self.progress_var.set(value)
        self.progress_bar.update()  
    


    def choose_file(self):
        file_name = filedialog.askopenfilename(filetypes=[("European Data Format","*.edf"),("Matlab File","*.mat")])
        if file_name:
            self.instruction_label.config(text='Uploading signal...')
            bipolar_data, bipolar_channels, sr= read_edf_file(file_name, self.update_progress_bar, bipolar=BIPOLAR_DATA)
            self.signal=bipolar_data
            self.channels=bipolar_channels
            self.sr=sr
            self.update_progress_bar(100)
            self.instruction_label.config(text='Signal Uploaded. \n You can now analyse the signal')
            self.analyse_button.config(state='normal')

    def analyse_signal(self):
        if self.signal is not None:
            self.update_progress_bar(0)
            self.instruction_label.config(text='Pre-processing signal...')
            Xr, Xfr = pre_processing(self.signal, self.channels, self.sr, self.update_progress_bar)
            self.instruction_label.config(text='Pre-processing complete. \n Predicting HFOs...')
            self.update_progress_bar(0)
            self.PREDr, self.PREDfr = predict_hfo(Xr,Xfr, self.update_progress_bar)
            self.instruction_label.config(text='Predictions complete. \n Post-processing...')
            self.update_progress_bar(0)
            self.markers=post_processing(Xr, Xfr, self.PREDr, self.PREDfr, self.sr, self.update_progress_bar)
            self.instruction_label.config(text='Post-processing complete. \n You can now save the .mrk file')
            self.save_results_button.config(state='normal')


        else:
            self.instruction_label.config(text="Please choose a file first.")

    def save_results(self):
        if self.markers is not None:
            file_name = filedialog.asksaveasfilename(defaultextension='.mrk', filetypes=[("Marker","*.mrk"), ("All Files", "*.*")])
            if file_name:
                self.instruction_label.config(text="Saving results...")
                save_markers(file_name+'.mrk', self.markers, self.channels, self.update_progress_bar)
                self.instruction_label.config(text="Results saved!")
        else:
            self.instruction_label.config(text="Please analyze the signal first.")


    def clear_all(self):
        self.read_file=None
        self.signal = None
        self.channels = None
        self.sr = 0
        self.Xr = None
        self.Xfr = None
        self.PREDr = None
        self.PREDfr = None
        self.write_file=None

        self.instruction_label.config(text='Please choose a .edf file')
        self.analyse_button.config(state='disabled')
        self.save_results_button.config(state='disabled')
        self.update_progress_bar(0)

# Tkinter GUI setup
window = tk.Tk()
app = InstructionApp(window)
window.mainloop()
