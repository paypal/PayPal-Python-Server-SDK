
# RequestLoggingConfiguration

Represents the logging configuration for API request.

## Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| log_body | `bool` | optional | Toggles the logging of the request body. **Default : `False`** |
| log_headers | `bool` | optional | Toggles the logging of the request headers. **Default : `False`** |
| headers_to_include | `List[str]` | optional | Includes only specified request headers in the log output. **Default : `[]`** |
| headers_to_exclude | `List[str]` | optional | Excludes specified request headers from the log output. **Default : `[]`** |
| headers_to_unmask | `List[str]` | optional | Logs specified request headers without masking, revealing their actual values. **Default : `[]`** |
| include_query_in_path | `bool` | optional | Toggles the inclusion of query parameters in the logged request path. **Default : `False`** |

