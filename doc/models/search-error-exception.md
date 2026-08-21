
# Search Error Exception

The error details.

## Structure

`SearchErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The human-readable, unique name of the error. |
| `message` | `str` | Required | The message that describes the error. |
| `debug_id` | `str` | Required | The PayPal internal ID. Used for correlation purposes. |
| `information_link` | `str` | Optional, Read-only | The information link, or URI, that shows detailed information about this error for the developer. |
| `details` | [`List[TransactionSearchErrorDetails]`](../../doc/models/transaction-search-error-details.md) | Optional | An array of additional details about the error. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links). |
| `total_items` | `int` | Optional | The total number of transactions. Valid only for `RESULTSET_TOO_LARGE`.<br><br>**Constraints**: `>= 0`, `<= 2147483647` |
| `maximum_items` | `int` | Optional | The maximum number of transactions. Valid only for `RESULTSET_TOO_LARGE`.<br><br>**Constraints**: `>= 0`, `<= 2147483647` |

## Example

```python
try:
    # make the API call
except SearchErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

