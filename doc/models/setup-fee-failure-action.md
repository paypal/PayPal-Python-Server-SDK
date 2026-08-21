
# Setup Fee Failure Action

The action to take on the subscription if the initial payment for the setup fails.

## Enumeration

`SetupFeeFailureAction`

## Fields

| Name | Description |
|  --- | --- |
| `CONTINUE` | Continues the subscription if the initial payment for the setup fails. |
| `CANCEL` | Cancels the subscription if the initial payment for the setup fails. |

## Example

```python
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction

setup_fee_failure_action = SetupFeeFailureAction.CONTINUE
```

