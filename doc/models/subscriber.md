
# Subscriber

The subscriber response information.

## Structure

`Subscriber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email_address` | `str` | Optional | The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted @ sign exists.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `254`, *Pattern*: ``(?:[a-zA-Z0-9!#$%&'*+/=?^_`{\|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{\|}~-]+)*\|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]\|\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\|\[(?:(?:(2(5[0-5]\|[0-4][0-9])\|1[0-9][0-9]\|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]\|[0-4][0-9])\|1[0-9][0-9]\|[1-9]?[0-9])\|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]\|\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])`` |
| `payer_id` | `str` | Optional | The account identifier for a PayPal account.<br><br>**Constraints**: *Minimum Length*: `13`, *Maximum Length*: `13`, *Pattern*: `^[2-9A-HJ-NP-Z]{13}$` |
| `name` | [`Name`](../../doc/models/name.md) | Optional | The name of the party. |
| `shipping_address` | [`ShippingDetails`](../../doc/models/shipping-details.md) | Optional | The shipping details. |
| `payment_source` | [`SubscriptionPaymentSourceResponse`](../../doc/models/subscription-payment-source-response.md) | Optional | The payment source used to fund the payment. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_response_with_billing_address import CardResponseWithBillingAddress
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.money import Money
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.shipping_option import ShippingOption
from paypalserversdk.models.shipping_type import ShippingType
from paypalserversdk.models.subscriber import Subscriber
from paypalserversdk.models.subscription_payment_source_response import SubscriptionPaymentSourceResponse

subscriber = Subscriber(
    email_address='email_address8',
    payer_id='payer_id8',
    name=Name(
        given_name='given_name2',
        surname='surname8'
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
    payment_source=SubscriptionPaymentSourceResponse(
        card=CardResponseWithBillingAddress(
            name='name6',
            billing_address=Address(
                country_code='country_code8',
                address_line_1='address_line_12',
                address_line_2='address_line_28',
                admin_area_2='admin_area_28',
                admin_area_1='admin_area_14',
                postal_code='postal_code0'
            ),
            expiry='expiry4',
            currency_code='currency_code2'
        )
    )
)
```

