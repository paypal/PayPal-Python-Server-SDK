
# Environment-Based Client Initialization

The SDK client can also be initialized directly from environment variables using the `from_environment()` class method. This allows the SDK to automatically read configuration values from the runtime environment or a .env file.

## Example

```python
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PaypalServersdkClient.from_environment(dotenv_path='/path/to/.env')
```

You can also specify a path to a `.env` file by passing it to the `from_environment()` method:

The same method can accept keyword arguments to override any values read from the environment, and the arguments to override values should follow the same approach as code-based client initialization.

```python
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient

client = PaypalServersdkClient.from_environment(
    dotenv_path='/path/to/.env',
    timeout=0,  # overrides timeout from environment variable
)
```

Values provided through arguments take precedence over those defined in environment variables.

## Example `.env` File

```python
ENVIRONMENT=sandbox

O_AUTH_CLIENT_ID=ExampleOAuthClientId
O_AUTH_CLIENT_SECRET=ExampleOAuthClientSecret
O_AUTH_CLOCK_SKEW=5

TIMEOUT=60
MAX_RETRIES=3
BACKOFF_FACTOR=2
RETRY_STATUSES=408,413
RETRY_METHODS=GET,PUT,DELETE

# Logging Configuration
LOG_LEVEL=DEBUG
MASK_SENSITIVE_HEADERS=true

# Request Logging Configuration
REQUEST_LOG_BODY=true
REQUEST_LOG_HEADERS=true
REQUEST_INCLUDE_QUERY_IN_PATH=true
REQUEST_HEADERS_TO_INCLUDE=Content-Type,X-Request-ID
REQUEST_HEADERS_TO_EXCLUDE=Authorization
REQUEST_HEADERS_TO_UNMASK=X-Request-ID

# Response Logging Configuration
RESPONSE_LOG_BODY=true
RESPONSE_LOG_HEADERS=true
RESPONSE_HEADERS_TO_INCLUDE=Content-Type,X-Correlation-ID,Date,Server
RESPONSE_HEADERS_TO_EXCLUDE=Set-Cookie,Authorization,X-API-Key
RESPONSE_HEADERS_TO_UNMASK=X-Correlation-ID

# Proxy Configuration
PROXY_ADDRESS=http://localhost:3000
PROXY_PORT=8080
PROXY_USERNAME=username
PROXY_PASSWORD=password
```

## Note

- If an environment variable is not defined, the default SDK configuration value will be used.

