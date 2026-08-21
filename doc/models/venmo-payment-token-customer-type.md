
# Venmo Payment Token Customer Type

The customer type associated with the Venmo payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a consumer.

## Enumeration

`VenmoPaymentTokenCustomerType`

## Fields

| Name | Description |
|  --- | --- |
| `CONSUMER` | The customer vaulting the Venmo payment token is a consumer on the merchant / platform. |
| `BUSINESS` | The customer vaulting the Venmo payment token is a business on merchant / platform. |

## Example

```python
from paypalserversdk.models.venmo_payment_token_customer_type import VenmoPaymentTokenCustomerType

venmo_payment_token_customer_type = VenmoPaymentTokenCustomerType.CONSUMER
```

