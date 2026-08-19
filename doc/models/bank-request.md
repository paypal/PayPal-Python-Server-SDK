
# Bank Request

A Resource representing a request to vault a Bank used for ACH Debit.

## Structure

`BankRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ach_debit` | `Any` | Optional | A Resource representing a request to vault a ACH Debit. |
| `sepa_debit` | [`SepaDebitRequest`](../../doc/models/sepa-debit-request.md) | Optional | An API resource denoting a request to securely store a SEPA Debit. |

## Example

```python
import jsonpickle

from paypalserversdk.models.bank_request import BankRequest
from paypalserversdk.models.sepa_debit_experience_context import SepaDebitExperienceContext
from paypalserversdk.models.sepa_debit_request import SepaDebitRequest

bank_request = BankRequest(
    ach_debit=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    sepa_debit=SepaDebitRequest(
        experience_context=SepaDebitExperienceContext(
            return_url='return_url4',
            cancel_url='cancel_url6',
            locale='locale6'
        )
    )
)
```

