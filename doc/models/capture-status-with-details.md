
# Capture Status with Details

The status and status details of a captured payment.

## Structure

`CaptureStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`CaptureStatus`](../../doc/models/capture-status.md) | Optional, Read-only | The status of the captured payment. |
| `status_details` | [`CaptureStatusDetails`](../../doc/models/capture-status-details.md) | Optional | The details of the captured payment status. |

## Example

```python
from paypalserversdk.models.capture_incomplete_reason import CaptureIncompleteReason
from paypalserversdk.models.capture_status_details import CaptureStatusDetails
from paypalserversdk.models.capture_status_with_details import CaptureStatusWithDetails

capture_status_with_details = CaptureStatusWithDetails(
    status_details=CaptureStatusDetails(
        reason=CaptureIncompleteReason.VERIFICATION_REQUIRED
    )
)
```

