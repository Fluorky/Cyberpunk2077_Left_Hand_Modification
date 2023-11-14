import tkinter as tk
import os


absolute_path = os.path.dirname(__file__)
appdata_path = os.getenv('LOCALAPPDATA')

destination_file1 = "D:\\CYBERPUNK2077\\r6\\config\\inputUserMappings.xml"

relative_path_destination_file2 = "CD Projekt Red\\Cyberpunk 2077\\UserSettings.json"
destination_file2 = os.path.join(appdata_path, relative_path_destination_file2)


relative_path_left_file1 = "LiftLeft\\inputUserMappings.xml"
relative_path_left_file2 = "LiftLeft\\UserSettings.json"

relative_path_default_file1 = "Default\\inputUserMappings.xml"
relative_path_default_file2 = "Default\\UserSettings.json"

source_left_file1  = os.path.join(absolute_path, relative_path_left_file1)
source_left_file2  = os.path.join(absolute_path, relative_path_left_file2)

source_default_file1  = os.path.join(absolute_path, relative_path_default_file1)
source_default_file2  = os.path.join(absolute_path, relative_path_default_file2)


def submit():
    selected_mode = var.get()
    if selected_mode == 1:
        result_label.config(text="Mouse mode selected: Left\n")
        os.system("copy \"" + source_left_file1 + "\" \"" + destination_file1 + "\"")
        os.system("copy \"" + source_left_file2 + "\" \"" + destination_file2 + "\"")
        result_label.config(text="Files successfully copied\n")
        result_label.config(text="Now you are using Cyberpunk 2077 left mode\n")
    elif selected_mode == 2:
        result_label.config(text="Mouse mode selected: Default\n")
        os.system("copy \"" + source_default_file1 + "\" \"" + destination_file1 + "\"")
        os.system("copy \"" + source_default_file2 + "\" \"" + destination_file2 + "\"")
        result_label.config(text="Files successfully copied\n")
        result_label.config(text="Now you are using Cyberpunk 2077 in default mode\n")
    window.after(5000, window.destroy)  # Auto close after 5 seconds


# Create main window
window = tk.Tk()
window.title("Mouse Mode Selector")
window.geometry("480x360")  # Set minimal GUI size

# Create a variable to store the selected mode
var = tk.IntVar()

# Create label for instruction
instruction_label = tk.Label(window, text="Please select the mode of the mouse in Cyberpunk 2077", font=("Helvetica", 12))
instruction_label.pack(pady=10)

# Create radio buttons
left_radio = tk.Radiobutton(window, text="Left", variable=var, value=1, font=("Helvetica", 12))
default_radio = tk.Radiobutton(window, text="Default", variable=var, value=2, font=("Helvetica", 12))

# Create submit button
submit_button = tk.Button(window, text="Submit", command=submit, font=("Helvetica", 12))

# Create a label for displaying results
result_label = tk.Label(window, text="", wraplength=300, font=("Helvetica", 12), justify="center")

# Place widgets in the window with the pack manager
left_radio.pack(pady=10)
default_radio.pack(pady=10)
submit_button.pack(pady=10)
result_label.pack(pady=20)

# Configure pack to center vertically
window.update_idletasks()
height = (window.winfo_screenheight() - window.winfo_reqheight()) // 2
window.geometry('+{}+{}'.format(window.winfo_x(), height))

# Start the main event loop
window.mainloop()
