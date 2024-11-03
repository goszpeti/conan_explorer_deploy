
from functools import cached_property
import os
from conans import ConanFile
from conan.tools.cmake import CMake
from conan.tools.meson import Meson
from conan.tools.google import Bazel

class MyConanClass(ConanFile):
    name = "conan_explorer_deploy"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "txt"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    no_copy_source = True

    @cached_property
    def build_system_conf(self):
        return os.getenv("BUILD_SYSTEM", "cmake").lower()

    def build_requirements(self):
        if self.build_system_conf == "cmake":
            self.tool_requires("cmake/3.29.0")
            self.tool_requires("ninja/1.12.1")
            self.generators.append("CMakeDeps")
            self.generators.append("CMakeToolchain")
        elif self.build_system_conf == "meson":
            self.tool_requires("meson/1.6.0")
            self.tool_requires("pkgconf/2.2.0")
            self.generators.append("PkgConfigDeps")
            self.generators.append("MesonToolchain")
        elif self.build_system_conf == "bazel":
            self.tool_requires("bazel/7.2.1")
            self.generators.append("BazelDeps")
            self.generators.append("BazelToolchain")

    def requirements(self):
        self.requires("ftxui/5.0.0", private=True)

    def get_build_system(self):
        if self.build_system_conf == "cmake":
                return CMake(self)
        elif self.build_system_conf == "meson":
                return Meson(self)
        elif self.build_system_conf == "bazel":
                return Bazel(self)

    def build(self):
        build_system = self.get_build_system()
        build_system.configure()
        build_system.build()

    def package(self):
        build_system = self.get_build_system()
        build_system.install()
