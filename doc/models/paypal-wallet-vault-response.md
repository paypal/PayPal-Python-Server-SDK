
# Paypal Wallet Vault Response

The details about a saved PayPal Wallet payment source.

## Structure

`PaypalWalletVaultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the saved payment source.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `status` | [`PaypalWalletVaultStatus`](../../doc/models/paypal-wallet-vault-status.md) | Optional | The vault status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `customer` | [`PaypalWalletCustomer`](../../doc/models/paypal-wallet-customer.md) | Optional | The details about a customer in PayPal's system of record. |

## Example

```python
from paypalserversdk.models.name import Name
from paypalserversdk.models.paypal_wallet_customer import PaypalWalletCustomer
from paypalserversdk.models.paypal_wallet_vault_response import PaypalWalletVaultResponse
from paypalserversdk.models.paypal_wallet_vault_status import PaypalWalletVaultStatus
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType

paypal_wallet_vault_response = PaypalWalletVaultResponse(
    id='id6',
    status=PaypalWalletVaultStatus.CREATED,
    customer=PaypalWalletCustomer(
        id='id0',
        email_address='email_address2',
        phone=PhoneWithType(
            phone_number=PhoneNumber(
                national_number='national_number6'
            ),
            phone_type=PhoneType.OTHER
        ),
        name=Name(
            given_name='given_name2',
            surname='surname8'
        ),
        merchant_customer_id='merchant_customer_id2'
    )
)
```

