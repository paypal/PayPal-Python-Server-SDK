
# Venmo Wallet Attributes Response

Additional attributes associated with the use of a Venmo Wallet.

## Structure

`VenmoWalletAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`VenmoVaultResponse`](../../doc/models/venmo-vault-response.md) | Optional | The details about a saved venmo payment source. |

## Example

```python
from paypalserversdk.models.customer_information import CustomerInformation
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.venmo_vault_response import VenmoVaultResponse
from paypalserversdk.models.venmo_vault_response_status import VenmoVaultResponseStatus
from paypalserversdk.models.venmo_wallet_attributes_response import VenmoWalletAttributesResponse

venmo_wallet_attributes_response = VenmoWalletAttributesResponse(
    vault=VenmoVaultResponse(
        id='id6',
        status=VenmoVaultResponseStatus.APPROVED,
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
        )
    )
)
```

