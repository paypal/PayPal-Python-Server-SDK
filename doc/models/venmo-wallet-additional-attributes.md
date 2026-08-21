
# Venmo Wallet Additional Attributes

Additional attributes associated with the use of this Venmo Wallet.

## Structure

`VenmoWalletAdditionalAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`VenmoWalletCustomerInformation`](../../doc/models/venmo-wallet-customer-information.md) | Optional | The details about a customer in PayPal's system of record. |
| `vault` | [`VenmoWalletVaultAttributes`](../../doc/models/venmo-wallet-vault-attributes.md) | Optional | Resource consolidating common request and response attirbutes for vaulting Venmo Wallet. |

## Example

```python
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction
from paypalserversdk.models.venmo_payment_token_customer_type import VenmoPaymentTokenCustomerType
from paypalserversdk.models.venmo_payment_token_usage_pattern import VenmoPaymentTokenUsagePattern
from paypalserversdk.models.venmo_payment_token_usage_type import VenmoPaymentTokenUsageType
from paypalserversdk.models.venmo_wallet_additional_attributes import VenmoWalletAdditionalAttributes
from paypalserversdk.models.venmo_wallet_customer_information import VenmoWalletCustomerInformation
from paypalserversdk.models.venmo_wallet_vault_attributes import VenmoWalletVaultAttributes

venmo_wallet_additional_attributes = VenmoWalletAdditionalAttributes(
    customer=VenmoWalletCustomerInformation(
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
        )
    ),
    vault=VenmoWalletVaultAttributes(
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
        usage_type=VenmoPaymentTokenUsageType.MERCHANT,
        description='description6',
        usage_pattern=VenmoPaymentTokenUsagePattern.THRESHOLD_PREPAID,
        customer_type=VenmoPaymentTokenCustomerType.CONSUMER,
        permit_multiple_payment_tokens=False
    )
)
```

