
# Subscription Pricing Model

The pricing model for tiered plan. The `tiers` parameter is required.

## Enumeration

`SubscriptionPricingModel`

## Fields

| Name | Description |
|  --- | --- |
| `VOLUME` | A volume pricing model. |
| `TIERED` | A tiered pricing model. |

## Example

```python
from paypalserversdk.models.subscription_pricing_model import SubscriptionPricingModel

subscription_pricing_model = SubscriptionPricingModel.VOLUME
```

