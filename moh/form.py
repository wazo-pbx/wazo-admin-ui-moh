# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import TextField
from wtforms.fields import SelectField

from wtforms.validators import InputRequired


class MohForm(FlaskForm):
    name = TextField('Name', [InputRequired()])
    mode = SelectField('Mode',
                       choices = [
                           ('custom', 'Custom'),
                           ('files', 'Files'),
                           ('mp3', 'MP3')
                       ])
    submit = SubmitField('Submit')
