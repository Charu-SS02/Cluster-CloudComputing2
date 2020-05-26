#!/bin/bash

. ./unimelb-comp90024-2020-grp-26-openrc.sh; ansible-playbook --ask-become-pass open-ports.yml -i inventory/hosts.ini