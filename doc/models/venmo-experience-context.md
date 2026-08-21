
# Venmo Experience Context

A resource representing an experience context of vault a venmo account.

## Structure

`VenmoExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `shipping_preference` | [`ExperienceContextShippingPreference`](../../doc/models/experience-context-shipping-preference.md) | Optional | The shipping preference. This only applies to PayPal payment source.<br><br>**Default**: `"GET_FROM_FILE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `vault_instruction` | [`VaultInstructionAction`](../../doc/models/vault-instruction-action.md) | Optional | DEPRECATED. Vault Instruction on action to be performed after a successful payer approval.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[A-Z_]+$` |
| `user_action` | [`VaultUserAction`](../../doc/models/vault-user-action.md) | Optional | User Action on action to be performed after a successful payer approval.<br><br>**Default**: `"CONTINUE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[A-Z_]+$` |

## Example

```python
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.vault_instruction_action import VaultInstructionAction
from paypalserversdk.models.vault_user_action import VaultUserAction
from paypalserversdk.models.venmo_experience_context import VenmoExperienceContext

venmo_experience_context = VenmoExperienceContext(
    brand_name='brand_name0',
    shipping_preference=ExperienceContextShippingPreference.GET_FROM_FILE,
    vault_instruction=VaultInstructionAction.ON_CREATE_PAYMENT_TOKENS,
    user_action=VaultUserAction.CONTINUE
)
```

