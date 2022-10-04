#!/usr/bin/python
# -*- coding: utf-8 -*-
from excel.execel_utils import write, ExcelModel, ExcelData, ExcelConfig, read
from data_source import properties_loader, mysql_utils as db


def __replace_head_name(head_list, dic: dict):
    for i in range(len(head_list)):
        if head_list[i] in dic.keys():
            head_list[i] = dic.get(head_list[i])


def get_excel_config(config_dic):
    # file_path, sheet_name, cover, header_font, header_bold, body_font
    return ExcelConfig(config_dic['fileName'] + '.xlsx', config_dic['sheetName'], 'true' == config_dic['cover'].lower(),
                       int(config_dic['header_font']), 'true' == config_dic['header_font'].lower(),
                       int(config_dic['body_font']), 'true' == config_dic['header_horizontal'].lower(),
                       'true' == config_dic['body_horizontal'].lower(), 'true' == config_dic['border'].lower())


def export_data():
    # 执行sql
    config_dic = properties_loader.load('excel.properties')
    result = db.query(config_dic['sql'])
    config = get_excel_config(config_dic)
    # 处理结果
    name_map = properties_loader.load('bean-map.properties')
    __replace_head_name(head_list=result['headers'], dic=name_map)
    # 写入excel
    data = ExcelData(result['headers'], result['rows'])
    excel_model = ExcelModel(config,
                             excel_data=data)
    write(excel_model)
