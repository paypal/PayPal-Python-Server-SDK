
# Taxes Override

The tax details.

## Structure

`TaxesOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `percentage` | `str` | Optional | The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`.<br><br>**Constraints**: *Pattern*: `^((-?[0-9]+)\|(-?([0-9]+)?[.][0-9]+))$` |
| `inclusive` | `bool` | Optional | Indicates whether the tax was already included in the billing amount. |

## Example

```python
from paypalserversdk.models.taxes_override import TaxesOverride

taxes_override = TaxesOverride(
    percentage='percentage2',
    inclusive=False
)
```

