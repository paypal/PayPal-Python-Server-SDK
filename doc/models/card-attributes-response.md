
# Card Attributes Response

Additional attributes associated with the use of this card.

## Structure

`CardAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`CardVaultResponse`](../../doc/models/card-vault-response.md) | Optional | The details about a saved Card payment source. |

## Example

```python
from paypalserversdk.models.card_attributes_response import CardAttributesResponse
from paypalserversdk.models.card_customer_information import CardCustomerInformation
from paypalserversdk.models.card_vault_response import CardVaultResponse
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.vault_status import VaultStatus

card_attributes_response = CardAttributesResponse(
    vault=CardVaultResponse(
        id='id6',
        status=VaultStatus.APPROVED,
        customer=CardCustomerInformation(
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
    )
)
```

