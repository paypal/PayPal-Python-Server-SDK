
# Order Authorize Response Payment Source

The payment source used to fund the payment.

## Structure

`OrderAuthorizeResponsePaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardResponse`](../../doc/models/card-response.md) | Optional | The payment card to use to fund a payment. Card can be a credit or debit card. |
| `paypal` | [`PaypalWalletResponse`](../../doc/models/paypal-wallet-response.md) | Optional | The PayPal Wallet response. |
| `apple_pay` | [`ApplePayPaymentObject`](../../doc/models/apple-pay-payment-object.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayWalletResponse`](../../doc/models/google-pay-wallet-response.md) | Optional | Google Pay Wallet payment data. |
| `venmo` | [`VenmoWalletResponse`](../../doc/models/venmo-wallet-response.md) | Optional | Venmo wallet response. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_payment_object import ApplePayPaymentObject
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response import CardResponse
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.google_pay_card_response import GooglePayCardResponse
from paypalserversdk.models.google_pay_wallet_response import GooglePayWalletResponse
from paypalserversdk.models.name import Name
from paypalserversdk.models.order_authorize_response_payment_source import OrderAuthorizeResponsePaymentSource
from paypalserversdk.models.paypal_wallet_response import PaypalWalletResponse
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.venmo_wallet_response import VenmoWalletResponse

order_authorize_response_payment_source = OrderAuthorizeResponsePaymentSource(
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
)
```

