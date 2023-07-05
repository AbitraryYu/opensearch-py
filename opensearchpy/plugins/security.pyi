# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
from typing import Any, Union

from ..client.utils import NamespacedClient as NamespacedClient

class SecurityClient(NamespacedClient):
    def get_account_details(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def change_password(
        self,
        current_password: Any,
        current_papasswordssword: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_action_group(
        self,
        action_group: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_action_groups(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def delete_action_group(
        self,
        action_group: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def put_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_action_groups(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_user(
        self,
        username: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_users(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def delete_user(
        self,
        username: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def put_user(
        self,
        username: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_user(
        self,
        username: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_users(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_role(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_roles(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def delete_role(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def put_role(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_role(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_roles(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_role_mapping(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_role_mappings(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def delete_role_mappings(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def put_role_mappings(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_role_mapping(
        self, role: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_role_mappings(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_tenant(
        self,
        tenant: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_tenants(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def delete_tenant(
        self,
        tenant: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def put_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def patch_tenants(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_configuration(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def put_configuration(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_configuration(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_distinguished_names(
        self,
        cluster_name: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def put_distinguished_names(
        self,
        cluster_name: Any,
        body: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def delete_distinguished_names(
        self,
        cluster_name: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_certificates(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def reload_transport_certificates(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def reload_http_certificates(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def flush_cache(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def health_check(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_audit_configuration(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def put_audit_configuration(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def patch_audit_configuration(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...