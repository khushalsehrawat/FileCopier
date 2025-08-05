# FileCopier
# 📁 File Copier – Web App (Flask + JS)

A **powerful, easy-to-use** web application for copying files from one folder to another on your local system. Supports **selective copying**, **file extension-based folder organization**, and a modern **premium UI** with a user-friendly interface.

---

## 🚀 Features

- ✅ List all files in a given source directory (recursive)
- ✅ Select individual or all files to copy
- ✅ Input source and destination folders
- ✅ **Auto-create folders by file type/extension** (e.g., pdf, png, txt)
- ✅ Prevents overwriting with smart name conflict resolution
- ✅ Toggle: enable/disable extension-wise sorting
- ✅ Built with Flask, HTML5, CSS3, JavaScript (vanilla), Bootstrap 5
- ✅ Fully responsive and mobile-friendly
- ✅ Clean, modern UI with gradient background and neumorphic styling

---

## 🖥️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | Python 3, Flask    |
| Frontend   | HTML5, CSS3, JS    |
| UI Styling | Bootstrap 5, Custom CSS |
| Deployment | Localhost (Flask dev server) |

---

## 🧩 Project Structure

```
file-copier/
├── app.py                   # Flask backend with routes & logic
├── templates/
│   └── index.html           # Frontend HTML
├── static/
│   └── style.css            # Premium UI CSS
├── README.md                # You're here!
```

---

## 📸 Screenshots

> *(Add screenshots here if available)*

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/file-copier.git
cd file-copier
```

### 2. Install Python Dependencies

```bash
pip install flask
```

> Make sure Python 3.6+ is installed.

### 3. Run the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💡 How It Works

### 🗂 Folder Browsing

- User inputs a valid source folder path.
- Backend uses `os.walk()` to list all files recursively.
- Each file is rendered as a checkbox with relative path.

### 📤 File Copying

- User selects desired files, inputs destination path.
- Optional toggle to organize files by **extension**.
- Backend checks for:
  - Source/destination path validity
  - File existence
  - File extension
- If enabled, creates subfolders like `/pdf`, `/png`, etc.
- Avoids overwrites with `(1)`, `(2)` suffix logic.

---

## ✅ Extension-Based Folder Logic

- `.pdf` → `/destination/pdf/`
- `.jpg` → `/destination/jpg/`
- `.txt` → `/destination/txt/`
- No extension → `/destination/unknown/`

This keeps your copied folder **neatly organized**.

---

## ⚙️ Configuration

You can tweak:

- Folder scanning logic in `list_files_in_directory()`
- Custom extension behavior
- MIME-based type detection (advanced)
- Add logging or audit features

---

## 📦 Future Enhancements (Ideas)

- Drag & drop support
- Real file preview thumbnails
- Desktop app version with PyInstaller or Electron
- Recently copied file history
- Compression (zip copied folders)

---

## 🤝 Contributing

Pull requests welcome! Feel free to fork the repo and submit PRs to add features, fix bugs, or improve UI.

---

## 🛡️ Disclaimer

This project works on **local file paths** — it does **not upload or share** your files anywhere. It's built for local file organization purposes.

---

## 📄 License

MIT License – Free to use, modify, and distribute.

---

## 🙏 Credits

Built with ❤️ by [Your Name] – combining frontend elegance with backend utility.

---

## 📬 Contact

For feedback, ideas, or collaborations:
📧 your.email@example.com  
🔗 [LinkedIn Profile](https://linkedin.com/in/your-profile)

---
