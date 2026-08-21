
# Plan Details

The plan details.

## Structure

`PlanDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `str` | Optional | The ID for the product.<br><br>**Constraints**: *Minimum Length*: `22`, *Maximum Length*: `22`, *Pattern*: `^PROD-[A-Z0-9]*$` |
| `name` | `str` | Optional | The plan name.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `description` | `str` | Optional | The detailed description of the plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `billing_cycles` | [`List[SubscriptionBillingCycle]`](../../doc/models/subscription-billing-cycle.md) | Optional | An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `12` |
| `payment_preferences` | [`PaymentPreferences`](../../doc/models/payment-preferences.md) | Optional | The payment preferences for a subscription. |
| `merchant_preferences` | [`MerchantPreferences`](../../doc/models/merchant-preferences.md) | Optional | The merchant preferences for a subscription. |
| `taxes` | [`Taxes`](../../doc/models/taxes.md) | Optional | The tax details. |
| `quantity_supported` | `bool` | Optional | Indicates whether you can subscribe to this plan by providing a quantity for the goods or service.<br><br>**Default**: `False` |

## Example

```python
from paypalserversdk.models.frequency import Frequency
from paypalserversdk.models.interval_unit import IntervalUnit
from paypalserversdk.models.money import Money
from paypalserversdk.models.payment_preferences import PaymentPreferences
from paypalserversdk.models.plan_details import PlanDetails
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction
from paypalserversdk.models.subscription_billing_cycle import SubscriptionBillingCycle
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.tenure_type import TenureType

plan_details = PlanDetails(
    product_id='product_id6',
    name='name0',
    description='description0',
    billing_cycles=[
        SubscriptionBillingCycle(
            frequency=Frequency(
                interval_unit=IntervalUnit.DAY,
                interval_count=94
            ),
            tenure_type=TenureType.REGULAR,
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
        ),
        SubscriptionBillingCycle(
            frequency=Frequency(
                interval_unit=IntervalUnit.DAY,
                interval_count=94
            ),
            tenure_type=TenureType.REGULAR,
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
    payment_preferences=PaymentPreferences(
        auto_bill_outstanding=False,
        setup_fee=Money(
            currency_code='currency_code8',
            value='value4'
        ),
        setup_fee_failure_action=SetupFeeFailureAction.CONTINUE,
        payment_failure_threshold=104
    ),
    quantity_supported=False
)
```

