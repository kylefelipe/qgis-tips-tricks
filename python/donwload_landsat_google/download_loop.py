# -*- coding: utf-8 -*-
"""Baixar imagem landsat 578"""

from landsat.google_download import GoogleDownload

path_row = [('218', '72'), ('218', '73'), ('218', '74'), ('218', '75')]
data_inicial = '2017-01-01'
data_final = '2017-02-02'
cloud = 10
image_folder = "/exercicios/baixando_imagem"
satellite_n = 8


def download_image(start_date, end_date, sat, img_path, img_row,  max_cloud,
                   folder):
    """Baixar a imagem do repo do google."""
    g = GoogleDownload(start=start_date, end=end_date, satellite=sat,
                       path=img_path, row=img_row, output_path=folder,
                       max_cloud_percent=float(max_cloud))
    g.download()


for i in path_row:
    download_image(data_inicial, data_final, satellite_n, i[0], i[1], cloud)
