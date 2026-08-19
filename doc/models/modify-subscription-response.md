
# Modify Subscription Response

The response to a request to update the quantity of the product or service in a subscription. You can also use this method to switch the plan and update the `shipping_amount` and `shipping_address` values for the subscription. This type of update requires the buyer's consent.

## Structure

`ModifySubscriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Optional | The unique PayPal-generated ID for the plan.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26`, *Pattern*: `^P-[A-Z0-9]*$` |
| `quantity` | `str` | Optional | The quantity of the product or service in the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^([0-9]+\|([0-9]+)?[.][0-9]+)$` |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_address` | [`ShippingDetails`](../../doc/models/shipping-details.md) | Optional | The shipping details. |
| `plan` | [`PlanOverride`](../../doc/models/plan-override.md) | Optional | An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object. |
| `plan_overridden` | `bool` | Optional, Read-only | Indicates whether the subscription has overridden any plan attributes. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links). |

## Example

```python
from paypalserversdk.models.billing_cycle_override import BillingCycleOverride
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.modify_subscription_response import ModifySubscriptionResponse
from paypalserversdk.models.money import Money
from paypalserversdk.models.payment_preferences_override import PaymentPreferencesOverride
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.plan_override import PlanOverride
from paypalserversdk.models.pricing_tier import PricingTier
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.shipping_option import ShippingOption
from paypalserversdk.models.shipping_type import ShippingType
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.taxes_override import TaxesOverride

modify_subscription_response = ModifySubscriptionResponse(
    plan_id='plan_id8',
    quantity='quantity2',
    shipping_amount=Money(
        currency_code='currency_code0',
        value='value6'
    ),
    shipping_address=ShippingDetails(
        name=ShippingName(
            full_name='full_name6'
        ),
        email_address='email_address8',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6'
        ),
        mtype=FulfillmentType.PICKUP_IN_STORE,
        options=[
            ShippingOption(
                id='id2',
                label='label2',
                selected=False,
                mtype=ShippingType.SHIPPING,
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                )
            )
        ]
    ),
    plan=PlanOverride(
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
            ),
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
)
```

