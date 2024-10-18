# Vault

Use the `/vault` resource to create, retrieve, and delete payment and setup tokens.

```python
vault_controller = client.vault
```

## Class Name

`VaultController`

## Methods

* [Customer Payment-Tokens Get](../../doc/controllers/vault.md#customer-payment-tokens-get)
* [Payment-Tokens Get](../../doc/controllers/vault.md#payment-tokens-get)
* [Payment-Tokens Create](../../doc/controllers/vault.md#payment-tokens-create)
* [Setup-Tokens Create](../../doc/controllers/vault.md#setup-tokens-create)
* [Payment-Tokens Delete](../../doc/controllers/vault.md#payment-tokens-delete)
* [Setup-Tokens Get](../../doc/controllers/vault.md#setup-tokens-get)


# Customer Payment-Tokens Get

Returns all payment tokens for a customer.

```python
def customer_payment_tokens_get(self,
                               options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Query, Required | A unique identifier representing a specific customer in merchant's/partner's system or records.<br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `36`, *Pattern*: `^[0-9a-zA-Z_-]+$` |
| `page_size` | `int` | Query, Optional | A non-negative, non-zero integer indicating the maximum number of results to return at one time.<br>**Default**: `5`<br>**Constraints**: `>= 1` |
| `page` | `int` | Query, Optional | A non-negative, non-zero integer representing the page of the results.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `total_required` | `bool` | Query, Optional | A boolean indicating total number of items (total_items) and pages (total_pages) are expected to be returned in the response.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CustomerVaultPaymentTokensResponse`](../../doc/models/customer-vault-payment-tokens-response.md).

## Example Usage

```python
collect = {
    'customer_id': 'customer_id8',
    'page_size': 5,
    'page': 1,
    'total_required': False
}
result = vault_controller.customer_payment_tokens_get(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |


# Payment-Tokens Get

Returns a readable representation of vaulted payment source associated with the payment token id.

```python
def payment_tokens_get(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | ID of the payment token.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[0-9a-zA-Z_-]+$` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PaymentTokenResponse`](../../doc/models/payment-token-response.md).

## Example Usage

```python
id = 'id0'

result = vault_controller.payment_tokens_get(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |


# Payment-Tokens Create

Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

```python
def payment_tokens_create(self,
                         options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paypal_request_id` | `str` | Header, Required | The server stores keys for 3 hours. |
| `body` | [`PaymentTokenRequest`](../../doc/models/payment-token-request.md) | Body, Required | Payment Token creation with a financial instrument and an optional customer_id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PaymentTokenResponse`](../../doc/models/payment-token-response.md).

## Example Usage

```python
collect = {
    'paypal_request_id': 'PayPal-Request-Id6',
    'body': PaymentTokenRequest(
        payment_source=PaymentTokenRequestPaymentSource()
    )
}
result = vault_controller.payment_tokens_create(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | Request contains reference to resources that do not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |


# Setup-Tokens Create

Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

```python
def setup_tokens_create(self,
                       options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paypal_request_id` | `str` | Header, Required | The server stores keys for 3 hours. |
| `body` | [`SetupTokenRequest`](../../doc/models/setup-token-request.md) | Body, Required | Setup Token creation with a instrument type optional financial instrument details and customer_id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SetupTokenResponse`](../../doc/models/setup-token-response.md).

## Example Usage

```python
collect = {
    'paypal_request_id': 'PayPal-Request-Id6',
    'body': SetupTokenRequest(
        payment_source=SetupTokenRequestPaymentSource()
    )
}
result = vault_controller.setup_tokens_create(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |


# Payment-Tokens Delete

Delete the payment token associated with the payment token id.

```python
def payment_tokens_delete(self,
                         id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | ID of the payment token.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[0-9a-zA-Z_-]+$` |

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
id = 'id0'

result = vault_controller.payment_tokens_delete(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |


# Setup-Tokens Get

Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

```python
def setup_tokens_get(self,
                    id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | ID of the setup token.<br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `36`, *Pattern*: `^[0-9a-zA-Z_-]+$` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SetupTokenResponse`](../../doc/models/setup-token-response.md).

## Example Usage

```python
id = 'id0'

result = vault_controller.setup_tokens_get(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |

