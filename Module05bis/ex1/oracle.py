import os
from dotenv import load_dotenv


def consult_oracle() -> None:
    """Load configuration without exposing secret values."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    load_dotenv(dotenv_path=env_path, override=False)

    print("ORACLE STATUS: Consulting the configuration...\n")

    matrix_mode = os.getenv("MATRIX_MODE", "development").strip().lower()
    if matrix_mode not in {"development", "production"}:
        print(
            f"WARNING: Unknown MATRIX_MODE '{matrix_mode}'; "
            "using development."
        )
        matrix_mode = "development"

    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    db_status = "Configured" if db_url else "Not configured"
    api_status = "Configured" if api_key else "Missing"
    zion_status = "Configured" if zion_endpoint else "Not configured"

    print("Configuration loaded:")
    print(f"  Mode: {matrix_mode}")
    if matrix_mode == "production":
        print("  Profile: Production validation enabled")
        missing = [
            name
            for name, value in (
                ("DATABASE_URL", db_url),
                ("API_KEY", api_key),
                ("ZION_ENDPOINT", zion_endpoint),
            )
            if not value
        ]
        if missing:
            print(
                "  [WARNING] Missing production settings: "
                f"{', '.join(missing)}"
            )
        else:
            print("  [OK] Required production settings are configured")
    else:
        print("  Profile: Development configuration")
    print(f"  Database: {db_status}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {log_level}")
    print(f"  Remote Network: {zion_status}\n")

    print("Configuration security check:")
    print("  [OK] Secret values are not printed")
    gitignore_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ".gitignore"
    )
    try:
        with open(gitignore_path, encoding="utf-8") as gitignore:
            env_is_ignored = any(
                line.strip() == ".env" for line in gitignore
            )
    except OSError as error:
        print(f"  [WARNING] Could not read .gitignore: {error}")
    else:
        if env_is_ignored:
            print("  [OK] .env is listed in ex1/.gitignore")
        else:
            print("  [WARNING] .env is not listed in ex1/.gitignore")
    print("  Environment variables take precedence over .env values.\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()
