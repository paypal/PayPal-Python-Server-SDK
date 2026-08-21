
# Error Exception

The error details.

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The human-readable, unique name of the error. |
| `message` | `str` | Required | The message that describes the error. |
| `debug_id` | `str` | Required | The PayPal internal ID. Used for correlation purposes. |
| `details` | [`List[ErrorDetails]`](../../doc/models/error-details.md) | Optional | An array of additional details about the error. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas-links). |

## Example

```python
try:
    # make the API call
except ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

