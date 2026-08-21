
# Card Type

Type of card. i.e Credit, Debit and so on.

## Enumeration

`CardType`

## Fields

| Name | Description |
|  --- | --- |
| `CREDIT` | A credit card. |
| `DEBIT` | A debit card. |
| `PREPAID` | A Prepaid card. |
| `STORE` | A store card. |
| `UNKNOWN` | Card type cannot be determined. |

## Example

```python
from paypalserversdk.models.card_type import CardType

card_type = CardType.UNKNOWN
```

