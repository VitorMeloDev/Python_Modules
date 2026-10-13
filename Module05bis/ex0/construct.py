import os
import site
import sys


def check_laboratory() -> None:
    """Detects and displays information about the Python environment."""
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print()

    if not in_venv:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("  python3 -m venv lab_env")
        print("  source lab_env/bin/activate # On Unix")
        print("  lab_env\\Scripts\\activate   # On Windows\n")
        print("Then run this program again.")
    else:
        env_name = os.path.basename(sys.prefix)
        site_packages = site.getsitepackages()
        reagent_path = site_packages[0] if site_packages else "Unknown"

        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.\n")
        print("Reagent installation path:")
        print(reagent_path)


if __name__ == "__main__":
    check_laboratory()