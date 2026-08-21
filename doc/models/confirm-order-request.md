
# Confirm Order Request

Payer confirms the intent to pay for the Order using the provided payment source.

## Structure

`ConfirmOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_source` | [`PaymentSource`](../../doc/models/payment-source.md) | Required | The payment source definition. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `application_context` | [`OrderConfirmApplicationContext`](../../doc/models/order-confirm-application-context.md) | Optional | Customizes the payer confirmation experience. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.bancontact_payment_request import BancontactPaymentRequest
from paypalserversdk.models.blik_experience_context import BlikExperienceContext
from paypalserversdk.models.blik_level_0_payment_object import BlikLevel0PaymentObject
from paypalserversdk.models.blik_one_click_payment_request import BlikOneClickPaymentRequest
from paypalserversdk.models.blik_payment_request import BlikPaymentRequest
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.confirm_order_request import ConfirmOrderRequest
from paypalserversdk.models.experience_context import ExperienceContext
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.name import Name
from paypalserversdk.models.network_transaction import NetworkTransaction
from paypalserversdk.models.order_confirm_application_context import OrderConfirmApplicationContext
from paypalserversdk.models.payment_initiator import PaymentInitiator
from paypalserversdk.models.payment_source import PaymentSource
from paypalserversdk.models.paypal_wallet import PaypalWallet
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.processing_instruction import ProcessingInstruction
from paypalserversdk.models.stored_payment_source import StoredPaymentSource
from paypalserversdk.models.stored_payment_source_payment_type import StoredPaymentSourcePaymentType
from paypalserversdk.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType
from paypalserversdk.models.token import Token
from paypalserversdk.models.token_type import TokenType

confirm_order_request = ConfirmOrderRequest(
    payment_source=PaymentSource(
        card=CardRequest(
            name='name6',
            number='number6',
            expiry='expiry4',
            security_code='security_code8',
            billing_address=Address(
                country_code='country_code8',
                address_line_1='address_line_12',
                address_line_2='address_line_28',
                admin_area_2='admin_area_28',
                admin_area_1='admin_area_14',
                postal_code='postal_code0'
            )
        ),
        token=Token(
            id='id6',
            mtype=TokenType.BILLING_AGREEMENT
        ),
        paypal=PaypalWallet(
            vault_id='vault_id0',
            email_address='email_address0',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            ),
            phone=PhoneWithType(
                phone_number=PhoneNumber(
                    national_number='national_number6'
                ),
                phone_type=PhoneType.OTHER
            ),
            birth_date='birth_date8'
        ),
        bancontact=BancontactPaymentRequest(
            name='name0',
            country_code='country_code0',
            experience_context=ExperienceContext(
                brand_name='brand_name2',
                locale='locale6',
                shipping_preference=ExperienceContextShippingPreference.NO_SHIPPING,
                return_url='return_url4',
                cancel_url='cancel_url6'
            )
        ),
        blik=BlikPaymentRequest(
            name='name2',
            country_code='country_code2',
            email='email4',
            experience_context=BlikExperienceContext(
                brand_name='brand_name2',
                locale='locale6',
                shipping_preference=ExperienceContextShippingPreference.NO_SHIPPING,
                return_url='return_url4',
                cancel_url='cancel_url6'
            ),
            level_0=BlikLevel0PaymentObject(
                auth_code='auth_code8'
            ),
            one_click=BlikOneClickPaymentRequest(
                consumer_reference='consumer_reference2',
                auth_code='auth_code0',
                alias_label='alias_label6',
                alias_key='alias_key4'
            )
        )
    ),
    processing_instruction=ProcessingInstruction.ORDER_COMPLETE_ON_PAYMENT_APPROVAL,
    application_context=OrderConfirmApplicationContext(
        brand_name='brand_name8',
        locale='locale2',
        return_url='return_url0',
        cancel_url='cancel_url2',
        stored_payment_source=StoredPaymentSource(
            payment_initiator=PaymentInitiator.CUSTOMER,
            payment_type=StoredPaymentSourcePaymentType.RECURRING,
            usage=StoredPaymentSourceUsageType.FIRST,
            previous_network_transaction_reference=NetworkTransaction(
                id='id6',
                date='date2',
                network=CardBrand.CONFIDIS,
                acquirer_reference_number='acquirer_reference_number8'
            )
        )
    )
)
```

