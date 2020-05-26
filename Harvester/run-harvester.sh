#!/bin/bash

. ./unimelb-comp90024-2020-grp-26-openrc.sh; ansible-playbook -u ubuntu --ask-become-pass --key-file=Hina-Key.pem -i hosts.ini harvester.yaml