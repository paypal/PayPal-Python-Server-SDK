# Payments

Use the `/payments` resource to authorize, capture, void authorizations, and retrieve captures.

```python
payments_controller = client.payments
```

## Class Name

`PaymentsController`

## Methods

* [Authorizations Get](../../doc/controllers/payments.md#authorizations-get)
* [Authorizations Capture](../../doc/controllers/payments.md#authorizations-capture)
* [Authorizations Reauthorize](../../doc/controllers/payments.md#authorizations-reauthorize)
* [Authorizations Void](../../doc/controllers/payments.md#authorizations-void)
* [Captures Get](../../doc/controllers/payments.md#captures-get)
* [Captures Refund](../../doc/controllers/payments.md#captures-refund)
* [Refunds Get](../../doc/controllers/payments.md#refunds-get)


# Authorizations Get

Shows details for an authorized payment, by ID.

```python
def authorizations_get(self,
                      authorization_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_id` | `str` | Template, Required | The ID of the authorized payment for which to show details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PaymentAuthorization`](../../doc/models/payment-authorization.md).

## Example Usage

```python
authorization_id = 'authorization_id8'

result = payments_controller.authorizations_get(authorization_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Authorizations Capture

Captures an authorized payment, by ID.

```python
def authorizations_capture(self,
                          options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_id` | `str` | Template, Required | The PayPal-generated ID for the authorized payment to capture. |
| `pay_pal_request_id` | `str` | Header, Optional | The server stores keys for 45 days. |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul> |
| `body` | [`CaptureRequest`](../../doc/models/capture-request.md) | Body, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CapturedPayment`](../../doc/models/captured-payment.md).

## Example Usage

```python
collect = {
    'authorization_id': 'authorization_id8',
    'prefer': 'return=minimal',
    'body': CaptureRequest(
        final_capture=False
    )
}
result = payments_controller.authorizations_capture(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request failed because it is not well-formed or is syntactically incorrect or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The request failed because it is semantically incorrect or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Authorizations Reauthorize

Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available, reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period, you can issue multiple re-authorizations after the honor period expires.<br/><br/>If 30 days have transpired since the date of the original authorization, you must create an authorized payment instead of reauthorizing the original authorized payment.<br/><br/>A reauthorized payment itself has a new honor period of three days.<br/><br/>You can reauthorize an authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of $75 USD.<br/><br/>Supports only the `amount` request parameter.<blockquote><strong>Note:</strong> This request is currently not supported for Partner use cases.</blockquote>

```python
def authorizations_reauthorize(self,
                              options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_id` | `str` | Template, Required | The PayPal-generated ID for the authorized payment to reauthorize. |
| `pay_pal_request_id` | `str` | Header, Optional | The server stores keys for 45 days. |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul> |
| `body` | [`ReauthorizeRequest`](../../doc/models/reauthorize-request.md) | Body, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PaymentAuthorization`](../../doc/models/payment-authorization.md).

## Example Usage

```python
collect = {
    'authorization_id': 'authorization_id8',
    'prefer': 'return=minimal'
}
result = payments_controller.authorizations_reauthorize(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request failed because it is not well-formed or is syntactically incorrect or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The request failed because it either is semantically incorrect or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Authorizations Void

Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully captured.

```python
def authorizations_void(self,
                       options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_id` | `str` | Template, Required | The PayPal-generated ID for the authorized payment to void. |
| `pay_pal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion).<blockquote><strong>Note:</strong>For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.</blockquote> |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul> |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PaymentAuthorization`](../../doc/models/payment-authorization.md).

## Example Usage

```python
collect = {
    'authorization_id': 'authorization_id8',
    'prefer': 'return=minimal'
}
result = payments_controller.authorizations_void(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request failed because it is not well-formed or is syntactically incorrect or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 409 | The request failed because a previous call for the given resource is in progress. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The request failed because it either is semantically incorrect or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Captures Get

Shows details for a captured payment, by ID.

```python
def captures_get(self,
                capture_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capture_id` | `str` | Template, Required | The PayPal-generated ID for the captured payment for which to show details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CapturedPayment`](../../doc/models/captured-payment.md).

## Example Usage

```python
capture_id = 'capture_id2'

result = payments_controller.captures_get(capture_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Captures Refund

Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For a partial refund, include an <code>amount</code> object in the JSON request body.

```python
def captures_refund(self,
                   options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capture_id` | `str` | Template, Required | The PayPal-generated ID for the captured payment to refund. |
| `pay_pal_request_id` | `str` | Header, Optional | The server stores keys for 45 days. |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul> |
| `pay_pal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion).<blockquote><strong>Note:</strong>For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.</blockquote> |
| `body` | [`RefundRequest`](../../doc/models/refund-request.md) | Body, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Refund`](../../doc/models/refund.md).

## Example Usage

```python
collect = {
    'capture_id': '1234',
    'pay_pal_request_id': '1234',
    'prefer': 'return=minimal',
    'pay_pal_auth_assertion': 'PayPal-Auth-Assertion',
    'body': RefundRequest(
        amount=Money(
            currency_code='USD',
            value='1.44'
        ),
        note_to_payer='Defective product'
    )
}
result = payments_controller.captures_refund(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request failed because it is not well-formed or is syntactically incorrect or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 409 | The request failed because a previous call for the given resource is in progress. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The request failed because it either is semantically incorrect or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Refunds Get

Shows details for a refund, by ID.

```python
def refunds_get(self,
               refund_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund_id` | `str` | Template, Required | The PayPal-generated ID for the refund for which to show details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Refund`](../../doc/models/refund.md).

## Example Usage

```python
refund_id = 'refund_id4'

result = payments_controller.refunds_get(refund_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The request failed because the caller has insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The request failed because the resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | The request failed because an internal server error occurred. | `APIException` |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |

