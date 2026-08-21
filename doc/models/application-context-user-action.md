
# Application Context User Action

Configures the label name to `Continue` or `Subscribe Now` for subscription consent experience.

## Enumeration

`ApplicationContextUserAction`

## Fields

| Name | Description |
|  --- | --- |
| `CONTINUE` | After you redirect the customer to the PayPal subscription consent page, a Continue button appears. Use this option when you want to control the activation of the subscription and do not want PayPal to activate the subscription. |
| `SUBSCRIBE_NOW` | After you redirect the customer to the PayPal subscription consent page, a Subscribe Now button appears. Use this option when you want PayPal to activate the subscription. |

## Example

```python
from paypalserversdk.models.application_context_user_action import ApplicationContextUserAction

application_context_user_action = ApplicationContextUserAction.CONTINUE
```

