
# Payment Supplementary Data

The supplementary data.

## Structure

`PaymentSupplementaryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `related_ids` | [`RelatedIdentifiers`](../../doc/models/related-identifiers.md) | Optional | Identifiers related to a specific resource. |

## Example

```python
from paypalserversdk.models.payment_supplementary_data import PaymentSupplementaryData
from paypalserversdk.models.related_identifiers import RelatedIdentifiers

payment_supplementary_data = PaymentSupplementaryData(
    related_ids=RelatedIdentifiers(
        order_id='order_id2',
        authorization_id='authorization_id0',
        capture_id='capture_id0'
    )
)
```

