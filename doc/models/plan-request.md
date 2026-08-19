
# Plan Request

The create plan request details.

## Structure

`PlanRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `str` | Required | The ID of the product created through Catalog Products API.<br><br>**Constraints**: *Minimum Length*: `22`, *Maximum Length*: `22`, *Pattern*: `^PROD-[A-Z0-9]*$` |
| `name` | `str` | Required | The plan name.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `status` | [`PlanRequestStatus`](../../doc/models/plan-request-status.md) | Optional | The initial state of the plan. Allowed input values are CREATED and ACTIVE.<br><br>**Default**: `"ACTIVE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `description` | `str` | Optional | The detailed description of the plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `billing_cycles` | [`List[SubscriptionBillingCycle]`](../../doc/models/subscription-billing-cycle.md) | Required | An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `12` |
| `payment_preferences` | [`PaymentPreferences`](../../doc/models/payment-preferences.md) | Required | The payment preferences for a subscription. |
| `merchant_preferences` | [`MerchantPreferences`](../../doc/models/merchant-preferences.md) | Optional | The merchant preferences for a subscription. |
| `taxes` | [`Taxes`](../../doc/models/taxes.md) | Optional | The tax details. |
| `quantity_supported` | `bool` | Optional | Indicates whether you can subscribe to this plan by providing a quantity for the goods or service.<br><br>**Default**: `False` |

## Example

```python
from paypalserversdk.models.frequency import Frequency
from paypalserversdk.models.interval_unit import IntervalUnit
from paypalserversdk.models.merchant_preferences import MerchantPreferences
from paypalserversdk.models.money import Money
from paypalserversdk.models.payment_preferences import PaymentPreferences
from paypalserversdk.models.plan_request import PlanRequest
from paypalserversdk.models.plan_request_status import PlanRequestStatus
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction
from paypalserversdk.models.subscription_billing_cycle import SubscriptionBillingCycle
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.taxes import Taxes
from paypalserversdk.models.tenure_type import TenureType

plan_request = PlanRequest(
    product_id='product_id8',
    name='name2',
    billing_cycles=[
        SubscriptionBillingCycle(
            frequency=Frequency(
                interval_unit=IntervalUnit.DAY,
                interval_count=1
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
            total_cycles=1
        )
    ],
    payment_preferences=PaymentPreferences(
        auto_bill_outstanding=True,
        setup_fee=Money(
            currency_code='currency_code8',
            value='value4'
        ),
        setup_fee_failure_action=SetupFeeFailureAction.CANCEL,
        payment_failure_threshold=0
    ),
    status=PlanRequestStatus.ACTIVE,
    description='description2',
    merchant_preferences=MerchantPreferences(
        return_url='return_url4',
        cancel_url='cancel_url6'
    ),
    taxes=Taxes(
        percentage='percentage8',
        inclusive=False
    ),
    quantity_supported=False
)
```

