import importlib
from typing import Any


def check_reagents() -> None:
    """Checks for required reagents (pandas, numpy) and prints status/versions."""
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    dependencies = ["pandas", "numpy"]
    missing: list[str] = []
    loaded_modules: dict[str, Any] = {}

    for dep in dependencies:
        try:
            mod = importlib.import_module(dep)
            version = getattr(mod, "__version__", "unknown")
            print(f"  [OK] {dep} ({version})")
            loaded_modules[dep] = mod
        except ImportError:
            print(f"  [MISSING] {dep}")
            missing.append(dep)

    print()

    if missing:
        print("WARNING: Missing reagents detected!")
        print("To install using pip, run:")
        print("  pip install -r ex0/requirements.txt\n")
        print("To install using Poetry, run:")
        print("  poetry install")
        return

    print("pip vs Poetry:")
    print("  Data manipulation ready")
    print("  Numerical computation ready")
    print("\nrequirements.txt declares what to install; pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins the resolved")
    print("versions in poetry.lock so every install is identical.\n")
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    check_reagents()