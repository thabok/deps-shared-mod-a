from os.path import join

from conan import ConanFile
from conan.tools.files import copy


class MyPackage(ConanFile):
    name = "shared_module_a"
    version = "1.0.1"
    license = "MIT"
    url = "https://github.com/thabok/deps-shared-mod-a"
    description = "Conan package for Shared Module A"
    exports_sources = "shared_module_a.slx"  # This line includes your file in the package
    no_copy_source = False

    def package(self):
        copy(self, "*.slx", self.source_folder, self.package_folder)
