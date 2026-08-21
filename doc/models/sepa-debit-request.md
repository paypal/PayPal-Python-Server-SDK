
# Sepa Debit Request

An API resource denoting a request to securely store a SEPA Debit.

## Structure

`SepaDebitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `experience_context` | [`SepaDebitExperienceContext`](../../doc/models/sepa-debit-experience-context.md) | Optional | Customizes the payer experience during the approval process for the SEPA Debit payment. |

## Example

```python
from paypalserversdk.models.sepa_debit_experience_context import SepaDebitExperienceContext
from paypalserversdk.models.sepa_debit_request import SepaDebitRequest

sepa_debit_request = SepaDebitRequest(
    experience_context=SepaDebitExperienceContext(
        return_url='return_url4',
        cancel_url='cancel_url6',
        locale='locale6'
    )
)
```

