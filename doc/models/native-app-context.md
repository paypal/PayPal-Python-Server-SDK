
# Native App Context

Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app.

## Structure

`NativeAppContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `os_type` | [`OsType`](../../doc/models/os-type.md) | Optional, Read-only | Operating System type of the device that the buyer is using.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `7`, *Pattern*: `^[A-Z_]+$` |
| `os_version` | `str` | Optional, Read-only | Operating System version of the device that the buyer is using.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^.*$` |

## Example

```python
from paypalserversdk.models.native_app_context import NativeAppContext

native_app_context = NativeAppContext()
```

