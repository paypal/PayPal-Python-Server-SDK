
# Cobranded Card

Details about the merchant cobranded card used for order purchase.

## Structure

`CobrandedCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `labels` | `List[str]` | Optional | Array of labels for the cobranded card.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `25`, *Minimum Length*: `1`, *Maximum Length*: `256` |
| `payee` | [`PayeeBase`](../../doc/models/payee-base.md) | Optional | The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the payee. |
| `amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example

```python
from paypalserversdk.models.cobranded_card import CobrandedCard
from paypalserversdk.models.money import Money
from paypalserversdk.models.payee_base import PayeeBase

cobranded_card = CobrandedCard(
    labels=[
        'labels0',
        'labels1',
        'labels2'
    ],
    payee=PayeeBase(
        email_address='email_address4',
        merchant_id='merchant_id6'
    ),
    amount=Money(
        currency_code='currency_code6',
        value='value0'
    )
)
```

