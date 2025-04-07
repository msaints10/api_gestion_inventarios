import secrets
import base64
from pathlib import Path

def generate_secret_key():
    return base64.b64encode(secrets.token_bytes(32)).decode('utf-8')

def update_env_file():
    # Get project root directory (assuming this script is in api/utils)
    project_root = Path(__file__).parent.parent
    env_path = project_root / '.env'

    # Generate new keys
    jwt_secret_key = generate_secret_key()
    jwt_refresh_secret_key = generate_secret_key()

    if env_path.exists():
        # Read existing content
        with open(env_path, 'r') as f:
            lines = f.readlines()

        # Track if keys exist
        jwt_key_exists = False
        jwt_refresh_key_exists = False

        # Update existing keys if found
        for i, line in enumerate(lines):
            if line.startswith('JWT_SECRET_KEY='):
                lines[i] = f'JWT_SECRET_KEY={jwt_secret_key}\n'
                jwt_key_exists = True
            elif line.startswith('JWT_REFRESH_SECRET_KEY='):
                lines[i] = f'JWT_REFRESH_SECRET_KEY={jwt_refresh_secret_key}\n'
                jwt_refresh_key_exists = True

        # Add missing keys
        if not jwt_key_exists:
            lines.append(f'JWT_SECRET_KEY={jwt_secret_key}\n')
        if not jwt_refresh_key_exists:
            lines.append(f'JWT_REFRESH_SECRET_KEY={jwt_refresh_secret_key}\n')

        # Write back to file
        with open(env_path, 'w') as f:
            f.writelines(lines)
    else:
        # Create new .env file
        with open(env_path, 'w') as f:
            f.write(f'JWT_SECRET_KEY={jwt_secret_key}\n')
            f.write(f'JWT_REFRESH_SECRET_KEY={jwt_refresh_secret_key}\n')

    print(f"JWT keys generated and saved to {env_path}")
    print(f"JWT_SECRET_KEY={jwt_secret_key}")
    print(f"JWT_REFRESH_SECRET_KEY={jwt_refresh_secret_key}")

if __name__ == "__main__":
    update_env_file()