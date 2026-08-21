
# Subscription Application Context

The application context, which customizes the payer experience during the subscription approval process with PayPal.

## Structure

`SubscriptionApplicationContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | The label that overrides the business name in the PayPal account on the PayPal site.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `locale` | `str` | Optional | The BCP 47-formatted locale of pages that the PayPal payment experience shows. PayPal supports a five-character code. For example, `da-DK`, `he-IL`, `id-ID`, `ja-JP`, `no-NO`, `pt-BR`, `ru-RU`, `sv-SE`, `th-TH`, `zh-CN`, `zh-HK`, or `zh-TW`.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `10`, *Pattern*: `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}\|[0-9]{3}))?$` |
| `shipping_preference` | [`ExperienceContextShippingPreference`](../../doc/models/experience-context-shipping-preference.md) | Optional | The location from which the shipping address is derived.<br><br>**Default**: `"GET_FROM_FILE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `user_action` | [`ApplicationContextUserAction`](../../doc/models/application-context-user-action.md) | Optional | Configures the label name to `Continue` or `Subscribe Now` for subscription consent experience.<br><br>**Default**: `"SUBSCRIBE_NOW"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `payment_method` | [`PaymentMethod`](../../doc/models/payment-method.md) | Optional | The customer and merchant payment preferences. |
| `return_url` | `str` | Required | The URL where the customer is redirected after the customer approves the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |
| `cancel_url` | `str` | Required | The URL where the customer is redirected after the customer cancels the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |

## Example

```python
from paypalserversdk.models.application_context_user_action import ApplicationContextUserAction
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.payee_payment_method_preference import PayeePaymentMethodPreference
from paypalserversdk.models.payment_method import PaymentMethod
from paypalserversdk.models.subscription_application_context import SubscriptionApplicationContext

subscription_application_context = SubscriptionApplicationContext(
    return_url='return_url4',
    cancel_url='cancel_url6',
    brand_name='brand_name2',
    locale='locale6',
    shipping_preference=ExperienceContextShippingPreference.GET_FROM_FILE,
    user_action=ApplicationContextUserAction.SUBSCRIBE_NOW,
    payment_method=PaymentMethod(
        payee_preferred=PayeePaymentMethodPreference.UNRESTRICTED
    )
)
```

