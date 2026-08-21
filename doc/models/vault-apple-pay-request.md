
# Vault Apple Pay Request

A resource representing a request to vault Apple Pay.

## Structure

`VaultApplePayRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `str` | Optional | Encrypted Apple Pay token, containing card information. This token would be base64 encoded.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10000`, *Pattern*: `^.*$` |
| `card` | [`ApplePayRequestCard`](../../doc/models/apple-pay-request-card.md) | Optional | The payment card to be used to fund a payment. Can be a credit or debit card. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_request_card import ApplePayRequestCard
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.vault_apple_pay_request import VaultApplePayRequest

vault_apple_pay_request = VaultApplePayRequest(
    token='token8',
    card=ApplePayRequestCard(
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
```

