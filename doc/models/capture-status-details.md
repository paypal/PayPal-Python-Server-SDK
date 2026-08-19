
# Capture Status Details

The details of the captured payment status.

## Structure

`CaptureStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`CaptureIncompleteReason`](../../doc/models/capture-incomplete-reason.md) | Optional | The reason why the captured payment status is `PENDING` or `DENIED`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[A-Z_]+$` |

## Example

```python
from paypalserversdk.models.capture_incomplete_reason import CaptureIncompleteReason
from paypalserversdk.models.capture_status_details import CaptureStatusDetails

capture_status_details = CaptureStatusDetails(
    reason=CaptureIncompleteReason.OTHER
)
```

