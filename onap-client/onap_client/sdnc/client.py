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
from frozendict import frozendict
from onap_client.client.clients import Client
from onap_client.auth import auth_handler


class SDNCClient(Client):
    @property
    def namespace(self):
        return "sdnc"

    @property
    def catalog_resources(self):
        return {}

    @property
    def sdnc_username(self):
        """Username to authenticate to SDNC"""
        return self.config.sdnc.SDNC_USERNAME

    @property
    def sdnc_password(self):
        """Password to authenticate to SDNC"""
        return self.config.sdnc.SDNC_PASSWORD

    @property
    def auth(self):
        return auth_handler(
            frozendict(self.config.sdnc.AUTH_PLUGIN) if self.config.sdnc.AUTH_PLUGIN else None,
            self.sdnc_username,
            self.sdnc_password,
        )
