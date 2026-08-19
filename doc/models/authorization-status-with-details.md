
# Authorization Status with Details

The status fields and status details for an authorized payment.

## Structure

`AuthorizationStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`AuthorizationStatus`](../../doc/models/authorization-status.md) | Optional, Read-only | The status for the authorized payment. |
| `status_details` | [`AuthorizationStatusDetails`](../../doc/models/authorization-status-details.md) | Optional | The details of the authorized payment status. |

## Example

```python
from paypalserversdk.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypalserversdk.models.authorization_status_details import AuthorizationStatusDetails
from paypalserversdk.models.authorization_status_with_details import AuthorizationStatusWithDetails

authorization_status_with_details = AuthorizationStatusWithDetails(
    status_details=AuthorizationStatusDetails(
        reason=AuthorizationIncompleteReason.PENDING_REVIEW
    )
)
```

