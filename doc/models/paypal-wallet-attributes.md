
# Paypal Wallet Attributes

Additional attributes associated with the use of this PayPal Wallet.

## Structure

`PaypalWalletAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`PaypalWalletCustomerRequest`](../../doc/models/paypal-wallet-customer-request.md) | Optional | - |
| `vault` | [`PaypalWalletVaultInstruction`](../../doc/models/paypal-wallet-vault-instruction.md) | Optional | - |

## Example

```python
from paypalserversdk.models.name import Name
from paypalserversdk.models.paypal_payment_token_customer_type import PaypalPaymentTokenCustomerType
from paypalserversdk.models.paypal_payment_token_usage_type import PaypalPaymentTokenUsageType
from paypalserversdk.models.paypal_wallet_attributes import PaypalWalletAttributes
from paypalserversdk.models.paypal_wallet_customer_request import PaypalWalletCustomerRequest
from paypalserversdk.models.paypal_wallet_vault_instruction import PaypalWalletVaultInstruction
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.store_in_vault_instruction import StoreInVaultInstruction
from paypalserversdk.models.usage_pattern import UsagePattern

paypal_wallet_attributes = PaypalWalletAttributes(
    customer=PaypalWalletCustomerRequest(
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
    ),
    vault=PaypalWalletVaultInstruction(
        usage_type=PaypalPaymentTokenUsageType.MERCHANT,
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
        description='description6',
        usage_pattern=UsagePattern.THRESHOLD_PREPAID,
        customer_type=PaypalPaymentTokenCustomerType.CONSUMER,
        permit_multiple_payment_tokens=False
    )
)
```

