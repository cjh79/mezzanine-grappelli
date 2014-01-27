
from setuptools import setup, find_packages
from mezzanine_grappelli import __version__


install_requires = [
    "django-filebrowser >= 3.5.3",
    "django-grappelli >= 2.5.1",
]

setup(
    name="mezzanine-grappelli",
    version=__version__,
    author="Sylvain Fankhauser",
    author_email="sylvain@fankhauser.name",
    description="mezzanine-grappelli makes Mezzanine ♥ Grappelli",
    long_description=open("README.rst", 'rb').read().decode('utf-8'),
    license="BSD",
    url="https://github.com/sephii/mezzanine-grappelli/",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
])