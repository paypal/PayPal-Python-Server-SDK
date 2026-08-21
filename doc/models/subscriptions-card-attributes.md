
# Subscriptions Card Attributes

Additional attributes associated with the use of this card.

## Structure

`SubscriptionsCardAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`CardCustomer`](../../doc/models/card-customer.md) | Optional | The details about a customer in PayPal's system of record. |
| `vault` | [`VaultInstructionBase`](../../doc/models/vault-instruction-base.md) | Optional | Basic vault instruction specification that can be extended by specific payment sources that supports vaulting. |
| `verification` | [`CardVerification`](../../doc/models/card-verification.md) | Optional | The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar Auth, 3DS). |

## Example

```python
from paypalserversdk.models.card_customer import CardCustomer
from paypalserversdk.models.card_verification import CardVerification
from paypalserversdk.models.orders_card_verification_method import OrdersCardVerificationMethod
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction
from paypalserversdk.models.subscriptions_card_attributes import SubscriptionsCardAttributes
from paypalserversdk.models.vault_instruction_base import VaultInstructionBase

subscriptions_card_attributes = SubscriptionsCardAttributes(
    customer=CardCustomer(
        id='id0',
        email_address='email_address2',
        phone=PhoneWithType(
            phone_number=PhoneNumber(
                national_number='national_number6'
            ),
            phone_type=PhoneType.OTHER
        ),
        merchant_customer_id='merchant_customer_id2'
    ),
    vault=VaultInstructionBase(
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS
    ),
    verification=CardVerification(
        method=OrdersCardVerificationMethod.ENUM_3D_SECURE
    )
)
```

