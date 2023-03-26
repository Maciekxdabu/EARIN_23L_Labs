import pkg_resources

# get a list of all installed packages and their version numbers
installed_packages = pkg_resources.working_set

# loop over the installed packages and check if they require pip install
for package in installed_packages:
    if package.key.startswith('pip'):
        continue  # skip pip packages
    try:
        package_dist = pkg_resources.get_distribution(package.key)
        if package_dist.has_metadata('RECORD'):
            print(f"{package.key} was installed via pip.")
    except:
        pass