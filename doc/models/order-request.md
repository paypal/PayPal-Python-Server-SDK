
# Order Request

The order request details.

## Structure

`OrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `intent` | [`CheckoutPaymentIntent`](../../doc/models/checkout-payment-intent.md) | Required | The intent to either capture payment immediately or authorize a payment for an order after order creation. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `payer` | [`Payer`](../../doc/models/payer.md) | Optional | DEPRECATED. The customer is also known as the payer. The Payer object was intended to only be used with the `payment_source.paypal` object. In order to make this design more clear, the details in the `payer` object are now available under `payment_source.paypal`. Please use `payment_source.paypal`. |
| `purchase_units` | [`List[PurchaseUnitRequest]`](../../doc/models/purchase-unit-request.md) | Required | An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `payment_source` | [`PaymentSource`](../../doc/models/payment-source.md) | Optional | The payment source definition. |
| `application_context` | [`OrderApplicationContext`](../../doc/models/order-application-context.md) | Optional | Customizes the payer experience during the approval process for the payment with PayPal. Note: Partners and Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the request values. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.amount_breakdown import AmountBreakdown
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.bancontact_payment_request import BancontactPaymentRequest
from paypalserversdk.models.blik_experience_context import BlikExperienceContext
from paypalserversdk.models.blik_level_0_payment_object import BlikLevel0PaymentObject
from paypalserversdk.models.blik_one_click_payment_request import BlikOneClickPaymentRequest
from paypalserversdk.models.blik_payment_request import BlikPaymentRequest
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.disbursement_mode import DisbursementMode
from paypalserversdk.models.experience_context import ExperienceContext
from paypalserversdk.models.experience_context_shipping_preference import ExperienceContextShippingPreference
from paypalserversdk.models.money import Money
from paypalserversdk.models.name import Name
from paypalserversdk.models.order_application_context import OrderApplicationContext
from paypalserversdk.models.order_application_context_landing_page import OrderApplicationContextLandingPage
from paypalserversdk.models.order_application_context_shipping_preference import OrderApplicationContextShippingPreference
from paypalserversdk.models.order_application_context_user_action import OrderApplicationContextUserAction
from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.payee_base import PayeeBase
from paypalserversdk.models.payer import Payer
from paypalserversdk.models.payment_instruction import PaymentInstruction
from paypalserversdk.models.payment_source import PaymentSource
from paypalserversdk.models.paypal_wallet import PaypalWallet
from paypalserversdk.models.phone_number import PhoneNumber
from paypalserversdk.models.phone_type import PhoneType
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.platform_fee import PlatformFee
from paypalserversdk.models.processing_instruction import ProcessingInstruction
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from paypalserversdk.models.token import Token
from paypalserversdk.models.token_type import TokenType

order_request = OrderRequest(
    intent=CheckoutPaymentIntent.CAPTURE,
    purchase_units=[
        PurchaseUnitRequest(
            amount=AmountWithBreakdown(
                currency_code='currency_code6',
                value='value0',
                breakdown=AmountBreakdown(
                    item_total=Money(
                        currency_code='currency_code0',
                        value='value6'
                    ),
                    shipping=Money(
                        currency_code='currency_code0',
                        value='value6'
                    ),
                    handling=Money(
                        currency_code='currency_code2',
                        value='value8'
                    ),
                    tax_total=Money(
                        currency_code='currency_code4',
                        value='value0'
                    ),
                    insurance=Money(
                        currency_code='currency_code2',
                        value='value8'
                    )
                )
            ),
            reference_id='reference_id4',
            payee=PayeeBase(
                email_address='email_address4',
                merchant_id='merchant_id6'
            ),
            payment_instruction=PaymentInstruction(
                platform_fees=[
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0'
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6'
                        )
                    ),
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0'
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6'
                        )
                    ),
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0'
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6'
                        )
                    )
                ],
                disbursement_mode=DisbursementMode.INSTANT,
                payee_pricing_tier_id='payee_pricing_tier_id2',
                payee_receivable_fx_rate_id='payee_receivable_fx_rate_id0'
            ),
            description='description6',
            custom_id='custom_id4'
        )
    ],
    processing_instruction=ProcessingInstruction.ORDER_COMPLETE_ON_PAYMENT_APPROVAL,
    payer=Payer(
        email_address='email_address6',
        payer_id='payer_id6',
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
        birth_date='birth_date4'
    ),
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
    application_context=OrderApplicationContext(
        brand_name='brand_name8',
        locale='locale2',
        landing_page=OrderApplicationContextLandingPage.BILLING,
        shipping_preference=OrderApplicationContextShippingPreference.SET_PROVIDED_ADDRESS,
        user_action=OrderApplicationContextUserAction.CONTINUE
    )
)
```

