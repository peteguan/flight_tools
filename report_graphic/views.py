# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from pyecharts import GeoLines, Style
from django.http import HttpResponse
from django.template import loader

import sys
reload(sys)
sys.setdefaultencoding('utf8')

style = Style(
    title_top="#fff",
    title_pos="center",
    width=1600,
    height=800,
    background_color="#58FAF4",
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0,
    line_opacity=0.6,
    legend_text_color="#ff",
    legend_pos="right",
    label_color=['#910000', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#",
    symbol=[None,None],
    maptype=u"中国",
    is_geo_effect_show=False,
    geo_normal_color="#BDD3C6"
    # legend_selectedmode="single"
)



