
# Cancel Subscription Request

The cancel subscription request details.

## Structure

`CancelSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | The reason for the cancellation of a subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |

## Example

```python
from paypalserversdk.models.cancel_subscription_request import CancelSubscriptionRequest

cancel_subscription_request = CancelSubscriptionRequest(
    reason='reason8'
)
```

