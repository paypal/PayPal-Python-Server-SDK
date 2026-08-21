
# Google Pay Experience Context

Customizes the payer experience during the approval process for the payment.

## Structure

`GooglePayExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Required | Describes the URL. |
| `cancel_url` | `str` | Required | Describes the URL. |

## Example

```python
from paypalserversdk.models.google_pay_experience_context import GooglePayExperienceContext

google_pay_experience_context = GooglePayExperienceContext(
    return_url='return_url0',
    cancel_url='cancel_url2'
)
```

