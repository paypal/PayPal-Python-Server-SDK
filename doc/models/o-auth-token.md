
# O Auth Token

OAuth 2 Authorization endpoint response

## Structure

`OAuthToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | Access token |
| `token_type` | `str` | Required | Type of access token |
| `expires_in` | `int` | Optional | Time in seconds before the access token expires |
| `scope` | `str` | Optional | List of scopes granted<br>This is a space-delimited list of strings. |
| `expiry` | `int` | Optional | Time of token expiry as unix timestamp (UTC) |
| `refresh_token` | `str` | Optional | Refresh token<br>Used to get a new access token when it expires. |
| `id_token` | `str` | Optional | An ID token response type is of JSON Web Token (JWT) that contains claims about the identity of the authenticated user. |

## Example

```python
from paypalserversdk.models.o_auth_token import OAuthToken

o_auth_token = OAuthToken(
    access_token='access_token4',
    token_type='token_type4',
    expires_in=80,
    scope='scope4',
    expiry=242,
    refresh_token='refresh_token6',
    id_token='id_token4'
)
```

