
# Venmo Wallet Experience Context

Customizes the buyer experience during the approval process for payment with Venmo. Note: Partners and Marketplaces might configure shipping_preference during partner account setup, which overrides the request values.

## Structure

`VenmoWalletExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | The business name of the merchant. The pattern is defined by an external party and supports Unicode.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `shipping_preference` | [`ShippingPreference`](../../doc/models/shipping-preference.md) | Optional | The location from which the shipping address is derived.<br>**Default**: `'GET_FROM_FILE'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `order_update_callback_config` | [`CallbackConfiguration`](../../doc/models/callback-configuration.md) | Optional | CallBack Configuration that the merchant can provide to PayPal/Venmo. |

## Example (as JSON)

```json
{
  "shipping_preference": "GET_FROM_FILE",
  "brand_name": "brand_name6",
  "order_update_callback_config": {
    "callback_events": [
      "SHIPPING_OPTIONS",
      "SHIPPING_ADDRESS",
      "SHIPPING_OPTIONS"
    ],
    "callback_url": "callback_url6"
  }
}
```

