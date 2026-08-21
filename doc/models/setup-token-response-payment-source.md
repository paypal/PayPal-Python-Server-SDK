
# Setup Token Response Payment Source

The setup payment method details.

## Structure

`SetupTokenResponsePaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`SetupTokenResponseCard`](../../doc/models/setup-token-response-card.md) | Optional | - |
| `paypal` | [`PaypalPaymentToken`](../../doc/models/paypal-payment-token.md) | Optional, Read-only | Full representation of a PayPal Payment Token. |
| `venmo` | [`VenmoPaymentToken`](../../doc/models/venmo-payment-token.md) | Optional, Read-only | Full representation of a Venmo Payment Token. |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.setup_token_response_card import SetupTokenResponseCard
from paypalserversdk.models.setup_token_response_payment_source import SetupTokenResponsePaymentSource

setup_token_response_payment_source = SetupTokenResponsePaymentSource(
    card=SetupTokenResponseCard(
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
    )
)
```

