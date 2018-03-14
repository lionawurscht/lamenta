#!/usr/bin/env python
from pathlib import Path
import sass
import os

package_directory = Path(os.path.dirname(os.path.abspath(__file__)))
package_name = package_directory.name
scss_directory = package_directory / 'scss'

def task_css():
    dependencies = (list(scss_directory.glob('**/*.scss'))
                    + list(scss_directory.glob('**/*.css')))

    def compile_sass(src_dir, dest_dir):
        sass.compile(
            dirname=(src_dir, dest_dir),
            output_style='compressed'
        )

    target = package_directory / 'lamenta.css'

    return {
        'basename': package_name + ':css',
        'actions': [(compile_sass, (scss_directory, package_directory))],
        'file_dep': dependencies,
        'targets': [target],
        'verbosity': 2,
    }

