
# Payment Token Request

Payment Token Request where the `source` defines the type of instrument to be stored.

## Structure

`PaymentTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_source` | [`PaymentTokenRequestPaymentSource`](../../doc/models/payment-token-request-payment-source.md) | Required | The payment method to vault with the instrument details. |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.customer import Customer
from paypalserversdk.models.payment_token_request import PaymentTokenRequest
from paypalserversdk.models.payment_token_request_card import PaymentTokenRequestCard
from paypalserversdk.models.payment_token_request_payment_source import PaymentTokenRequestPaymentSource
from paypalserversdk.models.vault_token_request import VaultTokenRequest
from paypalserversdk.models.vault_token_request_type import VaultTokenRequestType

payment_token_request = PaymentTokenRequest(
    payment_source=PaymentTokenRequestPaymentSource(
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
    ),
    customer=Customer(
        id='id0',
        merchant_customer_id='merchant_customer_id2'
    )
)
```

