
# Paypal Payment Token Customer Type

The customer type associated with the PayPal payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a consumer., The customer type associated with a digital wallet payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a consumer.

## Enumeration

`PaypalPaymentTokenCustomerType`

## Fields

| Name | Description |
|  --- | --- |
| `CONSUMER` | The customer vaulting the PayPal payment token is a consumer on the merchant / platform. |
| `BUSINESS` | The customer vaulting the PayPal payment token is a business on merchant / platform. |

## Example

```python
from paypalserversdk.models.paypal_payment_token_customer_type import PaypalPaymentTokenCustomerType

paypal_payment_token_customer_type = PaypalPaymentTokenCustomerType.CONSUMER
```

