
# Apple Pay Attributes

Additional attributes associated with apple pay.

## Structure

`ApplePayAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`CustomerInformation`](../../doc/models/customer-information.md) | Optional | This object represents a merchant’s customer, allowing them to store contact details, and track all payments associated with the same customer. |
| `vault` | [`VaultInstruction`](../../doc/models/vault-instruction.md) | Optional | Base vaulting specification. The object can be extended for specific use cases within each payment_source that supports vaulting. |

## Example

```python
from paypalserversdk.models.apple_pay_attributes import ApplePayAttributes
from paypalserversdk.models.customer_information import CustomerInformation
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction
from paypalserversdk.models.vault_instruction import VaultInstruction

apple_pay_attributes = ApplePayAttributes(
    customer=CustomerInformation(
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
        )
    ),
    vault=VaultInstruction(
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS
    )
)
```

