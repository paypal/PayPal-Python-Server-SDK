
# Tax Amount

The tax levied by a government on the purchase of goods or services.

## Structure

`TaxAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.tax_amount import TaxAmount

tax_amount = TaxAmount(
    tax_amount=Money(
        currency_code='currency_code2',
        value='value8'
    )
)
```

