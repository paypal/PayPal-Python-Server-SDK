
# Apple Pay Attributes Response

Additional attributes associated with the use of Apple Pay.

## Structure

`ApplePayAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`VaultResponse`](../../doc/models/vault-response.md) | Optional | The details about a saved payment source. |

## Example

```python
from paypalserversdk.models.apple_pay_attributes_response import ApplePayAttributesResponse
from paypalserversdk.models.name import Name
from paypalserversdk.models.vault_customer import VaultCustomer
from paypalserversdk.models.vault_response import VaultResponse
from paypalserversdk.models.vault_status import VaultStatus

apple_pay_attributes_response = ApplePayAttributesResponse(
    vault=VaultResponse(
        id='id6',
        status=VaultStatus.APPROVED,
        customer=VaultCustomer(
            id='id0',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            )
        )
    )
)
```

