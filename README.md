# DCS Static Template Duplicator

A Python-based utility for duplicating and modifying `.stm` static template files for use across multiple theatres in *DCS: World*.

Created by [ChariotOfFLAME](https://github.com/ChariotOfFLAME)

---

## 🛠️ What It Does

This tool helps DCS mission editors quickly duplicate static templates for different maps (theatres) supported in the simulator. It is ideal for small, modular templates like:

- SAM site clusters  
- Static aircraft displays  
- Beach or airfield clutter  
- Modular mission support elements  

Templates are modified by replacing the `["theatre"]` tag in the `.stm` file and saving new versions with the correct map identifier.

---

## 🚀 Features

- ✅ Batch processing of multiple `.stm` files  
- ✅ Easy GUI-based theatre selection  
- ✅ Automatically updates `"theatre"` values and saves modified copies  
- ✅ Select/Deselect All buttons for quick operations  
- ✅ Informative error handling and success dialogs  

---

## 📂 Usage Instructions

### 1. Run the Script

Make sure you have Python 3 installed. Then run the script:

```bash
python TemplateDuplicator.v6.py
```

### 2. Select Files

Use the file dialog to select one or more `.stm` files to duplicate.

### 3. Choose Theatres

Use the GUI to check off which maps you want copies for. You can "Select All" or "Select None" with one click.

### 4. Output

You’ll be prompted to choose a folder to save the modified files. Each duplicated file will be renamed with the theatre prefix, e.g.:

```
Syria-myTemplate.stm
Nevada-myTemplate.stm
```

### 5. Load in DCS

Load the new `.stm` template in the desired map. Use the mission editor's multiselect tool to move units as needed.

> **📝 Placement Tip:**  
> To maximize template visibility across maps, place units close to directly beneath the original Neutral Bullseye in your source template.

---

## 🗺 Supported Theatres

The following DCS theatres are included by default:

```
Afghanistan, Caucasus, Channel, Falklands, GermanyCW, Iraq,
Kola, MarianaIslands, Nevada, Normandy, PersianGulf, Sinai, Syria
```

> ⚠️ **To add new maps:**  
> Add their internal folder names (e.g., from `DCS World/Mods/terrains`) to the `THEATRES` list in the script.  
> You can also find the exact name at the end of any `.stm` file.

---

## 💻 Building a Standalone .EXE

If you'd like to run this as a standalone app:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole TemplateDuplicator.v6.py
```

The resulting `.exe` will be in the `/dist` folder.

---

## 🪪 License
This project is licensed under the MIT License.

## Disclaimer
This tool is an unofficial utility for use with DCS: World. It is not affiliated with, endorsed by, or supported by Eagle Dynamics.
All trademarks and content related to DCS: World remain the property of Eagle Dynamics and their respective owners.

---

## 🙏 Credits

Created by [ChariotOfFLAME](https://github.com/ChariotOfFLAME)
