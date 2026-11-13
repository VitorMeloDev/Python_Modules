import importlib


def check_reagents() -> None:
    """Check for the required reagents and report their versions."""
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    dependencies: dict[str, str] = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
    }
    missing: list[str] = []

    for dep, purpose in dependencies.items():
        try:
            mod = importlib.import_module(dep)
            version = getattr(mod, "__version__", "unknown")
            print(f"  [OK] {dep} ({version}) - {purpose} ready")
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
    print(
        "requirements.txt declares constraints; pip resolves "
        "compatible versions when installed."
    )
    print(
        "pyproject.toml uses the same constraints. Poetry can save "
        "exact versions in poetry.lock for repeatable installs.\n"
    )
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    check_reagents()
