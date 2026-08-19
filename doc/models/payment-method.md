
# Payment Method

The customer and merchant payment preferences.

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payee_preferred` | [`PayeePaymentMethodPreference`](../../doc/models/payee-payment-method-preference.md) | Optional | The merchant-preferred payment methods.<br><br>**Default**: `"UNRESTRICTED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |

## Example

```python
from paypalserversdk.models.payee_payment_method_preference import PayeePaymentMethodPreference
from paypalserversdk.models.payment_method import PaymentMethod

payment_method = PaymentMethod(
    payee_preferred=PayeePaymentMethodPreference.UNRESTRICTED
)
```

