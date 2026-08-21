
# Apple Pay Experience Context

Customizes the payer experience during the approval process for the payment.

## Structure

`ApplePayExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Required | Describes the URL. |
| `cancel_url` | `str` | Required | Describes the URL. |

## Example

```python
from paypalserversdk.models.apple_pay_experience_context import ApplePayExperienceContext

apple_pay_experience_context = ApplePayExperienceContext(
    return_url='return_url4',
    cancel_url='cancel_url6'
)
```

