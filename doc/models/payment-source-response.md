
# Payment Source Response

The payment source used to fund the payment.

## Structure

`PaymentSourceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardResponse`](../../doc/models/card-response.md) | Optional | The payment card to use to fund a payment. Card can be a credit or debit card. |
| `paypal` | [`PaypalWalletResponse`](../../doc/models/paypal-wallet-response.md) | Optional | The PayPal Wallet response. |
| `bancontact` | [`BancontactPaymentObject`](../../doc/models/bancontact-payment-object.md) | Optional | Information used to pay Bancontact. |
| `blik` | [`BlikPaymentObject`](../../doc/models/blik-payment-object.md) | Optional | Information used to pay using BLIK. |
| `eps` | [`EpsPaymentObject`](../../doc/models/eps-payment-object.md) | Optional | Information used to pay using eps. |
| `giropay` | [`GiropayPaymentObject`](../../doc/models/giropay-payment-object.md) | Optional | Information needed to pay using giropay. |
| `ideal` | [`IdealPaymentObject`](../../doc/models/ideal-payment-object.md) | Optional | Information used to pay using iDEAL. |
| `mybank` | [`MybankPaymentObject`](../../doc/models/mybank-payment-object.md) | Optional | Information used to pay using MyBank. |
| `p_24` | [`P24PaymentObject`](../../doc/models/p24-payment-object.md) | Optional | Information used to pay using P24(Przelewy24). |
| `sofort` | [`SofortPaymentObject`](../../doc/models/sofort-payment-object.md) | Optional | Information used to pay using Sofort. |
| `trustly` | [`TrustlyPaymentObject`](../../doc/models/trustly-payment-object.md) | Optional | Information needed to pay using Trustly. |
| `apple_pay` | [`ApplePayPaymentObject`](../../doc/models/apple-pay-payment-object.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayWalletResponse`](../../doc/models/google-pay-wallet-response.md) | Optional | Google Pay Wallet payment data. |
| `venmo` | [`VenmoWalletResponse`](../../doc/models/venmo-wallet-response.md) | Optional | Venmo wallet response. |

## Example

```python
from paypalserversdk.models.bancontact_payment_object import BancontactPaymentObject
from paypalserversdk.models.blik_one_click_payment_object import BlikOneClickPaymentObject
from paypalserversdk.models.blik_payment_object import BlikPaymentObject
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response import CardResponse
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.eps_payment_object import EpsPaymentObject
from paypalserversdk.models.name import Name
from paypalserversdk.models.payment_source_response import PaymentSourceResponse
from paypalserversdk.models.paypal_wallet_response import PaypalWalletResponse
from paypalserversdk.models.phone_type import PhoneType

payment_source_response = PaymentSourceResponse(
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
    bancontact=BancontactPaymentObject(
        name='name0',
        country_code='country_code0',
        bic='bic2',
        iban_last_chars='iban_last_chars8',
        card_last_digits='card_last_digits4'
    ),
    blik=BlikPaymentObject(
        name='name2',
        country_code='country_code2',
        email='email4',
        one_click=BlikOneClickPaymentObject(
            consumer_reference='consumer_reference2'
        )
    ),
    eps=EpsPaymentObject(
        name='name6',
        country_code='country_code6',
        bic='bic8'
    )
)
```

