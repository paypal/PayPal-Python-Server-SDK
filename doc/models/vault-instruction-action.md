
# Vault Instruction Action

Vault Instruction on action to be performed after a successful payer approval.

## Enumeration

`VaultInstructionAction`

## Fields

| Name | Description |
|  --- | --- |
| `ON_CREATE_PAYMENT_TOKENS` | Vault the payment method after API caller performs a successful POST on Payment Tokens. |
| `ON_PAYER_APPROVAL` | Vault the payment method on successful payer authentication and approval. |

## Example

```python
from paypalserversdk.models.vault_instruction_action import VaultInstructionAction

vault_instruction_action = VaultInstructionAction.ON_CREATE_PAYMENT_TOKENS
```

