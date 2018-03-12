#!/usr/bin/env python
from pathlib import Path
import sass

working_directory = Path('.')
scss_directory = working_directory / 'scss'
print(working_directory)

def task_css():
    dependencies = (list(scss_directory.glob('**/*.scss'))
                    + list(scss_directory.glob('**/*.css')))

    def compile_sass(src_dir, dest_dir):
        sass.compile(
            dirname=(src_dir, dest_dir),
            output_style='compressed'
        )

    return {
        'actions': [(compile_sass, (scss_directory, working_directory))],
        'file_dep': dependencies,
        'targets': [working_directory / 'lamenta.css'],
        'verbosity': 2,
    }

