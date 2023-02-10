from typing import TYPE_CHECKING

from .exporter import SystemRDLExporter

if TYPE_CHECKING:
    import argparse
    from systemrdl.node import AddrmapNode

class ExporterCmd:
    short_desc = "Export the register model to SystemRDL"

    def do_export(self, top_node: 'AddrmapNode', options: 'argparse.Namespace') -> None:
        x = SystemRDLExporter()
        x.export(top_node, options.output)
