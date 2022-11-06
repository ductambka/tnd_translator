# Make sure you have the latest version of PyPA’s build installed:
py -m pip install --upgrade build

# Now run this command from the same directory where pyproject.toml is located:
py -m build

# Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:
py -m pip install --upgrade twine
