
# Token Type

The tokenization method that generated the ID.

## Enumeration

`TokenType`

## Fields

| Name | Description |
|  --- | --- |
| `BILLING_AGREEMENT` | The PayPal billing agreement ID. References an approved recurring payment for goods or services. |

## Example

```python
from paypalserversdk.models.token_type import TokenType

token_type = TokenType.BILLING_AGREEMENT
```

