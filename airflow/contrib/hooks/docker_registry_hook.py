# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from airflow.hooks.base_hook import BaseHook


class DockerRegistryHook(BaseHook):
    """
    Authenticate against a docker registry.
    This class is a thin wrapper around the docker-py python library.
    """
    def __init__(self, docker_registry_conn_id='docker_registry_default'):
        self.docker_registry_conn_id = docker_registry_conn_id

    def login(self, client):
        connection_object = self.get_connection(self.aws_conn_id)
        username = connection_object.login
        password = connection_object.password
        registry = connection_object.hostname

        client.login(username=username,
                     password=password,
                     registry=registry,
                     reauth=True)

        return client
