from setuptools import setup

version_number = "1.0.3dev"  # this must be defined here so we can import it elsewhere

try:
    with open("README.md") as readmefile:
        long_description = readmefile.read()
except IOError:
    long_description = ""


if __name__ == "__main__":
    # remove file if it exists and re-write with current version number
    fp = open('psiturk/version.py',"w+")
    fp.write("version_number = '%s'\n" % version_number)
    fp.flush()
    fp.close()

    setup(
        name = "PsiTurk",
        version = version_number,
        packages = ["psiturk"],
        include_package_data = True,
        zip_safe = False,
        entry_points = {
            'console_scripts': [
                'psiturk = psiturk.command_line:process',
                'psiturk-dashboard = psiturk.command_line:process',
                'psiturk-server = psiturk.command_line:process',
                'psiturk-setup-example = psiturk.command_line:process'
            ]
        },
        setup_requires = [],
        install_requires = ["argparse", "Flask", "SQLAlchemy", "gunicorn", "boto>=2.9"],
        author = "NYU Computation and Cognition Lab",
        author_email = "authors@psiturk.org",
        description = "An open platform for science on Amazon Mechanical Turk",
        long_description = long_description,
        url = "http://github.com/NYUCCL/psiturk"
    )

