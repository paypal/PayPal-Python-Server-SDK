
# Capture Subscription Request

The charge amount from the subscriber.

## Structure

`CaptureSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `note` | `str` | Required | The reason or note for the subscription charge.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `capture_type` | [`CaptureType`](../../doc/models/capture-type.md) | Required | The type of capture.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `amount` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example

```python
from paypalserversdk.models.capture_subscription_request import CaptureSubscriptionRequest
from paypalserversdk.models.capture_type import CaptureType
from paypalserversdk.models.money import Money

capture_subscription_request = CaptureSubscriptionRequest(
    note='note8',
    capture_type=CaptureType.OUTSTANDING_BALANCE,
    amount=Money(
        currency_code='currency_code6',
        value='value0'
    )
)
```

