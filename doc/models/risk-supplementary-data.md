
# Risk Supplementary Data

Additional information necessary to evaluate the risk profile of a transaction.

## Structure

`RiskSupplementaryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`ParticipantMetadata`](../../doc/models/participant-metadata.md) | Optional | Profile information of the sender or receiver. |

## Example

```python
from paypalserversdk.models.participant_metadata import ParticipantMetadata
from paypalserversdk.models.risk_supplementary_data import RiskSupplementaryData

risk_supplementary_data = RiskSupplementaryData(
    customer=ParticipantMetadata(
        ip_address='ip_address0'
    )
)
```

