
# Authorization Status Details

The details of the authorized payment status.

## Structure

`AuthorizationStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`AuthorizationIncompleteReason`](../../doc/models/authorization-incomplete-reason.md) | Optional | The reason why the authorized status is `PENDING`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[A-Z_]+$` |

## Example

```python
from paypalserversdk.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypalserversdk.models.authorization_status_details import AuthorizationStatusDetails

authorization_status_details = AuthorizationStatusDetails(
    reason=AuthorizationIncompleteReason.PENDING_REVIEW
)
```

