
# Payment Token Request Payment Source

The payment method to vault with the instrument details.

## Structure

`PaymentTokenRequestPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`PaymentTokenRequestCard`](../../doc/models/payment-token-request-card.md) | Optional | A Resource representing a request to vault a Card. |
| `token` | [`VaultTokenRequest`](../../doc/models/vault-token-request.md) | Optional | The Tokenized Payment Source representing a Request to Vault a Token. |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.payment_token_request_card import PaymentTokenRequestCard
from paypalserversdk.models.payment_token_request_payment_source import PaymentTokenRequestPaymentSource
from paypalserversdk.models.vault_token_request import VaultTokenRequest
from paypalserversdk.models.vault_token_request_type import VaultTokenRequestType

payment_token_request_payment_source = PaymentTokenRequestPaymentSource(
    card=PaymentTokenRequestCard(
        name='name6',
        number='number6',
        expiry='expiry4',
        security_code='security_code8',
        brand=CardBrand.CB_NATIONALE
    ),
    token=VaultTokenRequest(
        id='id6',
        mtype=VaultTokenRequestType.SETUP_TOKEN
    )
)
```

