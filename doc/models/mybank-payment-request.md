
# Mybank Payment Request

Information needed to pay using MyBank.

## Structure

`MybankPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The full name representation like Mr J Smith.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `300` |
| `country_code` | `str` | Required | The [two-character ISO 3166-1 code](https://developer.paypal.com/api/rest/reference/country-codes/) that identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level domain names for that country. Use the `C2` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2`, *Pattern*: `^([A-Z]{2}\|C2)$` |
| `experience_context` | [`ExperienceContext`](../../doc/models/experience-context.md) | Optional | Customizes the payer experience during the approval process for the payment. |

## Example

```python
from paypalserversdk.models.experience_context import ExperienceContext
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.mybank_payment_request import MybankPaymentRequest

mybank_payment_request = MybankPaymentRequest(
    name='name2',
    country_code='country_code2',
    experience_context=ExperienceContext(
        brand_name='brand_name2',
        locale='locale6',
        shipping_preference=ExperienceContextShippingPreference.NO_SHIPPING,
        return_url='return_url4',
        cancel_url='cancel_url6'
    )
)
```

