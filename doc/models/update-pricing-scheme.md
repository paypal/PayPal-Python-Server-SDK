
# Update Pricing Scheme

The update pricing scheme request details.

## Structure

`UpdatePricingScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_cycle_sequence` | `int` | Required | The billing cycle sequence.<br><br>**Constraints**: `>= 1`, `<= 99` |
| `pricing_scheme` | [`SubscriptionPricingScheme`](../../doc/models/subscription-pricing-scheme.md) | Required | The pricing scheme details. |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.update_pricing_scheme import UpdatePricingScheme

update_pricing_scheme = UpdatePricingScheme(
    billing_cycle_sequence=99,
    pricing_scheme=SubscriptionPricingScheme(
        fixed_price=Money(
            currency_code='currency_code4',
            value='value0'
        ),
        pricing_model=SubscriptionPricingModel.VOLUME,
        tiers=[
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                ending_quantity='ending_quantity6'
            ),
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                ending_quantity='ending_quantity6'
            ),
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                ending_quantity='ending_quantity6'
            )
        ],
        create_time='create_time4'
    )
)
```

