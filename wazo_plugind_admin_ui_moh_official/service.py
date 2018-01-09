# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class MohService(BaseConfdService):

    resource_confd = 'moh'

    def download_filename(self, uuid, moh_filename):
        return confd.moh.download_file(uuid, moh_filename)

    def delete_filename(self, uuid, moh_filename):
        return confd.moh.delete_file(uuid, moh_filename)

    def upload_filename(self, uuid, moh_filename, binary_content):
        return confd.moh.upload_file(uuid, moh_filename, binary_content)
