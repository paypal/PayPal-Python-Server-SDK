
# Universal Product Code

The Universal Product Code of the item.

## Structure

`UniversalProductCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`UpcType`](../../doc/models/upc-type.md) | Required | The Universal Product Code type.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `5`, *Pattern*: `^[0-9A-Z_-]+$` |
| `code` | `str` | Required | The UPC product code of the item.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `17`, *Pattern*: `^[0-9]{0,17}$` |

## Example

```python
from paypalserversdk.models.universal_product_code import UniversalProductCode
from paypalserversdk.models.upc_type import UpcType

universal_product_code = UniversalProductCode(
    mtype=UpcType.UPC_5,
    code='code2'
)
```

