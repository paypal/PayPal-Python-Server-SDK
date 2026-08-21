
# Patch

The JSON patch object to apply partial updates to resources.

## Structure

`Patch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `op` | [`PatchOp`](../../doc/models/patch-op.md) | Required | The operation. |
| `path` | `str` | Optional | The JSON Pointer to the target document location at which to complete the operation. |
| `value` | `Any` | Optional | The value to apply. The remove, copy, and move operations do not require a value. Since JSON Patch allows any type for value, the type property is not specified. |
| `mfrom` | `str` | Optional | The JSON Pointer to the target document location from which to move the value. Required for the move operation. |

## Example

```python
import jsonpickle

from paypalserversdk.models.patch import Patch
from paypalserversdk.models.patch_op import PatchOp

patch = Patch(
    op=PatchOp.COPY,
    path='path4',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    mfrom='from2'
)
```

