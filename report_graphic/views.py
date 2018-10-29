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
    # maptype=u"新疆",
    is_geo_effect_show=False,
    geo_normal_color="#BDD3C6"
    # legend_selectedmode="single"
)

def generate_html():
    data_urumchi = [
        [u"乌鲁木齐", u"吐鲁番"],
        [u"乌鲁木齐", u"库尔勒"],
        [u"乌鲁木齐", u"哈密"],
        [u"乌鲁木齐", u"和田"],
        [u"乌鲁木齐", u"喀什"],
        [u"乌鲁木齐", u"阿克苏"]
    ]
    data_turpan = [
        [u"吐鲁番", u"乌鲁木齐"],
    ]
    geolines = GeoLines(u"例子", **style.init_style)
    geolines.add(u"depart1", data_urumchi, **style_geo)
    geolines.add(u"depart2", data_turpan, **style_geo)
    geolines.render()

if __name__ == "__main__":
    generate_html()
