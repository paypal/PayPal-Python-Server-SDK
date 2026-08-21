
# Modify Subscription Request

The request to update the quantity of the product or service in a subscription. You can also use this method to switch the plan and update the `shipping_amount` and `shipping_address` values for the subscription. This type of update requires the buyer's consent.

## Structure

`ModifySubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Optional | The unique PayPal-generated ID for the plan.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26`, *Pattern*: `^P-[A-Z0-9]*$` |
| `quantity` | `str` | Optional | The quantity of the product or service in the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^([0-9]+\|([0-9]+)?[.][0-9]+)$` |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_address` | [`ShippingDetails`](../../doc/models/shipping-details.md) | Optional | The shipping details. |
| `application_context` | [`SubscriptionPatchApplicationContext`](../../doc/models/subscription-patch-application-context.md) | Optional | The application context, which customizes the payer experience during the subscription approval process with PayPal. |
| `plan` | [`PlanOverride`](../../doc/models/plan-override.md) | Optional | An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object. |

## Example

```python
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.modify_subscription_request import ModifySubscriptionRequest
from paypalserversdk.models.money import Money
from paypalserversdk.models.payee_payment_method_preference import PayeePaymentMethodPreference
from paypalserversdk.models.payment_method import PaymentMethod
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.shipping_option import ShippingOption
from paypalserversdk.models.shipping_type import ShippingType
from paypalserversdk.models.subscription_patch_application_context import SubscriptionPatchApplicationContext

modify_subscription_request = ModifySubscriptionRequest(
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
    application_context=SubscriptionPatchApplicationContext(
        return_url='return_url0',
        cancel_url='cancel_url2',
        brand_name='brand_name8',
        locale='locale2',
        shipping_preference=ExperienceContextShippingPreference.SET_PROVIDED_ADDRESS,
        payment_method=PaymentMethod(
            payee_preferred=PayeePaymentMethodPreference.UNRESTRICTED
        )
    )
)
```

