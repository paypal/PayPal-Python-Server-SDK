
# Store in Vault Instruction

Defines how and when the payment source gets vaulted.

## Enumeration

`StoreInVaultInstruction`

## Fields

| Name | Description |
|  --- | --- |
| `ON_SUCCESS` | Defines that the payment_source will be vaulted only when at least one authorization or capture using that payment_source is successful. |

## Example

```python
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction

store_in_vault_instruction = StoreInVaultInstruction.ON_SUCCESS
```

