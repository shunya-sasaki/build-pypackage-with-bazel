load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "pybind11_bazel",
    strip_prefix = "pybind11_bazel-fc56ce8a8b51e3dd941139d329b63ccfea1d304b",
    urls = ["https://github.com/pybind/pybind11_bazel/archive/fc56ce8a8b51e3dd941139d329b63ccfea1d304b.zip"],
)

# We still require the pybind library.
http_archive(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11.BUILD",
    strip_prefix = "pybind11-2.10.4",
    urls = ["https://github.com/pybind/pybind11/archive/v2.10.4.tar.gz"],
)

load("@pybind11_bazel//:python_configure.bzl", "python_configure")

python_configure(name = "local_config_python")
