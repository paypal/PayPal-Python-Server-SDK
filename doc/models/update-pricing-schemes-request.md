
# Update Pricing Schemes Request

The update pricing scheme request details.

## Structure

`UpdatePricingSchemesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_schemes` | [`List[UpdatePricingScheme]`](../../doc/models/update-pricing-scheme.md) | Required | An array of pricing schemes.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `99` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.update_pricing_scheme import UpdatePricingScheme
from paypalserversdk.models.update_pricing_schemes_request import UpdatePricingSchemesRequest

update_pricing_schemes_request = UpdatePricingSchemesRequest(
    pricing_schemes=[
        UpdatePricingScheme(
            billing_cycle_sequence=34,
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
    ]
)
```

