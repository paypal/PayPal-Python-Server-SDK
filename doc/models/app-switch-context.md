
# App Switch Context

Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal consumer app.

## Structure

`AppSwitchContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `native_app` | [`NativeAppContext`](../../doc/models/native-app-context.md) | Optional | Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app. |
| `mobile_web` | [`MobileWebContext`](../../doc/models/mobile-web-context.md) | Optional | Buyer's mobile web browser context to app switch to the PayPal consumer app. |

## Example

```python
from paypalserversdk.models.app_switch_context import AppSwitchContext
from paypalserversdk.models.mobile_web_context import MobileWebContext
from paypalserversdk.models.native_app_context import NativeAppContext

app_switch_context = AppSwitchContext(
    native_app=NativeAppContext(),
    mobile_web=MobileWebContext(
        buyer_user_agent='buyer_user_agent8'
    )
)
```

