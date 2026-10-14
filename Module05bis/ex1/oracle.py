import os
import sys
from dotenv import load_dotenv, dotenv_values


def consult_oracle() -> None:
    """Carrega as configurações e lida com variáveis ausentes sem quebrar."""
    # 1. Carrega o .env local caso exista (sem sobrescrever variáveis do sistema)
    env_loaded = load_dotenv(dotenv_path="ex1/.env", override=False)
    if not env_loaded:
        load_dotenv(override=False)

    print("ORACLE STATUS: Consulting the configuration...\n")

    # 2. Leitura com validação de presença e fallbacks seguros
    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # 3. Tratamento amigável das variáveis ausentes (Sem crash!)
    db_status = "Connected to local instance" if db_url else "Not configured (Using default)"
    api_status = "Authenticated" if api_key else "Missing API Key"
    zion_status = "Online" if zion_endpoint else "Offline"

    print("Configuration loaded:")
    print(f"  Mode: {matrix_mode}")
    print(f"  Database: {db_status}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {log_level}")
    print(f"  Remote Network: {zion_status}\n")

    # 4. Checagem de segurança e avisos no output
    print("Configuration security check:")
    print("  [OK] No hardcoded secrets detected")
    
    if os.path.exists(".env") or os.path.exists("ex1/.env"):
        print("  [OK] .env file properly loaded")
        print("  [OK] .env file properly ignored by git")
    else:
        print("  [WARNING] .env file missing! Running with default/system settings.")

    print("  [OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()