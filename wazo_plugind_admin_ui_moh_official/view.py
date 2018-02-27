# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import cgi

from io import BytesIO

from flask import jsonify, request, send_file, redirect, flash, url_for
from flask_babel import lazy_gettext as l_
from flask_classful import route
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import MohForm


class MohView(BaseView):

    form = MohForm
    resource = 'moh'

    @classy_menu_item('.moh', l_('Musics'), order=6, icon='music')
    def index(self):
        return super(MohView, self).index()

    def download_filename(self, uuid, moh_filename):
        response = self.service.download_filename(uuid, moh_filename)
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            _, params = cgi.parse_header(content_disposition)
            if params:
                moh_filename = params['filename']

        return send_file(
            BytesIO(response.content),
            attachment_filename=moh_filename,
            as_attachment=True,
            mimetype=response.headers.get('content-type')
        )

    def delete_filename(self, uuid, moh_filename):
        self.service.delete_filename(uuid, moh_filename)
        return redirect(url_for('.{}:{}'.format(self.__class__.__name__,
                                                'get'), id=uuid))

    @route('/upload_filename/<uuid>', methods=['POST'])
    def upload_filename(self, uuid):
        if 'moh_filename' not in request.files:
            flash('[upload] Upload attempt with no file', 'error')
            return redirect(url_for('.{}:{}'.format(self.__class__.__name__,
                                                    'get'), id=uuid))

        file = request.files.get('moh_filename')

        self.service.upload_filename(uuid, file.filename, file.read())

        return redirect(url_for('.{}:{}'.format(self.__class__.__name__,
                                                'get'), id=uuid))

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('moh', {}))
        return form


class MohListingView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        musiconhold = self.service.list(**params)
        results = [{'id': moh['name'], 'text': moh['name']} for moh in musiconhold['items']]
        return jsonify(build_select2_response(results, musiconhold['total'], params))
