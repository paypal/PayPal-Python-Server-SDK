
# Authentication Response

Results of Authentication such as 3D Secure.

## Structure

`AuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `liability_shift` | [`LiabilityShiftIndicator`](../../doc/models/liability-shift-indicator.md) | Optional | Liability shift indicator. The outcome of the issuer's authentication.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `three_d_secure` | [`ThreeDSecureAuthenticationResponse`](../../doc/models/three-d-secure-authentication-response.md) | Optional | Results of 3D Secure Authentication. |

## Example

```python
from paypalserversdk.models.authentication_response import AuthenticationResponse
from paypalserversdk.models.enrollment_status import EnrollmentStatus
from paypalserversdk.models.liability_shift_indicator import LiabilityShiftIndicator
from paypalserversdk.models.pa_res_status import PaResStatus
from paypalserversdk.models.three_d_secure_authentication_response import ThreeDSecureAuthenticationResponse

authentication_response = AuthenticationResponse(
    liability_shift=LiabilityShiftIndicator.UNKNOWN,
    three_d_secure=ThreeDSecureAuthenticationResponse(
        authentication_status=PaResStatus.CHALLENGEREQUIRED,
        enrollment_status=EnrollmentStatus.ENROLLED
    )
)
```

