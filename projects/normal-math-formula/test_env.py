import shutil
import sys

import manim
import numpy as np


def find_binary(name):
    path = shutil.which(name)
    return path if path else "missing"


def test_environment():
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Interpreter prefix: {sys.prefix}")
    print(f"Manim version: {manim.__version__}")
    print(f"NumPy version: {np.__version__}")

    checks = {
        "latex": find_binary("latex"),
        "dvisvgm": find_binary("dvisvgm"),
        "ffmpeg": find_binary("ffmpeg"),
    }

    print("\nExternal tools")
    missing = []
    for name, path in checks.items():
        print(f"  {name}: {path}")
        if path == "missing":
            missing.append(name)

    if missing:
        print("\nEnvironment check failed.")
        print(f"Missing required tools: {', '.join(missing)}")
        raise SystemExit(1)

    print("\nEnvironment check passed.")
    print("Run the MathTex smoke test next to verify actual rendering.")


if __name__ == "__main__":
    test_environment()
