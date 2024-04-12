from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer

access_security = JwtAccessBearer(secret_key="your-secret-key", auto_error=True)
