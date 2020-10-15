# -*- coding: utf8 -*-
# ============LICENSE_START=======================================================
# org.onap.vvp/validation-scripts
# ===================================================================
# Copyright © 2020 AT&T Intellectual Property. All rights reserved.
# ===================================================================
#
# Unless otherwise specified, all software contained herein is licensed
# under the Apache License, Version 2.0 (the "License");
# you may not use this software except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
# Unless otherwise specified, all documentation contained herein is licensed
# under the Creative Commons License, Attribution 4.0 Intl. (the "License");
# you may not use this documentation except in compliance with the License.
# You may obtain a copy of the License at
#
#             https://creativecommons.org/licenses/by/4.0/
#
# Unless required by applicable law or agreed to in writing, documentation
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ============LICENSE_END============================================
import uuid
from functools import partial

from onap_client.aai.client import AAIClient


class CloudInfrastructureClient(AAIClient):
    @property
    def namespace(self):
        return "cloud_infrastructure"

    @property
    def catalog_resources(self):
        return {
            "GET_CLOUD_REGIONS": {
                "verb": "GET",
                "description": "Queries AAI for all cloud regions",
                "uri": partial(
                    "{endpoint}{service_path}/cloud-regions".format,
                    endpoint=self.config.aai.AAI_BE_ENDPOINT,
                    service_path=self.config.aai.AAI_CLOUD_INFRASTRUCTURE_PATH,
                ),
                "success_code": 200,
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-TransactionId": str(uuid.uuid4()),
                    "X-FromAppId": self.config.application_id,
                },
                "auth": self.auth,
            },
            "GET_CLOUD_REGION": {
                "verb": "GET",
                "description": "Queries AAI for a cloud region",
                "uri": partial(
                    "{endpoint}{service_path}/cloud-regions/cloud-region/{cloud_owner}/{cloud_region}".format,
                    endpoint=self.config.aai.AAI_BE_ENDPOINT,
                    service_path=self.config.aai.AAI_CLOUD_INFRASTRUCTURE_PATH,
                ),
                "uri-parameters": ["cloud_region", "cloud_owner"],
                "success_code": 200,
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-TransactionId": str(uuid.uuid4()),
                    "X-FromAppId": self.config.application_id,
                },
                "auth": self.auth,
            },
            "GET_CLOUD_REGION_TENANTS": {
                "verb": "GET",
                "description": "Queries AAI for a cloud region's tenants",
                "uri": partial(
                    "{endpoint}{service_path}/cloud-regions/cloud-region/{cloud_owner}/{cloud_region}/tenants".format,
                    endpoint=self.config.aai.AAI_BE_ENDPOINT,
                    service_path=self.config.aai.AAI_CLOUD_INFRASTRUCTURE_PATH,
                ),
                "uri-parameters": ["cloud_region", "cloud_owner"],
                "success_code": 200,
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-TransactionId": str(uuid.uuid4()),
                    "X-FromAppId": self.config.application_id,
                },
                "auth": self.auth,
            },
            "GET_ESR_LIST": {
                "verb": "GET",
                "description": "Queries AAI for a esr info",
                "uri": partial(
                    "{endpoint}{service_path}/cloud-regions/cloud-region/{cloud_owner}/{cloud_region}/esr-system-info-list".format,
                    endpoint=self.config.aai.AAI_BE_ENDPOINT,
                    service_path=self.config.aai.AAI_CLOUD_INFRASTRUCTURE_PATH,
                ),
                "uri-parameters": ["cloud_region", "cloud_owner"],
                "success_code": 200,
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-TransactionId": str(uuid.uuid4()),
                    "X-FromAppId": self.config.application_id,
                },
                "auth": self.auth,
            },
            "GET_VOLUME_GROUPS": {
                "verb": "GET",
                "description": "Queries AAI for the list of volume groups",
                "uri": partial(
                    "{endpoint}{service_path}/cloud-regions/cloud-region/{cloud_owner}/{cloud_region}/volume-groups".format,
                    endpoint=self.config.aai.AAI_BE_ENDPOINT,
                    service_path=self.config.aai.AAI_CLOUD_INFRASTRUCTURE_PATH,
                ),
                "uri-parameters": ["cloud_region", "cloud_owner"],
                "success_code": 200,
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-TransactionId": str(uuid.uuid4()),
                    "X-FromAppId": self.config.application_id,
                },
                "auth": self.auth,
            },
        }
