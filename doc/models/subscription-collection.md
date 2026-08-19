
# Subscription Collection

The list of subscriptions.

## Structure

`SubscriptionCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriptions` | [`List[Subscription]`](../../doc/models/subscription.md) | Optional | An array of subscriptions.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.subscription import Subscription
from paypalserversdk.models.subscription_collection import SubscriptionCollection

subscription_collection = SubscriptionCollection(
    subscriptions=[
        Subscription(
            plan_id='plan_id8',
            start_time='start_time0',
            quantity='quantity2',
            shipping_amount=Money(
                currency_code='currency_code0',
                value='value6'
            )
        )
    ]
)
```

