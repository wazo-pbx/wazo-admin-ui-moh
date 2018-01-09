# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            FieldList,
                            FormField)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.form import BaseForm


class MohFilesForm(BaseForm):
    name = StringField(l_('Name'), [InputRequired()])


class MohForm(BaseForm):
    name = StringField(l_('Name'), [InputRequired()], description=l_('The name used by Asterisk (can only by set on create and must be unique)'))
    label = StringField(l_('Label'), description=l_('The label of the MOH class'))
    mode = SelectField(l_('Mode'),
                       choices=[
                           ('custom', l_('Custom')),
                           ('files', l_('Files')),
                           ('mp3', l_('MP3'))
                       ],
                       description=l_("The play mode of the MOH class = ['custom', 'files', 'mp3']"))
    application = StringField(l_('Application'), description=l_('The command to run (only used when mode is "custom")'))
    sort = SelectField(l_('Sort'),
                       choices=[
                           ('alphabetical', l_('Alphabetical')),
                           ('random', l_('Random')),
                           ('random_start', l_('Random start')),
                       ],
                       description=l_("The order in which files are played (only used when mode is 'files') = ['alphabetical', 'random', 'random_start']"))
    files = FieldList(FormField(MohFilesForm))
    submit = SubmitField(l_('Submit'))
