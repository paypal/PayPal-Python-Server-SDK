
# Phone with Type

The phone information.

## Structure

`PhoneWithType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_type` | [`PhoneType`](../../doc/models/phone-type.md) | Optional | The phone type. |
| `phone_number` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | The phone number in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). |

## Example

```python
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType

phone_with_type = PhoneWithType(
    phone_number=PhoneNumber(
        national_number='national_number6'
    ),
    phone_type=PhoneType.PAGER
)
```

