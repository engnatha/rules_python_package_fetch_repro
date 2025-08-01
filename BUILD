load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_uv//uv:pip.bzl", "pip_compile")

pip_compile(
    name = "requirements",
    # Specify a compatible runtime, if unspecified we get this:
    # Error: 'PyRuntimeInfo' value has no field or method 'interpreter_version_info'
    py3_runtime = "@python_3_13_4//:py3_runtime",
    requirements_in = ":requirements.txt",
    requirements_txt = "requirements_lock.txt",
)

py_binary(
    name = "demo",
    srcs = ["demo.py"],
    deps = ["@pypi//click"]
)