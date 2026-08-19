
# Venmo Wallet Experience Context

Customizes the buyer experience during the approval process for payment with Venmo. Note: Partners and Marketplaces might configure shipping_preference during partner account setup, which overrides the request values.

## Structure

`VenmoWalletExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | The business name of the merchant. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `shipping_preference` | [`VenmoWalletExperienceContextShippingPreference`](../../doc/models/venmo-wallet-experience-context-shipping-preference.md) | Optional | The location from which the shipping address is derived.<br><br>**Default**: `"GET_FROM_FILE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `order_update_callback_config` | [`CallbackConfiguration`](../../doc/models/callback-configuration.md) | Optional | CallBack Configuration that the merchant can provide to PayPal/Venmo. |
| `user_action` | [`VenmoWalletExperienceContextUserAction`](../../doc/models/venmo-wallet-experience-context-user-action.md) | Optional | Configures a Continue or Pay Now checkout flow.<br><br>**Default**: `"CONTINUE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `8`, *Pattern*: `^[0-9A-Z_]+$` |

## Example

```python
from paypalserversdk.models.callback_configuration import CallbackConfiguration
from paypalserversdk.models.callback_events import CallbackEvents
from paypalserversdk.models.venmo_wallet_experience_context import VenmoWalletExperienceContext
from paypalserversdk.models.venmo_wallet_experience_context_shipping_preference import VenmoWalletExperienceContextShippingPreference
from paypalserversdk.models.venmo_wallet_experience_context_user_action import VenmoWalletExperienceContextUserAction

venmo_wallet_experience_context = VenmoWalletExperienceContext(
    brand_name='brand_name2',
    shipping_preference=VenmoWalletExperienceContextShippingPreference.GET_FROM_FILE,
    order_update_callback_config=CallbackConfiguration(
        callback_events=[
            CallbackEvents.SHIPPING_OPTIONS,
            CallbackEvents.SHIPPING_ADDRESS,
            CallbackEvents.SHIPPING_OPTIONS
        ],
        callback_url='callback_url6'
    ),
    user_action=VenmoWalletExperienceContextUserAction.CONTINUE
)
```

