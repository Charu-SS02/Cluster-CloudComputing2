#!/bin/bash

export ANSIBLE_HOST_KEY_CHECKING=False
. ./unimelb-comp90024-2020-grp-26-openrc.sh; ansible-playbook --ask-become-pass playbook.yml -i inventory/hosts.ini
