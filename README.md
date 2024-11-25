
# Getting Started with PayPal Server SDK

## Introduction

### ⚠️ Beta Release Notice

This version is considered a **beta release**. While we have done our best to ensure stability and functionality, there may still be bugs, incomplete features, or breaking changes in future updates.

#### Important Notes

- **Available Features:** This SDK currently contains only 3 of PayPal's API endpoints. Additional endpoints and functionality will be added in the future.
- **API Changes:** Expect potential changes in APIs and features as we finalize the product.

### Information

The PayPal Server SDK provides integration access to the PayPal REST APIs. The API endpoints are divided into distinct controllers:

- Orders Controller: <a href="https://developer.paypal.com/docs/api/orders/v2/">Orders API v2</a>
- Payments Controller: <a href="https://developer.paypal.com/docs/api/payments/v2/">Payments API v2</a>
- Vault Controller: <a href="https://developer.paypal.com/docs/api/payment-tokens/v3/">Payment Method Tokens API v3</a> *Available in the US only.*

Find out more here: [https://developer.paypal.com/docs/api/orders/v2/](https://developer.paypal.com/docs/api/orders/v2/)

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install paypal-server-sdk==0.6.1
```

You can also view the package at:
https://pypi.python.org/pypi/paypal-server-sdk/0.6.1

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `logging_configuration` | [`LoggingConfiguration`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| `client_credentials_auth_credentials` | [`ClientCredentialsAuthCredentials`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
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

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production | PayPal Live Environment |
| Sandbox | **Default** PayPal Sandbox Environment |

## Authorization

This API uses the following authentication schemes.

* [`Oauth2 (OAuth 2 Client Credentials Grant)`](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/auth/oauth-2-client-credentials-grant.md)

## List of APIs

* [Orders](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/controllers/orders.md)
* [Payments](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/controllers/payments.md)
* [Vault](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/controllers/vault.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/http-response.md)
* [HttpRequest](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/http-request.md)
* [LoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/response-logging-configuration.md)
* [AbstractLogger](https://www.github.com/paypal/PayPal-Python-Server-SDK/tree/0.6.1/doc/abstract-logger.md)

