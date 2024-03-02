# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import lakefs_sdk
from lakefs_sdk.models.repository_creation import RepositoryCreation  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestRepositoryCreation(unittest.TestCase):
    """RepositoryCreation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryCreation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryCreation`
        """
        model = lakefs_sdk.models.repository_creation.RepositoryCreation()  # noqa: E501
        if include_optional :
            return RepositoryCreation(
                name = 'wr1c2v7s6djuy1zmeto', 
                storage_namespace = 's3://example-bucket/', 
                default_branch = 'main', 
                sample_data = True, 
                read_only = True
            )
        else :
            return RepositoryCreation(
                name = 'wr1c2v7s6djuy1zmeto',
                storage_namespace = 's3://example-bucket/',
        )
        """

    def testRepositoryCreation(self):
        """Test RepositoryCreation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
