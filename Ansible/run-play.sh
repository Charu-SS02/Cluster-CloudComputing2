#!/bin/bash

. ./unimelb-comp90024-2020-grp-26-openrc.sh; ansible-playbook --ask-become-pass playbook.yml -i inventory/hosts.ini