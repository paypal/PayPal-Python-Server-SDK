
# Paypal Wallet Attributes Response

Additional attributes associated with the use of a PayPal Wallet.

## Structure

`PaypalWalletAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`PaypalWalletVaultResponse`](../../doc/models/paypal-wallet-vault-response.md) | Optional | The details about a saved PayPal Wallet payment source. |
| `cobranded_cards` | [`List[CobrandedCard]`](../../doc/models/cobranded-card.md) | Optional | An array of merchant cobranded cards used by buyer to complete an order. This array will be present if a merchant has onboarded their cobranded card with PayPal and provided corresponding label(s).<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `25` |

## Example

```python
from paypalserversdk.models.cobranded_card import CobrandedCard
from paypalserversdk.models.money import Money
from paypalserversdk.models.name import Name
from paypalserversdk.models.payee_base import PayeeBase
from paypalserversdk.models.paypal_wallet_attributes_response import PaypalWalletAttributesResponse
from paypalserversdk.models.paypal_wallet_customer import PaypalWalletCustomer
from paypalserversdk.models.paypal_wallet_vault_response import PaypalWalletVaultResponse
from paypalserversdk.models.paypal_wallet_vault_status import PaypalWalletVaultStatus
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType

paypal_wallet_attributes_response = PaypalWalletAttributesResponse(
    vault=PaypalWalletVaultResponse(
        id='id6',
        status=PaypalWalletVaultStatus.APPROVED,
        customer=PaypalWalletCustomer(
            id='id0',
            email_address='email_address2',
            phone=PhoneWithType(
                phone_number=PhoneNumber(
                    national_number='national_number6'
                ),
                phone_type=PhoneType.OTHER
            ),
            name=Name(
                given_name='given_name2',
                surname='surname8'
            ),
            merchant_customer_id='merchant_customer_id2'
        )
    ),
    cobranded_cards=[
        CobrandedCard(
            labels=[
                'labels4',
                'labels3'
            ],
            payee=PayeeBase(
                email_address='email_address4',
                merchant_id='merchant_id6'
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        ),
        CobrandedCard(
            labels=[
                'labels4',
                'labels3'
            ],
            payee=PayeeBase(
                email_address='email_address4',
                merchant_id='merchant_id6'
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        )
    ]
)
```

