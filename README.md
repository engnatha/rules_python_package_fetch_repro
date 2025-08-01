# rules_python_index_url_repro
Rules python has a convenient feature to use separate indexes instead of pypi.org. This messes with the bazel cache and causes regular fetches of metadata with no changes to the repo.
