
# Balance Information

The Balance information.

## Structure

`BalanceInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `primary` | `bool` | Optional | Optional field representing if the currency is primary currency or not. |
| `total_balance` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `available_balance` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `withheld_balance` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example

```python
from paypalserversdk.models.balance_information import BalanceInformation
from paypalserversdk.models.money import Money

balance_information = BalanceInformation(
    currency='currency8',
    total_balance=Money(
        currency_code='currency_code6',
        value='value2'
    ),
    primary=False,
    available_balance=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    withheld_balance=Money(
        currency_code='currency_code2',
        value='value8'
    )
)
```

