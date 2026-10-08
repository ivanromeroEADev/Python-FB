"""Convierte un .py en un asset FBScript (.dbx) para FrostEd.

Uso:
    python build_fbscript.py <codigo.py> <carpeta_destino> <ruta_del_asset>

Ejemplo:
    python build_fbscript.py PyQV_S1_FollowTheValue.py ^
        D:/dev/dingo/dev/DingoData/Source/ztest/users/ivromero/Scripts ^
        ztest/users/ivromero/Scripts

Si el .dbx ya existe, conserva sus GUID y solo reemplaza el codigo.
"""

import os
import re
import sys
import uuid
from xml.sax.saxutils import escape

TEMPLATE = (
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<partition guid="{partition}" primaryInstance="{instance}" exportMode="All">\n'
    '\t<instance id="{name}" guid="{instance}" type="FBScriptPipeline.FBScript" exported="True">\n'
    '\t\t<field name="Name">{asset_path}/{name}</field>\n'
    '\t\t<field name="AssetFormat">1</field>\n'
    '\t\t<field name="Code">{code}</field>\n'
    '\t</instance>\n'
    '</partition>'
)


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 1

    source, target_dir, asset_path = sys.argv[1], sys.argv[2], sys.argv[3].strip("/")
    name = os.path.splitext(os.path.basename(source))[0]
    target = os.path.join(target_dir, name + ".dbx")

    with open(source, "r", encoding="ascii") as handle:
        code = handle.read().rstrip("\n")

    partition, instance = str(uuid.uuid4()), str(uuid.uuid4())
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8") as handle:
            existing = handle.read()
        found = re.search(r'<partition guid="([^"]+)" primaryInstance="([^"]+)"', existing)
        if found:
            partition, instance = found.group(1), found.group(2)

    text = TEMPLATE.format(
        partition=partition,
        instance=instance,
        name=name,
        asset_path=asset_path,
        code=escape(code, {'"': "&quot;", "'": "&apos;"}),
    )

    with open(target, "w", encoding="utf-8", newline="\r\n") as handle:
        handle.write(text)

    print("Escrito: " + target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
