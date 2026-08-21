
# Plan Override

An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object.

## Structure

`PlanOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_cycles` | [`List[BillingCycleOverride]`](../../doc/models/billing-cycle-override.md) | Optional | An array of billing cycles for trial billing and regular billing. The subscription billing cycle definition has to adhere to the plan billing cycle definition.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `12` |
| `payment_preferences` | [`PaymentPreferencesOverride`](../../doc/models/payment-preferences-override.md) | Optional | The payment preferences to override at subscription level. |
| `taxes` | [`TaxesOverride`](../../doc/models/taxes-override.md) | Optional | The tax details. |

## Example

```python
from paypalserversdk.models.billing_cycle_override import BillingCycleOverride
from paypalserversdk.models.money import Money
from paypalserversdk.models.payment_preferences_override import PaymentPreferencesOverride
from paypalserversdk.models.plan_override import PlanOverride
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.taxes_override import TaxesOverride

plan_override = PlanOverride(
    billing_cycles=[
        BillingCycleOverride(
            sequence=8,
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
            ),
            total_cycles=198
        )
    ],
    payment_preferences=PaymentPreferencesOverride(
        auto_bill_outstanding=False,
        setup_fee=Money(
            currency_code='currency_code8',
            value='value4'
        ),
        setup_fee_failure_action=SetupFeeFailureAction.CONTINUE,
        payment_failure_threshold=104
    ),
    taxes=TaxesOverride(
        percentage='percentage8',
        inclusive=False
    )
)
```

