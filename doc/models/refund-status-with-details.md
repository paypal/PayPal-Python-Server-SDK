
# Refund Status with Details

The refund status with details.

## Structure

`RefundStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`RefundStatus`](../../doc/models/refund-status.md) | Optional, Read-only | The status of the refund. |
| `status_details` | [`RefundStatusDetails`](../../doc/models/refund-status-details.md) | Optional | The details of the refund status. |

## Example

```python
from paypalserversdk.models.refund_incomplete_reason import RefundIncompleteReason
from paypalserversdk.models.refund_status_details import RefundStatusDetails
from paypalserversdk.models.refund_status_with_details import RefundStatusWithDetails

refund_status_with_details = RefundStatusWithDetails(
    status_details=RefundStatusDetails(
        reason=RefundIncompleteReason.ECHECK
    )
)
```

