
# Assurance Details

Information about cardholder possession validation and cardholder identification and verifications (ID&V).

## Structure

`AssuranceDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_verified` | `bool` | Optional | If true, indicates that Cardholder possession validation has been performed on returned payment credential.<br><br>**Default**: `False` |
| `card_holder_authenticated` | `bool` | Optional | If true, indicates that identification and verifications (ID&V) was performed on the returned payment credential.If false, the same risk-based authentication can be performed as you would for card transactions. This risk-based authentication can include, but not limited to, step-up with 3D Secure protocol if applicable.<br><br>**Default**: `False` |

## Example

```python
from paypalserversdk.models.assurance_details import AssuranceDetails

assurance_details = AssuranceDetails(
    account_verified=False,
    card_holder_authenticated=False
)
```

