
# Vault Token Request Type

The tokenization method that generated the ID.

## Enumeration

`VaultTokenRequestType`

## Fields

| Name | Description |
|  --- | --- |
| `SETUP_TOKEN` | The setup token, which is a temporary reference to payment source. |

## Example

```python
from paypalserversdk.models.vault_token_request_type import VaultTokenRequestType

vault_token_request_type = VaultTokenRequestType.SETUP_TOKEN
```

