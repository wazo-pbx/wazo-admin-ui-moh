# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import MohService
from .view import MohView

moh = create_blueprint('moh', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        MohView.service = MohService(config['confd'])
        MohView.register(moh, route_base='/moh')
        register_flaskview(moh, MohView)

        core.register_blueprint(moh)
