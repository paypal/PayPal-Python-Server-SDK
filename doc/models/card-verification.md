
# Card Verification

The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar Auth, 3DS).

## Structure

`CardVerification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`OrdersCardVerificationMethod`](../../doc/models/orders-card-verification-method.md) | Optional | The method used for card verification.<br><br>**Default**: `"SCA_WHEN_REQUIRED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |

## Example

```python
from paypalserversdk.models.card_verification import CardVerification
from paypalserversdk.models.orders_card_verification_method import OrdersCardVerificationMethod

card_verification = CardVerification(
    method=OrdersCardVerificationMethod.SCA_WHEN_REQUIRED
)
```

