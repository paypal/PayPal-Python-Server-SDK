
# Refund Status Details

The details of the refund status.

## Structure

`RefundStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`RefundIncompleteReason`](../../doc/models/refund-incomplete-reason.md) | Optional | The reason why the refund has the `PENDING` or `FAILED` status. |

## Example

```python
from paypalserversdk.models.refund_incomplete_reason import RefundIncompleteReason
from paypalserversdk.models.refund_status_details import RefundStatusDetails

refund_status_details = RefundStatusDetails(
    reason=RefundIncompleteReason.ECHECK
)
```

