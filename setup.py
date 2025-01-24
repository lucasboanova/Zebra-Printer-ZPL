from cx_Freeze import setup, Executable

# ...existing code...

# Add the icon to the executable
executables = [
    Executable(
        script="main.py",
        base="Win32GUI",
        icon="path/to/your/icon.ico"
    )
]

# Include additional files
include_files = [
    ('csvFile/tonner.csv', 'csvFile/tonner.csv'),
    # Add other files if needed
]

setup(
    name="PrinterZPL",
    version="1.0",
    description="Descrição do seu aplicativo",
    options={
        'build_exe': {
            'include_files': include_files,
        }
    },
    executables=executables
)
