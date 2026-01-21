
# Payment Method

The customer and merchant payment preferences.

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payee_preferred` | [`PayeePaymentMethodPreference`](../../doc/models/payee-payment-method-preference.md) | Optional | The merchant-preferred payment methods.<br><br>**Default**: `"UNRESTRICTED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |

## Example (as JSON)

```json
{
  "payee_preferred": "UNRESTRICTED"
}
```

