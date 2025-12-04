
# Getting Started with PayPal Server SDK

## Introduction

### Important Notes

- **Available Features:** This SDK currently contains only 5 of PayPal's API endpoints. Additional endpoints and functionality will be added in the future.

### Information

The PayPal Server SDK provides integration access to the PayPal REST APIs. The API endpoints are divided into distinct controllers:

- Orders Controller: [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/)
- Payments Controller: [Payments API v2](https://developer.paypal.com/docs/api/payments/v2)
- Vault Controller: [Payment Method Tokens API v3](https://developer.paypal.com/docs/api/payment-tokens/v3/) *Available in the US only.*
- Transaction Search Controller: [Transaction Search API v1](https://developer.paypal.com/docs/api/transaction-search/v1/)
- Subscriptions Controller: [Subscriptions API v1](https://developer.paypal.com/docs/api/subscriptions/v1/)

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install paypal-server-sdk==2.1.0
```

You can also view the package at:
https://pypi.python.org/pypi/paypal-server-sdk/2.1.0

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| proxy_settings | [`ProxySettings`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| client_credentials_auth_credentials | [`ClientCredentialsAuthCredentials`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
import logging

from paypalserversdk.configuration import Environment
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient

client = PaypalServersdkClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SANDBOX,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

### Environment-Based Client Initialization

```python
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PaypalServersdkClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production | PayPal Live Environment |
| Sandbox | **Default** PayPal Sandbox Environment |

## Authorization

This API uses the following authentication schemes.

* [`Oauth2 (OAuth 2 Client Credentials Grant)`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/auth/oauth-2-client-credentials-grant.md)

## List of APIs

* [Orders](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/controllers/orders.md)
* [Payments](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/controllers/payments.md)
* [Vault](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/controllers/vault.md)
* [Transaction Search](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/controllers/transaction-search.md)
* [Subscriptions](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/controllers/subscriptions.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/environment-based-client-initialization.md)
* [AbstractLogger](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/http-request.md)

### Utilities

* [ApiResponse](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/api-response.md)
* [ApiHelper](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/2.1.0/doc/unix-date-time.md)

