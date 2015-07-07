from setuptools import setup, find_packages

setup(
    name = "biomartian",
    packages = find_packages(),
    version = "0.0.1",
    description = "Access biomart in Python or from the command line.",
    author = "Endre Bakken Stovner",
    author_email = "endrebak@stud.ntnu.no",
    url = "http://github.com/endrebak/biomartian",
    keywords = ["Bioinformatics"],
    license = ["GPL-3.0"],
    install_requires = ["widediaper", "pandas", "biopython"],
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Scientific/Engineering"],
    long_description = ("Access biomart from Python or the command line."
                        "See the url for more info.")
)
