import random

import jsonpickle
from paypalserversdk.exceptions.error_exception import ErrorException
from paypalserversdk.models.address import Address
from paypalserversdk.models.amount_breakdown import AmountBreakdown
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.card_attributes import CardAttributes
from paypalserversdk.models.card_experience_context import CardExperienceContext
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.card_verification import CardVerification
from paypalserversdk.models.card_verification_method import CardVerificationMethod
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.confirm_order_request import ConfirmOrderRequest
from paypalserversdk.models.item import Item
from paypalserversdk.models.money import Money
from paypalserversdk.models.name import Name
from paypalserversdk.models.order_capture_request import OrderCaptureRequest
from paypalserversdk.models.order_capture_request_payment_source import (
    OrderCaptureRequestPaymentSource,
)
from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.order_tracker_item import OrderTrackerItem
from paypalserversdk.models.order_tracker_request import OrderTrackerRequest
from paypalserversdk.models.patch import Patch
from paypalserversdk.models.patch_op import PatchOp
from paypalserversdk.models.pay_pal_experience_landing_page import (
    PayPalExperienceLandingPage,
)
from paypalserversdk.models.pay_pal_experience_user_action import (
    PayPalExperienceUserAction,
)
from paypalserversdk.models.pay_pal_wallet import PayPalWallet
from paypalserversdk.models.pay_pal_wallet_experience_context import (
    PayPalWalletExperienceContext,
)
from paypalserversdk.models.payee_payment_method_preference import (
    PayeePaymentMethodPreference,
)
from paypalserversdk.models.payment_source import PaymentSource
from paypalserversdk.models.payment_token_request import PaymentTokenRequest
from paypalserversdk.models.payment_token_request_payment_source import (
    PaymentTokenRequestPaymentSource,
)
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from paypalserversdk.models.setup_token_request import SetupTokenRequest
from paypalserversdk.models.setup_token_request_payment_source import (
    SetupTokenRequestPaymentSource,
)
from paypalserversdk.models.shipment_carrier import ShipmentCarrier
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.shipping_preference import ShippingPreference
from paypalserversdk.models.token_request_type import TokenRequestType
from paypalserversdk.models.universal_product_code import UniversalProductCode
from paypalserversdk.models.upc_type import UPCType
from paypalserversdk.models.vault_experience_context import VaultExperienceContext
from paypalserversdk.models.vault_pay_pal_wallet_request import VaultPayPalWalletRequest
from paypalserversdk.models.vault_token_request import VaultTokenRequest
from tests.e2etests.e2e_test_base import E2ETestBase
from tests.e2etests.playwrightflows import PlaywrightFlows


