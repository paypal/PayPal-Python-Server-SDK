
# Payment Token Response Payment Source

The vaulted payment method details.

## Structure

`PaymentTokenResponsePaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardPaymentTokenEntity`](../../doc/models/card-payment-token-entity.md) | Optional | Full representation of a Card Payment Token including network token. |
| `paypal` | [`PaypalPaymentToken`](../../doc/models/paypal-payment-token.md) | Optional, Read-only | Full representation of a PayPal Payment Token. |
| `venmo` | [`VenmoPaymentToken`](../../doc/models/venmo-payment-token.md) | Optional, Read-only | Full representation of a Venmo Payment Token. |
| `apple_pay` | [`ApplePayPaymentToken`](../../doc/models/apple-pay-payment-token.md) | Optional | A resource representing a response for Apple Pay. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_card import ApplePayCard
from paypalserversdk.models.apple_pay_payment_token import ApplePayPaymentToken
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_payment_token_entity import CardPaymentTokenEntity
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.payment_token_response_payment_source import PaymentTokenResponsePaymentSource

payment_token_response_payment_source = PaymentTokenResponsePaymentSource(
    card=CardPaymentTokenEntity(
        name='name6',
        brand=CardBrand.CB_NATIONALE,
        expiry='expiry4',
        billing_address=CardResponseAddress(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0'
        )
    ),
    apple_pay=ApplePayPaymentToken(
        card=ApplePayCard(
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
    )
)
```

