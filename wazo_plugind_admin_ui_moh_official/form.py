# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import SubmitField
from wtforms.fields import StringField
from wtforms.fields import SelectField
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.form import BaseForm


class MohForm(BaseForm):
    name = StringField('Name', [InputRequired()])
    mode = SelectField('Mode',
                       choices=[
                           ('custom', 'Custom'),
                           ('files', 'Files'),
                           ('mp3', 'MP3')
                       ])
    submit = SubmitField('Submit')
