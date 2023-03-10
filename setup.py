import os
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


with open(os.path.join("src/peakrdl_systemrdl", "__about__.py"), encoding='utf-8') as f:
    v_dict = {}
    exec(f.read(), v_dict)
    version = v_dict['__version__']

setuptools.setup(
    name="peakrdl-systemrdl",
    version=version,
    author="Alex Mykyta",
    author_email="amykyta3@github.com",
    description="Write a register model to a SystemRDL file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SystemRDL/PeakRDL-systemrdl",
    package_dir={'': 'src'},
    packages=setuptools.find_packages("src"),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        "systemrdl-compiler>=1.25.1",
    ],
    entry_points = {
        "peakrdl.exporters": [
            'systemrdl = peakrdl_systemrdl.__peakrdl__:ExporterCmd'
        ]
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ),
    project_urls={
        "Source": "https://github.com/SystemRDL/PeakRDL-systemrdl",
        "Tracker": "https://github.com/SystemRDL/PeakRDL-systemrdl/issues",
    },
)
