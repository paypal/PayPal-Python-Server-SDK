
# Google Pay Payment Method

The type of the payment credential. Currently, only CARD is supported.

## Enumeration

`GooglePayPaymentMethod`

## Fields

| Name | Description |
|  --- | --- |
| `CARD` | CARD is the only value that Google Pay accepts. |

## Example

```python
from paypalserversdk.models.google_pay_payment_method import GooglePayPaymentMethod

google_pay_payment_method = GooglePayPaymentMethod.CARD
```

