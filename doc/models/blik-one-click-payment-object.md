
# Blik One Click Payment Object

Information used to pay using BLIK one-click flow.

## Structure

`BlikOneClickPaymentObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `consumer_reference` | `str` | Optional | The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[ -~]{3,64}$` |

## Example

```python
from paypalserversdk.models.blik_one_click_payment_object import BlikOneClickPaymentObject

blik_one_click_payment_object = BlikOneClickPaymentObject(
    consumer_reference='consumer_reference2'
)
```

