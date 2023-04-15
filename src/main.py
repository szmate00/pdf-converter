import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from converter import convert_pdf_to_image
from threading import Thread


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Converter")
        self.master.geometry("300x300")
        self.file_path = None
        self.output_folder = None
        self.output_format = "png"
        self.progress_bar = None
        self.conversion_thread = None

        self.create_widgets()

    def create_widgets(self):
        # Create file selection button
        self.file_button = tk.Button(self.master, text="Select PDF file", command=self.select_file)
        self.file_button.pack(pady=10)

        # Create output format selection buttons
        self.format_label = tk.Label(self.master, text="Select output format:")
        self.format_label.pack(pady=5)

        self.png_button = tk.Radiobutton(self.master, text=".png", variable=self.output_format, value="png")
        self.png_button.pack()

        self.jpg_button = tk.Radiobutton(self.master, text=".jpg", variable=self.output_format, value="jpg")
        self.jpg_button.pack()

        # Create output folder selection button
        self.folder_button = tk.Button(self.master, text="Select output folder", command=self.select_folder)
        self.folder_button.pack(pady=10)

        # Create conversion button
        self.convert_button = tk.Button(self.master, text="Convert", command=self.start_conversion)
        self.convert_button.pack(pady=10)

        # Create progress bar
        self.progress_bar = tk.ttk.Progressbar(self.master, mode="determinate")
        self.progress_bar.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=(("PDF files", "*.pdf"),))

    def select_folder(self):
        self.output_folder = filedialog.askdirectory(title="Select output folder")

    def start_conversion(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a PDF file to convert.")
            return

        if not self.output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        self.conversion_thread = Thread(target=self.convert_pdf)
        self.conversion_thread.start()

    def convert_pdf(self):
        output_files = convert_pdf_to_image(self.file_path, output_format=self.output_format, output_folder=self.output_folder, progress_callback=self.update_progress)

        if not output_files:
            messagebox.showerror("Error", "Error converting PDF file.")
        else:
            if len(output_files) == 1:
                messagebox.showinfo("Success", "PDF file converted successfully.")
            else:
                messagebox.showinfo("Success", f"{len(output_files)} pages converted successfully.")

        self.master.destroy()

    def update_progress(self, progress):
        self.progress_bar["value"] = progress
        self.master.update()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()