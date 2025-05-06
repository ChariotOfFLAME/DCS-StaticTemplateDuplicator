import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# run ``python TemplateDuplicator.v6.py`` in the terminal to execute the script.

# This script is designed to duplicate and modify STM files for different theatres in DCS.
# It allows users to select multiple files, choose theatres, and save modified copies with the appropriate theatre name.

# This is for use with small, modular templates (see SAM sites, static aircraft displays, beach debris, etc.), rather than map-wide or theare-specific templates.
# To ensure proper visibilily of the templates, place the units in the template as close to a directly below the original Nuetral Bullseye as possible.
# This will ensure that the templates are visible in mission editor.

# After succesfully running the script, you can load the new template into a different theatre and use the multi-select tool to move the units to your desired location.

# ----- Constants -----
THEATRES = [
    "Afghanistan", "Caucasus", "Channel", "Falklands", "GermanyCW", "Iraq", 
    "Kola", "MarianaIslands", "Nevada", "Normandy", "PersianGulf", "Sinai", "Syria"
]

# ----- File and Content Handling -----
def load_files():
    """Prompt user to select one or more STM files, return paths and contents."""
    files = filedialog.askopenfilenames(title="Select .stm files", filetypes=[("STM files", "*.stm"), ("All files", "*.*")])
    if not files:
        messagebox.showerror("Error", "No files selected.")
        exit()

    content_map = {}
    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content_map[path] = f.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read:\n{path}\n\n{e}")
            exit()

    return content_map

def get_current_theatre(sample_content):
    """Extract the current theatre value from STM content."""
    match = re.search(r'\["theatre"\] = \"(.*?)\"', sample_content)
    if not match:
        messagebox.showerror("Error", "No theatre value found in file(s).")
        exit()
    return match.group(1)

def save_modified_files(content_map, selected_theatres, current_theatre):
    """Prompt user for output directory and save modified files for each selected theatre."""
    save_dir = filedialog.askdirectory(
        title="Select save directory",
        initialdir=os.path.dirname(next(iter(content_map)))
    )
    if not save_dir:
        messagebox.showinfo("Info", "No directory selected.")
        return

    created = []
    for path, content in content_map.items():
        base = os.path.basename(path)
        for theatre in selected_theatres:
            new_content = content.replace(f'["theatre"] = "{current_theatre}"', f'["theatre"] = "{theatre}"')
            new_path = os.path.join(save_dir, f"{theatre}-{base}")
            with open(new_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            created.append(os.path.basename(new_path))

    messagebox.showinfo("Success", "Files created:\n\n" + "\n".join(created))

# ----- GUI Components -----
def build_gui(content_map, current_theatre):
    """Create the main theatre selection window and handle file generation."""

    def on_create():
        selected = [t for t, v in zip(THEATRES, var_list) if v.get()]
        if not selected:
            messagebox.showwarning("Warning", "No theatres selected.")
            return
        save_modified_files(content_map, selected, current_theatre)
        root.destroy()

    def on_close():
        messagebox.showinfo("Info", "No theatres selected. Exiting.")
        root.destroy()
        exit()

    # Setup window
    root = tk.Tk()
    root.title("Select Theatres to Generate")
    root.geometry("400x500")
    root.resizable(True, True)
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Scrollable list of checkboxes
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame)
    scroll = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable = tk.Frame(canvas)

    canvas.create_window((0, 0), window=scrollable, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)
    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    var_list = []
    for theatre in THEATRES:
        var = tk.BooleanVar()
        tk.Checkbutton(scrollable, text=theatre, variable=var).pack(anchor='w')
        var_list.append(var)

    # Layout
    frame.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Select All", command=lambda: [v.set(True) for v in var_list]).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Select None", command=lambda: [v.set(False) for v in var_list]).pack(side="left", padx=5)
    tk.Button(root, text="Create Files", command=on_create).pack(pady=(0, 10))

    root.mainloop()

# ----- Main Execution -----
def main():
    content_map = load_files()
    current_theatre = get_current_theatre(next(iter(content_map.values())))
    build_gui(content_map, current_theatre)

if __name__ == "__main__":
    main()

# to complile to .exe, use pyinstaller with the command:
# pyinstaller --onefile --noconsole TemplateDuplicator.v6.py
# from a terminal in the same directory as the script.