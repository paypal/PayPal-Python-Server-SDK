
import os
import unittest
from dotenv import load_dotenv
from paypalserversdk.configuration import Configuration
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.paypalserversdk_client import PaypalserversdkClient
from tests.http_response_catcher import HttpResponseCatcher


class E2ETestBase(unittest.TestCase):

    """E2E Tests Class inherits from this class. It abstracts out
    common functionality and configuration variables set up."""

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = E2ETestBase.create_configuration()
        cls.client = PaypalserversdkClient(config=cls.config)

    @staticmethod
    def create_configuration():
        ## Load the environment variables
        load_dotenv()
        o_auth_client_id = os.getenv("CLIENT_ID")
        o_auth_client_secret = os.getenv("CLIENT_SECRET")
        client_credentials_auth_credentials = ClientCredentialsAuthCredentials(
        o_auth_client_id= o_auth_client_id,
        o_auth_client_secret= o_auth_client_secret
    )
        return Configuration(http_call_back=HttpResponseCatcher() , client_credentials_auth_credentials=client_credentials_auth_credentials)