# All SystemRDL 2.0 keywords
RDL_KEYWORDS = {
    "abstract", "accesstype", "addressingtype", "addrmap", "alias", "all",
    "bit", "boolean", "bothedge", "compact", "component", "componentwidth",
    "constraint", "default", "encode", "enum", "external", "false", "field",
    "fullalign", "hw", "inside", "internal", "level", "longint", "mem", "na",
    "negedge", "nonsticky", "number", "onreadtype", "onwritetype", "posedge",
    "property", "r", "rclr", "ref", "reg", "regalign", "regfile", "rset",
    "ruser", "rw", "rw1", "signal", "string", "struct", "sw", "this", "true",
    "type", "unsigned", "w", "w1", "wclr", "woclr", "woset", "wot", "wr",
    "wset", "wuser", "wzc", "wzs", "wzt",
}

def kw_filter(s: str) -> str:
    """
    Make all user identifiers 'safe' and ensure they do not collide with
    SystemRDL keywords.

    SystemRDL allows identifier escaping with a preceding backslash
    """
    if s in RDL_KEYWORDS:
        s = "\\" + s
    return s
