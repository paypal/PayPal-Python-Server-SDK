
# Order Billing Plan

Metadata for merchant-managed recurring billing plans. Valid only during the saved payment method token or billing agreement creation.

## Structure

`OrderBillingPlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_cycles` | [`List[BillingCycle]`](../../doc/models/billing-cycle.md) | Required | An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `setup_fee` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `name` | `str` | Optional | Name of the recurring plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^[A-Za-z0-9() +',.:-]+$` |

## Example

```python
from paypalserversdk.models.billing_cycle import BillingCycle
from paypalserversdk.models.cycle_frequency import CycleFrequency
from paypalserversdk.models.frequency_interval_unit import FrequencyIntervalUnit
from paypalserversdk.models.money import Money
from paypalserversdk.models.order_billing_plan import OrderBillingPlan
from paypalserversdk.models.pricing_model import PricingModel
from paypalserversdk.models.pricing_scheme import PricingScheme
from paypalserversdk.models.tenure_type import TenureType

order_billing_plan = OrderBillingPlan(
    billing_cycles=[
        BillingCycle(
            tenure_type=TenureType.REGULAR,
            pricing_scheme=PricingScheme(
                pricing_model=PricingModel.AUTO_RELOAD,
                price=Money(
                    currency_code='currency_code8',
                    value='value4'
                ),
                reload_threshold_amount=Money(
                    currency_code='currency_code0',
                    value='value6'
                )
            ),
            total_cycles=1,
            sequence=1,
            start_date='start_date6',
            frequency=CycleFrequency(
                interval_unit=FrequencyIntervalUnit.LIFETIME,
                interval_count=94
            )
        )
    ],
    setup_fee=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    name='name4'
)
```

