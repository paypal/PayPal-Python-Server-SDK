
# Order Capture Request Payment Source

The payment source definition.

## Structure

`OrderCaptureRequestPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardRequest`](../../doc/models/card-request.md) | Optional | The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*. |
| `token` | [`Token`](../../doc/models/token.md) | Optional | The tokenized payment source to fund a payment. |
| `paypal` | [`PaypalWallet`](../../doc/models/paypal-wallet.md) | Optional | A resource that identifies a PayPal Wallet is used for payment. |
| `apple_pay` | [`ApplePayRequest`](../../doc/models/apple-pay-request.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayRequest`](../../doc/models/google-pay-request.md) | Optional | Information needed to pay using Google Pay. |
| `venmo` | [`VenmoWalletRequest`](../../doc/models/venmo-wallet-request.md) | Optional | Information needed to pay using Venmo. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_decrypted_token_data import ApplePayDecryptedTokenData
from paypalserversdk.models.apple_pay_payment_data import ApplePayPaymentData
from paypalserversdk.models.apple_pay_payment_data_type import ApplePayPaymentDataType
from paypalserversdk.models.apple_pay_request import ApplePayRequest
from paypalserversdk.models.apple_pay_tokenized_card import ApplePayTokenizedCard
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.google_pay_authentication_method import GooglePayAuthenticationMethod
from paypalserversdk.models.google_pay_card import GooglePayCard
from paypalserversdk.models.google_pay_decrypted_token_data import GooglePayDecryptedTokenData
from paypalserversdk.models.google_pay_payment_method import GooglePayPaymentMethod
from paypalserversdk.models.google_pay_request import GooglePayRequest
from paypalserversdk.models.google_pay_request_card import GooglePayRequestCard
from paypalserversdk.models.money import Money
from paypalserversdk.models.name import Name
from paypalserversdk.models.order_capture_request_payment_source import OrderCaptureRequestPaymentSource
from paypalserversdk.models.paypal_wallet import PaypalWallet
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.token import Token
from paypalserversdk.models.token_type import TokenType

order_capture_request_payment_source = OrderCaptureRequestPaymentSource(
    card=CardRequest(
        name='name6',
        number='number6',
        expiry='expiry4',
        security_code='security_code8',
        billing_address=Address(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0'
        )
    ),
    token=Token(
        id='id6',
        mtype=TokenType.BILLING_AGREEMENT
    ),
    paypal=PaypalWallet(
        vault_id='vault_id0',
        email_address='email_address0',
        name=Name(
            given_name='given_name2',
            surname='surname8'
        ),
        phone=PhoneWithType(
            phone_number=PhoneNumber(
                national_number='national_number6'
            ),
            phone_type=PhoneType.OTHER
        ),
        birth_date='birth_date8'
    ),
    apple_pay=ApplePayRequest(
        id='id0',
        name='name0',
        email_address='email_address8',
        phone_number=PhoneNumber(
            national_number='national_number6'
        ),
        decrypted_token=ApplePayDecryptedTokenData(
            tokenized_card=ApplePayTokenizedCard(
                name='name4',
                number='number2',
                expiry='expiry2',
                mtype=CardType.UNKNOWN
            ),
            transaction_amount=Money(
                currency_code='currency_code6',
                value='value2'
            ),
            device_manufacturer_id='device_manufacturer_id6',
            payment_data_type=ApplePayPaymentDataType.ENUM_3DSECURE,
            payment_data=ApplePayPaymentData(
                cryptogram='cryptogram6',
                eci_indicator='eci_indicator0',
                emv_data='emv_data0',
                pin='pin4'
            )
        )
    ),
    google_pay=GooglePayRequest(
        name='name8',
        email_address='email_address6',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6'
        ),
        card=GooglePayRequestCard(
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
        ),
        decrypted_token=GooglePayDecryptedTokenData(
            payment_method=GooglePayPaymentMethod.CARD,
            card=GooglePayCard(
                name='name6',
                number='number6',
                expiry='expiry4',
                mtype=CardType.UNKNOWN
            ),
            authentication_method=GooglePayAuthenticationMethod.PAN_ONLY,
            message_id='message_id0',
            message_expiration='message_expiration2',
            cryptogram='cryptogram6',
            eci_indicator='eci_indicator0'
        )
    )
)
```

