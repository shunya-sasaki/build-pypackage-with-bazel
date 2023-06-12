import os
import shutil
import subprocess
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class BazelExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class BazelBuild(build_ext):
    def build_extension(self, ext: BazelExtension) -> None:
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name)
        extdir = ext_fullpath.parent.resolve()
        build_temp = Path(self.build_temp) / ext.name

        if not build_temp.exists():
            build_temp.mkdir(parents=True)

        package_name = ext.name.split(".")[0]  ## cpputils
        module_name = ext.name.split(".")[1]  ## lib

        subprocess.run(
            [
                "bazel",
                "--output_user_root",
                build_temp,
                "build",
                f"//src/{package_name}:{module_name}.so",
            ],
            cwd=build_temp,
            check=True,
        )

        for libfile in list(
            build_temp.glob(f"**/src/bin/{package_name}/{module_name}.so")
        ):
            if libfile.is_file():
                shutil.copy(libfile, extdir.joinpath(libfile.name))


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="cpputils",
    ext_modules=[BazelExtension("cpputils.lib")],
    cmdclass={"build_ext": BazelBuild},
    zip_safe=False,
)
