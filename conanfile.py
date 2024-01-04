from conan import ConanFile
from conan.tools.files import copy


class MyPackage(ConanFile):
    name = "shared_module_a"
    license = "MIT"
    url = "https://github.com/thabok/deps-shared-mod-a"
    description = "Conan package for Shared Module A"
    exports_sources = "*.slx"
    no_copy_source = False

    def package(self):
        copy(self, "*.slx", self.source_folder, self.package_folder, keep_path=False)
