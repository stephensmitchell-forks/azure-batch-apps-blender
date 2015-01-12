#-------------------------------------------------------------------------
# The Blender Batch Apps Sample
#
# Copyright (c) Microsoft Corporation. All rights reserved. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#--------------------------------------------------------------------------
"""Zip up Blender Addon"""

import sys
import os
import subprocess
import shutil
import zipfile

VERSION = "0.1.0"

def main():
    """Build Blender Addon package"""

    python_exe = os.path.join(sys.prefix, "python.exe")
    if not os.path.exists(python_exe):
        print("Cannot find python.exe at path: {0}".format(python_exe))
        return

    print("Building package...")

    package_dir = os.path.abspath("build")
    if not os.path.isdir(package_dir):
        try:
            os.mkdir(package_dir)
        except:
            print("Cannot create build dir at path: {0}".format(package_dir))
            return

    package = os.path.join(package_dir, "batchapps-blender-{0}.zip".format(VERSION))
    source = os.path.abspath("batchapps_blender")

    with zipfile.ZipFile(package, mode='w') as blend_zip:
        for root, dirs, files in os.walk(source):
            if root.endswith("__pycache__"):
                continue

            for file in files:
                blend_zip.write(os.path.relpath(os.path.join(root, file)))

    print("Package complete!")

if __name__ == '__main__':
    main()