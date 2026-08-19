
# Vault Response

The details about a saved payment source.

## Structure

`VaultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the saved payment source.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `status` | [`VaultStatus`](../../doc/models/vault-status.md) | Optional | The vault status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `customer` | [`VaultCustomer`](../../doc/models/vault-customer.md) | Optional | This object represents a merchant’s customer, allowing them to store contact details, and track all payments associated with the same customer. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |

## Example

```python
from paypalserversdk.models.name import Name
from paypalserversdk.models.vault_customer import VaultCustomer
from paypalserversdk.models.vault_response import VaultResponse
from paypalserversdk.models.vault_status import VaultStatus

vault_response = VaultResponse(
    id='id8',
    status=VaultStatus.VAULTED,
    customer=VaultCustomer(
        id='id0',
        name=Name(
            given_name='given_name2',
            surname='surname8'
        )
    )
)
```

