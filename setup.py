import os
import re
import subprocess
import sys
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def build_extension(self, ext: CMakeExtension) -> None:
        # Must be in this form due to bug in .resolve() only fixed in Python 3.10+
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name)
        extdir = ext_fullpath.parent.resolve()


        build_temp = Path(self.build_temp) / ext.name

        print(f"build temp: {build_temp}")

        if not build_temp.exists():
            build_temp.mkdir(parents=True)

        # subprocess.run(
        #     ["cmake", ext.sourcedir, *cmake_args], cwd=build_temp, check=True
        # )
        # subprocess.run(
        #     ["cmake", "--build", ".", *build_args], cwd=build_temp, check=True
        # )


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="cpputils",
    ext_modules=[CMakeExtension("cpputils.lib")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
)
