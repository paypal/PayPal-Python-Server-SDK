
# Default Error Exception

The error details.

## Structure

`DefaultErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The human-readable, unique name of the error. |
| `message` | `str` | Required | The message that describes the error. |
| `debug_id` | `str` | Required | The PayPal internal ID. Used for correlation purposes. |
| `information_link` | `str` | Optional | The information link, or URI, that shows detailed information about this error for the developer. |
| `details` | [`List[TransactionSearchErrorDetails]`](../../doc/models/transaction-search-error-details.md) | Optional | An array of additional details about the error. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links). |

## Example (as JSON)

```json
{
  "name": "name2",
  "message": "message2",
  "debug_id": "debug_id8",
  "information_link": "information_link4",
  "details": [
    {
      "field": "field4",
      "value": "value2",
      "location": "location4",
      "issue": "issue6",
      "description": "description0"
    }
  ],
  "links": [
    {
      "href": "href6",
      "rel": "rel0",
      "method": "HEAD"
    }
  ]
}
```

