
# Liability Shift Indicator

Liability shift indicator. The outcome of the issuer's authentication.

## Enumeration

`LiabilityShiftIndicator`

## Fields

| Name | Description |
|  --- | --- |
| `NO` | Liability is with the merchant. |
| `POSSIBLE` | Liability may shift to the card issuer. |
| `UNKNOWN` | The authentication system is not available. |

## Example

```python
from paypalserversdk.models.liability_shift_indicator import LiabilityShiftIndicator

liability_shift_indicator = LiabilityShiftIndicator.POSSIBLE
```

