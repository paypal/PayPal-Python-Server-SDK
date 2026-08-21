
# Vault Instruction Base

Basic vault instruction specification that can be extended by specific payment sources that supports vaulting.

## Structure

`VaultInstructionBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_in_vault` | [`StoreInVaultInstruction`](../../doc/models/store-in-vault-instruction.md) | Optional | Defines how and when the payment source gets vaulted.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |

## Example

```python
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction
from paypalserversdk.models.vault_instruction_base import VaultInstructionBase

vault_instruction_base = VaultInstructionBase(
    store_in_vault=StoreInVaultInstruction.ON_SUCCESS
)
```

