# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from keystone.common.policies import base

service_provider_policies = [
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'create_service_provider',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Create federated service provider.',
        operations=[{'path': ('/v3/OS-FEDERATION/service_providers/'
                              '{service_provider_id}'),
                     'method': 'PUT'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'list_service_providers',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='List federated service providers.',
        operations=[{'path': '/v3/OS-FEDERATION/service_providers',
                     'method': 'GET'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_service_provider',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Get federated service provider.',
        operations=[{'path': ('/v3/OS-FEDERATION/service_providers/'
                              '{service_provider_id}'),
                     'method': 'GET'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'update_service_provider',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Update federated service provider.',
        operations=[{'path': ('/v3/OS-FEDERATION/service_providers/'
                              '{service_provider_id}'),
                     'method': 'PATCH'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'delete_service_provider',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Delete federated service provider.',
        operations=[{'path': ('/v3/OS-FEDERATION/service_providers/'
                              '{service_provider_id}'),
                     'method': 'DELETE'}])
]


def list_rules():
    return service_provider_policies
