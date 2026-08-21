
# Card Authentication Response

Results of Authentication such as 3D Secure.

## Structure

`CardAuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_d_secure` | [`ThreeDSecureCardAuthenticationResponse`](../../doc/models/three-d-secure-card-authentication-response.md) | Optional | Results of 3D Secure Authentication. |

## Example

```python
from paypalserversdk.models.card_authentication_response import CardAuthenticationResponse
from paypalserversdk.models.enrollment_status import EnrollmentStatus
from paypalserversdk.models.pa_res_status import PaResStatus
from paypalserversdk.models.three_d_secure_card_authentication_response import ThreeDSecureCardAuthenticationResponse

card_authentication_response = CardAuthenticationResponse(
    three_d_secure=ThreeDSecureCardAuthenticationResponse(
        authentication_status=PaResStatus.CHALLENGEREQUIRED,
        enrollment_status=EnrollmentStatus.ENROLLED,
        authentication_id='authentication_id6'
    )
)
```

