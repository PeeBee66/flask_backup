import os

def backup_flask_app(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as backup_file:
        for root, dirs, files in os.walk(root_dir):
            # Ignore __pycache__ folder
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')

            for file in files:
                # Ignore flask_backup.py and flask_backup.txt
                if file in ['flask_backup.py', 'flask_backup.txt']:
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, root_dir)

                backup_file.write(f"\n{relative_path}\n")
                backup_file.write("=" * len(relative_path) + "\n")

                try:
                    with open(file_path, 'r', encoding='utf-8') as source_file:
                        backup_file.write(source_file.read())
                except Exception as e:
                    backup_file.write(f"Error reading file: {str(e)}\n")

                backup_file.write("\n\n")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    backup_filename = "flask_backup.txt"
    backup_path = os.path.join(project_root, backup_filename)

    backup_flask_app(project_root, backup_path)
    print(f"Backup completed: {backup_path}")
