from flask import Flask, render_template, request, jsonify
import os
import shutil

app = Flask(__name__)

def list_files_in_directory(directory_path):
    """Recursively list all files and subfolders in a directory."""
    files = []
    for root, dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), directory_path))
    return files

def get_unique_filename(dest_folder, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}({counter}){extension}"
        counter += 1
    return new_filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_folder_contents', methods=['POST'])
def get_folder_contents():
    folder_path = request.json.get('folderPath', '')
    if not os.path.isdir(folder_path):
        return jsonify({'status': 'error', 'message': 'Invalid folder path.'}), 400
    files_and_folders = list_files_in_directory(folder_path)
    return jsonify({'status': 'success', 'files': files_and_folders})

@app.route('/copy_files', methods=['POST'])
def copy_files():
    source_folder = request.form['sourceFolder']
    destination_folder = request.form['destinationFolder']
    selected_files = request.form.getlist('selectedFiles')
    sort_by_extension = request.form.get('sortByExtension') == 'true'  # checkbox sends string

    if not os.path.isdir(source_folder):
        return jsonify({'status': 'error', 'message': 'Invalid source folder path.'})

    if not os.path.isdir(destination_folder):
        return jsonify({'status': 'error', 'message': 'Invalid destination folder path.'})

    try:
        for file in selected_files:
            source_path = os.path.join(source_folder, file)

            if os.path.exists(source_path):
                if sort_by_extension:
                    # Sort into extension folder
                    _, extension = os.path.splitext(file)
                    extension = extension.lstrip('.').lower() or "unknown"
                    ext_folder = os.path.join(destination_folder, extension)
                    os.makedirs(ext_folder, exist_ok=True)
                    target_folder = ext_folder
                else:
                    target_folder = destination_folder

                unique_filename = get_unique_filename(target_folder, os.path.basename(file))
                destination_path = os.path.join(target_folder, unique_filename)
                shutil.copy(source_path, destination_path)

        return jsonify({'status': 'success', 'message': 'Files copied successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/copy', methods=['POST'])
def copy_files():
    destination_path = request.form['destination']
    auto_folder = request.form.get('auto_folder') == 'on'
    uploaded_files = request.files.getlist('source_folder')

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        if not filename:
            continue
        if auto_folder:
            ext = os.path.splitext(filename)[1][1:].lower()
            ext_folder = os.path.join(destination_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            file.save(os.path.join(ext_folder, os.path.basename(filename)))
        else:
            file.save(os.path.join(destination_path, os.path.basename(filename)))

    return '✅ Files copied successfully!'



if __name__ == '__main__':
    app.run(debug=True)

