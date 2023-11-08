[![build](https://github.com/SystemRDL/PeakRDL-systemrdl/workflows/build/badge.svg)](https://github.com/SystemRDL/PeakRDL-systemrdl/actions?query=workflow%3Abuild+branch%3Amain)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/peakrdl-systemrdl.svg)](https://pypi.org/project/peakrdl-systemrdl)

# PeakRDL-systemrdl
Export a compiled register model into SystemRDL code.

Useful when converting from other imported file formats.

For the command line tool, see the [PeakRDL project](https://peakrdl.readthedocs.io).

## Example

The easiest way to use PeakRDL-systemrdl is via the [PeakRDL command line tool](https://peakrdl.readthedocs.io/):

```bash
# Install the command line tool
python3 -m pip install peakrdl

# Convert IP-XACT to SystemRDL
peakrdl systemrdl your_design.xml -o your_design.rdl
```
