
# Activate Subscription Request

The activate subscription request details.

## Structure

`ActivateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | The reason for activation of a subscription. Required to reactivate the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |

## Example

```python
from paypalserversdk.models.activate_subscription_request import ActivateSubscriptionRequest

activate_subscription_request = ActivateSubscriptionRequest(
    reason='reason4'
)
```

