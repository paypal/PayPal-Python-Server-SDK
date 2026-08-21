
# Plan Collection

The list of plans with details.

## Structure

`PlanCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plans` | [`List[BillingPlan]`](../../doc/models/billing-plan.md) | Optional | An array of plans.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `total_items` | `int` | Optional | The total number of items.<br><br>**Constraints**: `>= 0`, `<= 500000000` |
| `total_pages` | `int` | Optional | The total number of pages.<br><br>**Constraints**: `>= 0`, `<= 100000000` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |

## Example

```python
from paypalserversdk.models.billing_plan import BillingPlan
from paypalserversdk.models.plan_collection import PlanCollection
from paypalserversdk.models.subscription_plan_status import SubscriptionPlanStatus

plan_collection = PlanCollection(
    plans=[
        BillingPlan(
            product_id='product_id0',
            name='name4',
            status=SubscriptionPlanStatus.INACTIVE,
            description='description4'
        ),
        BillingPlan(
            product_id='product_id0',
            name='name4',
            status=SubscriptionPlanStatus.INACTIVE,
            description='description4'
        )
    ],
    total_items=68,
    total_pages=104
)
```

