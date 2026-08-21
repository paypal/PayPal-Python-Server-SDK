
# Card Experience Context

Customizes the payer experience during the 3DS Approval for payment.

## Structure

`CardExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Optional | Describes the URL. |
| `cancel_url` | `str` | Optional | Describes the URL. |

## Example

```python
from paypalserversdk.models.card_experience_context import CardExperienceContext

card_experience_context = CardExperienceContext(
    return_url='return_url2',
    cancel_url='cancel_url4'
)
```

