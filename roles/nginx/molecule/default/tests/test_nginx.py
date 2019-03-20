import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_user(host):
    user = host.user('www-data')

    assert user.exists
    assert user.group == 'www-data'
    assert user.shell == '/usr/sbin/nologin'
    assert user.home == '/var/www'


def test_http_port(host):
    port = host.socket('tcp://0.0.0.0:80')

    assert port.is_listening


def test_nginx_service(host):
    service = host.service('nginx')

    assert service.is_enabled
    assert service.is_running
