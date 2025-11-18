# `rules_python` Package Index Reproduction

# Update -- This is fixed in 1.7!

The latest release for
[1.7.0](https://github.com/bazel-contrib/rules_python/releases/tag/1.7.0) fixes 
this issues since it pulls in
[#3311](https://github.com/bazel-contrib/rules_python/pull/3311). The `bazel
shutdown` behavior no longer affects running compiled binaries.

# Original Reproduction Details

There is an issue with `rules_python` where package metadata is fetched at bazel
startup even for targets that should be reliably cached.

This repository sets up a representative `rules_python` setup with some example
dependencies to demonstrate the issue.

For more information, see
https://github.com/bazel-contrib/rules_python/issues/3034.

## Reproducing

There is an example script that uses the dependencies to make a simple web
request. It can be run with `bazel run //:demo`.

1. Execute the script with `bazel run //:demo` with internet access to pypi.org
   enabled.
2. Run `bazel shutdown`
3. Disable internet access
4. Run the script again with `bazel run //:demo`. You should get the following
   output failure to download package data.
```
WARNING: Download from https://pypi.org/simple/certifi/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/mdurl/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/rich/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/twine/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/nh3/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/keyring/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/idna/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/zipp/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/urllib3/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/pkginfo/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/rfc3986/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/requests/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/markdown-it-py/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/jaraco-classes/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/jaraco-context/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/requests-toolbelt/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/more-itertools/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/docutils/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/pygments/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/readme-renderer/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/jaraco-functools/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/backports-tarfile/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/charset-normalizer/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/pycparser/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/cffi/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/importlib-metadata/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/jeepney/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/cryptography/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/secretstorage/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
WARNING: Download from https://pypi.org/simple/pywin32-ctypes/ failed: class com.google.devtools.build.lib.bazel.repository.downloader.UnrecoverableHttpException Unknown host: pypi.org
ERROR: /home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/simpleapi_download.bzl:131:14: Traceback (most recent call last):
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/extension.bzl", line 625, column 25, in _pip_impl
		mods = parse_modules(module_ctx, enable_pipstar = rp_config.enable_pipstar)
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/extension.bzl", line 501, column 36, in parse_modules
		out = _create_whl_repos(
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/extension.bzl", line 163, column 50, in _create_whl_repos
		requirements_by_platform = parse_requirements(
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/parse_requirements.bzl", line 171, column 36, in parse_requirements
		index_urls = get_index_urls(
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/extension.bzl", line 477, column 79, in lambda
		get_index_urls = lambda ctx, distributions: simpleapi_download(
	File "/home/nathanael/.cache/bazel/_bazel_nathanael/eb80ca678d97bb912e8d1117b445416a/external/rules_python~/python/private/pypi/simpleapi_download.bzl", line 131, column 14, in simpleapi_download
		_fail(
Error in fail: Failed to download metadata for ["nh3", "idna", "rich", "zipp", "mdurl", "twine", "certifi", "keyring", "pkginfo", "rfc3986", "urllib3", "docutils", "pygments", "requests", "jaraco-classes", "jaraco-context", "markdown-it-py", "more-itertools", "readme-renderer", "jaraco-functools", "backports-tarfile", "requests-toolbelt", "charset-normalizer", "importlib-metadata", "cffi", "jeepney", "pycparser", "cryptography", "secretstorage", "pywin32-ctypes"] for from urls: ["https://pypi.org/simple"].
If you would like to skip downloading metadata for these packages please add 'simpleapi_skip=[
    "nh3",
    "idna",
    "rich",
    "zipp",
    "mdurl",
    "twine",
    "certifi",
    "keyring",
    "pkginfo",
    "rfc3986",
    "urllib3",
    "docutils",
    "pygments",
    "requests",
    "jaraco-classes",
    "jaraco-context",
    "markdown-it-py",
    "more-itertools",
    "readme-renderer",
    "jaraco-functools",
    "backports-tarfile",
    "requests-toolbelt",
    "charset-normalizer",
    "importlib-metadata",
    "cffi",
    "jeepney",
    "pycparser",
    "cryptography",
    "secretstorage",
    "pywin32-ctypes",
]' to your 'pip.parse' call.
ERROR: Analysis of target '//:demo' failed; build aborted: error evaluating module extension pip in @@rules_python~//python/extensions:pip.bzl
INFO: Elapsed time: 3.720s, Critical Path: 0.03s
INFO: 1 process: 1 internal.
ERROR: Build did NOT complete successfully
ERROR: Build failed. Not running target
FAILED: 
    Fetching module extension pip in @@rules_python~//python/extensions:pip.bzl; Fetch package lists from PyPI index
```
5. Re-enable internet access and confirm that subsequent runs of `bazel run
   //:demo` still fail.
6. Call `bazel shutdown` once more and then `bazel run //:demo` to see things
   work again.
