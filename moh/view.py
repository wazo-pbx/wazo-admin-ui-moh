# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import MohForm


class MohSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(MohForm)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'moh'

    moh = fields.Nested(MohSchema)


class MohView(BaseView):

    form = MohForm
    resource = 'moh'
    schema = AggregatorSchema

    @classy_menu_item('.moh', 'MusicOnHold', order=6, icon="music")
    def index(self):
        return super(MohView, self).index()



class MohListingView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        musiconhold = self.service.list(**params)
        results = [{'id': moh['name'], 'text': moh['name']} for moh in musiconhold['items']]
        return jsonify(build_select2_response(results, musiconhold['total'], params))