class E2ETests(E2ETestBase):
    """E2E Tests Class contains all the E2E tests."""

    # class variables
    ordercontroller = None
    paymentcontroller = None
    vaultcontroller = None
    flows = None

    # Method to set up the E2E tests
    @classmethod
    def setUpClass(cls):
        super(E2ETests, cls).setUpClass()
        # Initialize the client ,playwright flows instance ,controllers and response catchers
        cls.ordercontroller = cls.client.orders
        cls.vaultcontroller = cls.client.vault
        cls.paymentcontroller = cls.client.payments
        cls.order_response_catcher = cls.ordercontroller.http_call_back
        cls.flows = PlaywrightFlows()

    
    # Method to tear down the E2E tests
    @classmethod
    def tearDownClass(cls):
        cls.client = None
        cls.ordercontroller = None
        cls.paymentcontroller = None
        cls.vaultcontroller = None
        cls.order_response_catcher = None
        cls.vault_response_catcher = None
        cls.flows.destruct()

    # Method to setup a new page for playwright before each test
    def setUp(self):
        self.flows.generate_new_page()

    # Method to close the page after each test
    def tearDown(self):
        self.flows.teardown()

    #  E2E test for refund order flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Refund the order
    # 4. Get the refund
    def test_refund_flow(self):
        # create a random string
        random_string = str(random.randint(0, 100000))
        # create order
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="10.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="10.0"),
                                shipping=Money(currency_code="USD", value="0.0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Camera Shop",
                        items=[
                            Item(
                                name="Levis 501 Selvedge STF",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            ),
                            Item(
                                name="T-Shirt",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="1457432",
                            ),
                        ],
                        shipping=ShippingDetails(
                            address=Address(
                                country_code="US",
                                address_line_1="123 Main Street",
                                admin_area_2="San Jose",
                                admin_area_1="CA",
                                postal_code="95131",
                            )
                        ),
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id
        confirm_order_link = created_order.body.links[1].href

        assert order_id is not None
        assert confirm_order_link is not None

        # complete payment
        assert self.flows.complete_payment(confirm_order_link)

        

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        capture_id = captured_order.body.purchase_units[0].payments.captures[0].id

        assert capture_id is not None

        

        # refund order
        collect = {"capture_id": capture_id, "prefer": "return=representation"}

        refunded_order = self.paymentcontroller.captures_refund(collect)

        # check status code
        assert refunded_order.status_code == 201

        refund_id = refunded_order.body.id

        assert refund_id is not None

        

        # get refund
        get_refund = self.paymentcontroller.refunds_get(refund_id)

        # check status code
        assert get_refund.status_code == 200

    # E2E test for patch order flow:
    # 1. Create an order
    # 2. Patch the order
    # 3. Get the order
    def test_patch_flow(self):
        random_string = str(random.randint(0, 100000))
        # As this flow requires no browser interaction , setting the isSuccessful to True so no trace is created
        self.flows.isSuccessful = True
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="10.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="10.0"),
                                shipping=Money(currency_code="USD", value="0.0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Camera Shop",
                        items=[
                            Item(
                                name="Levis 501 Selvedge STF",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            ),
                            Item(
                                name="T-Shirt",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="1457432",
                            ),
                        ],
                        shipping=ShippingDetails(
                            address=Address(
                                country_code="US",
                                address_line_1="123 Main Street",
                                admin_area_2="San Jose",
                                admin_area_1="CA",
                                postal_code="95131",
                            )
                        ),
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        
        # patch order
        collect = {
            "id": order_id,
            "body": [
                Patch(
                    op=PatchOp.REPLACE,
                    path="/purchase_units/@reference_id=='default'/shipping/address",
                    value=jsonpickle.decode(
                        '{"address_line_1":"1234 Main St","address_line_2":"Floor 6","admin_area_2":"San Francisco","admin_area_1":"CA","postal_code":"94107","country_code":"US"}'
                    ),
                )
            ],
        }

        patched_order = self.ordercontroller.orders_patch(collect)

        # check status code
        assert patched_order.status_code == 204

        
        # get order
        collect = {
            "id": order_id,
        }
        get_order = self.ordercontroller.orders_get(collect)

        # check status code
        assert get_order.status_code == 200

        # check if the address was updated
        assert (
            get_order.body.purchase_units[0].shipping.address.address_line_1
            == "1234 Main St"
        )

    # E2E test for confirm order flow:
    # 1. Create an order
    # 2. Complete helios verification
    # 3. Get the order and check if the payment source is not None
    # 4. Capture the order
    def test_3D_secure_authentication_single_step(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="10.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="10.00")
                            ),
                        ),
                        description="Camera Shop",
                        custom_id="testcustom_id",
                        invoice_id=f"invoice_number_{random_string}",
                        items=[
                            Item(
                                name="Levis 501 Selvedge STF",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            ),
                            Item(
                                name="T-Shirt",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="1457432",
                            ),
                        ],
                    )
                ],
                payment_source=PaymentSource(
                    card=CardRequest(
                        name="John Doe",
                        number="4868719995056080",
                        expiry="2027-02",
                        billing_address=Address(
                            country_code="US",
                            address_line_1="2211 N First Street",
                            admin_area_2="San Jose",
                            admin_area_1="CA",
                            postal_code="95131",
                        ),
                        attributes=CardAttributes(
                            verification=CardVerification(
                                method=CardVerificationMethod.SCA_ALWAYS
                            )
                        ),
                        experience_context=CardExperienceContext(
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        ),
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=minimal",
        }

        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 201

        order_id = created_order.body.id
        confirm_order_link = created_order.body.links[1].href

        assert order_id is not None
        assert confirm_order_link is not None

        # complete payment
        assert self.flows.complete_helios_verification(
            confirm_order_link, timeout=13000
        )

        

        # get order
        collect = {
            "id": order_id,
        }
        get_order = self.ordercontroller.orders_get(collect)

        # check status code
        assert get_order.status_code == 200

        assert get_order.body.payment_source is not None

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        assert captured_order.body.status == "COMPLETED"

    # E2E test for 3D secure authentication multi-step flow:
    # 1. Create an order
    # 2. Capture the order
    # 3. Complete helios verification
    # 4. Get the order and check if the payment source is not None
    # 5. Capture the order
    def test_3D_secure_authentication_multi_step(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="10.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="10.00")
                            ),
                        ),
                        description="Camera Shop",
                        custom_id="testcustom_id",
                        invoice_id=f"invoice_number_{random_string}",
                        items=[
                            Item(
                                name="Levis 501 Selvedge STF",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            ),
                            Item(
                                name="T-Shirt",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="1457432",
                            ),
                        ],
                    )
                ],
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 201

        order_id = created_order.body.id

        

        # capture order
        collect = {
            "id": order_id,
            "prefer": "return=representation",
            "body": OrderCaptureRequest(
                payment_source=OrderCaptureRequestPaymentSource(
                    card=CardRequest(
                        name="John Doe",
                        number="4868719460707704",
                        expiry="2027-02",
                        billing_address=Address(
                            country_code="US",
                            address_line_1="2211 N First Street",
                            admin_area_2="San Jose",
                            admin_area_1="CA",
                            postal_code="95131",
                        ),
                        attributes=CardAttributes(
                            verification=CardVerification(
                                method=CardVerificationMethod.SCA_ALWAYS
                            )
                        ),
                        experience_context=CardExperienceContext(
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        ),
                    )
                )
            ),
        }

        try:
            captured_order = self.ordercontroller.orders_capture(collect)
        except ErrorException as e:
            links = e.links
            completion_link = links[0].href
            assert completion_link is not None

        # check status code
        assert self.order_response_catcher.response.status_code == 422

        assert self.flows.complete_helios_verification(completion_link, timeout=13000)

        

        # get order
        collect = {
            "id": order_id,
        }
        get_order = self.ordercontroller.orders_get(collect)

        # check status code
        assert get_order.status_code == 200

        assert get_order.body.payment_source is not None

        
        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        assert captured_order.body.status == "COMPLETED"

    # E2E test for payment method without purchase flow:
    # 1. Create a setup token
    # 2. Save the payment
    # 3. Create a payment token
    # 4. Get the setup token and check if the status is VAULTED
    # 5. Get the payment token and check if the status is completed
    def test_payment_method_without_purchase_flow(self):
        # create a random string
        random_string = str(random.randint(0, 100000))

        # create setup token
        collect = {
            "pay_pal_request_id": random_string,
            "body": SetupTokenRequest(
                payment_source=SetupTokenRequestPaymentSource(
                    paypal=VaultPayPalWalletRequest(
                        description="Description for PayPal to be shown to PayPal payer",
                        permit_multiple_payment_tokens=True,
                        usage_type="MERCHANT",
                        customer_type="CONSUMER",
                        experience_context=VaultExperienceContext(
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        ),
                    )
                )
            ),
        }
        setup_token = self.vaultcontroller.setup_tokens_create(collect)

        # check status code
        assert setup_token.status_code == 201

        setup_token_id = setup_token.body.id
        payer_action_link = setup_token.body.links[1].href

        assert setup_token_id is not None
        assert payer_action_link is not None

        # save payment
        assert self.flows.save_payment(payer_action_link)

        

        collect = {
            "pay_pal_request_id": random_string,
            "body": PaymentTokenRequest(
                payment_source=PaymentTokenRequestPaymentSource(
                    token=VaultTokenRequest(
                        id=setup_token_id, mtype=TokenRequestType.SETUP_TOKEN
                    )
                )
            ),
        }

        payment_token = self.vaultcontroller.payment_tokens_create(collect)

        # check status code
        assert payment_token.status_code == 201


        payment_token_id = payment_token.body.id

        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(currency_code="USD", value="10.00")
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(vault_id=payment_token_id)
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 201

        

        get_setup_token = self.vaultcontroller.setup_tokens_get(setup_token_id)

        # check status code
        assert get_setup_token.status_code == 200

        assert get_setup_token.body.status == "VAULTED"

        

        # get payment token

        get_payment_token = self.vaultcontroller.payment_tokens_get(payment_token_id)

        # check status code
        assert get_payment_token.status_code == 200

        assert get_payment_token.body is not None

    # E2E test for payment method with purchase flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Capture the order
    def test_payment_method_with_purchase_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="10.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="10.0"),
                                shipping=Money(currency_code="USD", value="0.0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Camera Shop",
                        items=[
                            Item(
                                name="Levis 501 Selvedge STF",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            ),
                            Item(
                                name="T-Shirt",
                                unit_amount=Money(currency_code="USD", value="5.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="1457432",
                            ),
                        ],
                        shipping=ShippingDetails(
                            address=Address(
                                country_code="US",
                                address_line_1="123 Main Street",
                                admin_area_2="San Jose",
                                admin_area_1="CA",
                                postal_code="95131",
                            )
                        ),
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        # create order
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        # complete payment
        confirm_order_link = created_order.body.links[1].href
        assert self.flows.complete_payment(confirm_order_link)

        

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        assert captured_order.body.status == "COMPLETED"

    # E2E test for add shipping information to order flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Capture the order
    # 4. Create tracking information
    # 5. Patch the tracker
    def test_add_shipping_information_to_order_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(currency_code="USD", value="100.00"),
                        reference_id="d9f80740-38f0-11e8-b467-0ed5f89f718b",
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        # complete payment
        confirm_order_link = created_order.body.links[1].href
        assert self.flows.complete_payment(confirm_order_link)

        

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        capture_id = captured_order.body.purchase_units[0].payments.captures[0].id

        assert capture_id is not None

        

        # create tracking information
        collect = {
            "id": order_id,
            "body": OrderTrackerRequest(
                capture_id=capture_id,
                tracking_number="443844607820",
                carrier=ShipmentCarrier.FEDEX,
                notify_payer=False,
                items=[
                    OrderTrackerItem(
                        name="T-Shirt",
                        quantity="1",
                        sku="sku02",
                        url="https://www.example.com/example",
                        image_url="https://www.example.com/example.jpg",
                        upc=UniversalProductCode(mtype=UPCType.UPCA, code="upc001"),
                    )
                ],
            ),
        }

        shipping_order = self.ordercontroller.orders_track_create(collect)

        # check status code
        assert shipping_order.status_code == 201

        tracker_id = shipping_order.body.purchase_units[0].shipping.trackers[0].id

        assert tracker_id is not None
        

        collect = {
            "id": order_id,
            "tracker_id": tracker_id,
            "body": [
                Patch(
                    op=PatchOp.REPLACE,
                    path="/notify_payer",
                    value=jsonpickle.decode("true"),
                )
            ],
        }

        patch_track_order = self.ordercontroller.orders_trackers_patch(collect)

        # check status code
        assert patch_track_order.status_code == 204

    def test_confirm_order_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(currency_code="USD", value="100.00"),
                        reference_id="d9f80740-38f0-11e8-b467-0ed5f89f718b",
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        # create order
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        

        # confirm order
        collect = {
            "id": order_id,
            "prefer": "return=representation",
            "body": ConfirmOrderRequest(
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        email_address="customer@example.com",
                        name=Name(given_name="John", surname="Doe"),
                        experience_context=PayPalWalletExperienceContext(
                            brand_name="EXAMPLE INC",
                            locale="en-US",
                            shipping_preference=ShippingPreference.SET_PROVIDED_ADDRESS,
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                            user_action=PayPalExperienceUserAction.PAY_NOW,
                            payment_method_preference=PayeePaymentMethodPreference.IMMEDIATE_PAYMENT_REQUIRED,
                        ),
                    )
                )
            ),
        }

        confirmed_order = self.ordercontroller.orders_confirm(collect)

        # check status code
        assert confirmed_order.status_code == 200

        payer_action_link = confirmed_order.body.links[1].href

        # complete payment
        assert self.flows.complete_payment(payer_action_link)

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        assert captured_order.body.status == "COMPLETED"

    # E2E test for authorize and capture flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Authorize the order
    # 4. Capture the authorization
    def test_authorize_and_capture_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.AUTHORIZE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="25.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="25.00"),
                                shipping=Money(currency_code="USD", value="0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Clothing Shop",
                        items=[
                            Item(
                                name="Levis 501",
                                unit_amount=Money(currency_code="USD", value="25.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            )
                        ],
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        # create order
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        # complete payment
        confirm_order_link = created_order.body.links[1].href
        assert self.flows.complete_payment(confirm_order_link)

        

        # authorize order
        collect = {"id": order_id, "prefer": "return=representation"}

        authorized_order = self.ordercontroller.orders_authorize(collect)

        # check status code
        assert authorized_order.status_code == 201

        authorization_id = (
            authorized_order.body.purchase_units[0].payments.authorizations[0].id
        )

        

        # capture authorization

        collect = {
            "authorization_id": authorization_id,
            "prefer": "return=representation",
        }

        captured_order = self.paymentcontroller.authorizations_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        capture_id = captured_order.body.id

        assert capture_id is not None

        

        # get authorization
        get_authorization = self.paymentcontroller.authorizations_get(authorization_id)

        # check status code
        assert get_authorization.status_code == 200

        assert get_authorization.body.status == "CAPTURED"

        

        # get capture
        get_captures = self.paymentcontroller.captures_get(capture_id)

        # check status code
        assert get_captures.status_code == 200

        assert get_captures.body.status == "COMPLETED"

    # E2E test for standard checkout flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Capture the order
    def test_standard_checkout_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.CAPTURE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="25.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="25.00"),
                                shipping=Money(currency_code="USD", value="0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Clothing Shop",
                        items=[
                            Item(
                                name="Levis 501",
                                unit_amount=Money(currency_code="USD", value="25.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            )
                        ],
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        # create order
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        # complete payment
        confirm_order_link = created_order.body.links[1].href
        assert self.flows.complete_payment(confirm_order_link)

        

        # capture order
        collect = {"id": order_id, "prefer": "return=representation"}

        captured_order = self.ordercontroller.orders_capture(collect)

        # check status code
        assert captured_order.status_code == 201

        assert captured_order.body.status == "COMPLETED"

        

        # get order
        collect = {
            "id": order_id,
        }

        get_order = self.ordercontroller.orders_get(collect)

        # check status code
        assert get_order.status_code == 200

        assert get_order.body.status == "COMPLETED"

    # E2E test for void capture flow:
    # 1. Create an order
    # 2. Complete the payment
    # 3. Authorize the order
    # 4. Void the authorization
    def test_void_capture_flow(self):
        random_string = str(random.randint(0, 100000))
        collect = {
            "body": OrderRequest(
                intent=CheckoutPaymentIntent.AUTHORIZE,
                purchase_units=[
                    PurchaseUnitRequest(
                        amount=AmountWithBreakdown(
                            currency_code="USD",
                            value="25.00",
                            breakdown=AmountBreakdown(
                                item_total=Money(currency_code="USD", value="25.00"),
                                shipping=Money(currency_code="USD", value="0"),
                                tax_total=Money(currency_code="USD", value="0"),
                            ),
                        ),
                        description="Clothing Shop",
                        items=[
                            Item(
                                name="Levis 501",
                                unit_amount=Money(currency_code="USD", value="25.00"),
                                quantity="1",
                                tax=Money(currency_code="USD", value="0.00"),
                                sku="5158936",
                            )
                        ],
                    )
                ],
                payment_source=PaymentSource(
                    paypal=PayPalWallet(
                        experience_context=PayPalWalletExperienceContext(
                            locale="en-US",
                            return_url="https://example.com/returnUrl",
                            cancel_url="https://example.com/cancelUrl",
                            landing_page=PayPalExperienceLandingPage.LOGIN,
                        )
                    )
                ),
            ),
            "pay_pal_request_id": random_string,
            "pay_pal_partner_attribution_id": "PayPal-Partner-Attribution-Id",
            "pay_pal_client_metadata_id": "PayPal-Client-Metadata-Id",
            "prefer": "return=representation",
        }

        # create order
        created_order = self.ordercontroller.orders_create(collect)

        # check status code
        assert created_order.status_code == 200

        order_id = created_order.body.id

        assert order_id is not None

        # complete payment
        confirm_order_link = created_order.body.links[1].href
        assert self.flows.complete_payment(confirm_order_link)

        

        # authorize order
        collect = {"id": order_id, "prefer": "return=representation"}

        authorized_order = self.ordercontroller.orders_authorize(collect)

        # check status code
        assert authorized_order.status_code == 201

        authorization_id = (
            authorized_order.body.purchase_units[0].payments.authorizations[0].id
        )

        

        # void authorization
        collect = {
            "authorization_id": authorization_id,
            "prefer": "return=representation",
        }

        void_authorization = self.paymentcontroller.authorizations_void(collect)

        # check status code
        assert void_authorization.status_code == 200
