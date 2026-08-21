
# Order Authorize Response

The order authorize response.

## Structure

`OrderAuthorizeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `create_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `update_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `id` | `str` | Optional, Read-only | The ID of the order. |
| `payment_source` | [`OrderAuthorizeResponsePaymentSource`](../../doc/models/order-authorize-response-payment-source.md) | Optional | The payment source used to fund the payment. |
| `intent` | [`CheckoutPaymentIntent`](../../doc/models/checkout-payment-intent.md) | Optional | The intent to either capture payment immediately or authorize a payment for an order after order creation. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `payer` | [`Payer`](../../doc/models/payer.md) | Optional | The customer who approves and pays for the order. The customer is also known as the payer. |
| `purchase_units` | [`List[PurchaseUnit]`](../../doc/models/purchase-unit.md) | Optional | An array of purchase units. Each purchase unit establishes a contract between a customer and merchant. Each purchase unit represents either a full or partial order that the customer intends to purchase from the merchant.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `status` | [`OrderStatus`](../../doc/models/order-status.md) | Optional | The order status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links. To complete payer approval, use the `approve` link to redirect the payer. The API caller has 6 hours (default setting, this which can be changed by your account manager to 24/48/72 hours to accommodate your use case) from the time the order is created, to redirect your payer. Once redirected, the API caller has 6 hours for the payer to approve the order and either authorize or capture the order. If you are not using the PayPal JavaScript SDK to initiate PayPal Checkout (in context) ensure that you include `application_context.return_url` is specified or you will get "We're sorry, Things don't appear to be working at the moment" after the payer approves the payment. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_payment_object import ApplePayPaymentObject
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response import CardResponse
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.google_pay_card_response import GooglePayCardResponse
from paypalserversdk.models.google_pay_wallet_response import GooglePayWalletResponse
from paypalserversdk.models.name import Name
from paypalserversdk.models.order_authorize_response import OrderAuthorizeResponse
from paypalserversdk.models.order_authorize_response_payment_source import OrderAuthorizeResponsePaymentSource
from paypalserversdk.models.paypal_wallet_response import PaypalWalletResponse
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.venmo_wallet_response import VenmoWalletResponse

order_authorize_response = OrderAuthorizeResponse(
    create_time='create_time6',
    update_time='update_time2',
    payment_source=OrderAuthorizeResponsePaymentSource(
        card=CardResponse(
            name='name6',
            brand=CardBrand.CB_NATIONALE,
            mtype=CardType.UNKNOWN
        ),
        paypal=PaypalWalletResponse(
            email_address='email_address0',
            account_id='account_id4',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            ),
            phone_type=PhoneType.FAX
        ),
        apple_pay=ApplePayPaymentObject(
            id='id0',
            token='token6',
            name='name0',
            email_address='email_address8',
            phone_number=PhoneNumber(
                national_number='national_number6'
            )
        ),
        google_pay=GooglePayWalletResponse(
            name='name8',
            email_address='email_address6',
            phone_number=PhoneNumberWithCountryCode(
                country_code='country_code2',
                national_number='national_number6'
            ),
            card=GooglePayCardResponse(
                name='name6',
                mtype=CardType.UNKNOWN,
                brand=CardBrand.CB_NATIONALE,
                billing_address=Address(
                    country_code='country_code8',
                    address_line_1='address_line_12',
                    address_line_2='address_line_28',
                    admin_area_2='admin_area_28',
                    admin_area_1='admin_area_14',
                    postal_code='postal_code0'
                )
            )
        ),
        venmo=VenmoWalletResponse(
            email_address='email_address4',
            account_id='account_id8',
            user_name='user_name2',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            ),
            phone_number=PhoneNumber(
                national_number='national_number6'
            )
        )
    ),
    intent=CheckoutPaymentIntent.CAPTURE
)
```

