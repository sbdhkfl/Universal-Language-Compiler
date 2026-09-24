from importlib import import_module

NAMES={"python":"python","c":"c","cpp":"cpp","java":"java","csharp":"csharp","javascript":"javascript","visual-basic":"visual_basic","vb":"visual_basic","sql":"sql","r":"r","rust":"rust"}
def get_target(name):
    key=name.lower()
    if key not in NAMES: raise ValueError(f"Unsupported target: {name}")
    return import_module(f"targets.{NAMES[key]}")
