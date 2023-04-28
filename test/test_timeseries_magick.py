####
# title: test_timeseries.py
#
# language: python3
# author: bue
# date: 2022-10-15
# license: BSD 3-Clause
#
# description:
#   pytest unit test library for heat.py
#   + https://docs.pytest.org/
#
#   note:
#   assert actual == expected, message
#   == value equality
#   is reference equality
#   pytest.approx for real values
#####

# load library
import os
import pathlib

import sys
sys.path.append('..')

import pcDataLoader as pc
import platform

# const
s_path_2d = str(pathlib.Path(pc.__file__).parent.resolve()/'data_timeseries_2d')

# load physicell data time series
class TestPyMcdsTs(object):
    ''' test for pc.pyMCDSts data loader. '''
    mcds = pc.pyMCDSts(s_path_2d, verbose=False)

    ## magick command ##
    def test_mcds_handle_magick(self, mcds=mcds):
        s_magick = mcds._handle_magick()
        if not((os.system('magick --version') == 0) or ((platform.system() in {'Linux'}) and (os.system('convert --version') == 0))):
            s_magick = None
            print('Error @ pyMCDSts._handle_magick : image magick installation version >= 7.0 missing!')
        assert s_magick in {'', 'magick '}

    ## make_imgcell jpeg ##
    def test_mcds_make_imgcell_jpeg(self, mcds=mcds):
        s_path = mcds.make_imgcell()
        assert os.path.exists(s_path)

    ## make_gif jpeg ##
    def test_mcds_make_gif_jpeg(self, mcds=mcds):
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        s_gifout = mcds.make_gif(s_path) # make gif with jpegs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.jpeg'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)
        
    ## make_imgcell png ##
    def test_mcds_make_imgcell_png(self, mcds=mcds):
        s_path = mcds.make_imgcell(ext='png')
        assert os.path.exists(s_path)

    ## make_gif png ##
    def test_mcds_make_gif_png(self, mcds=mcds):
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        s_gifout = mcds.make_gif(s_path, interface='png') # make gif with pngs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.png'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)

    ## make_imgcell tiff ##
    def test_mcds_make_imgcell_tiff(self, mcds=mcds):
        s_path = mcds.make_imgcell(ext='tiff')
        assert os.path.exists(s_path)

    ## make_gif tiff ##
    def test_mcds_make_gif_tiff(self, mcds=mcds):
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        s_gifout = mcds.make_gif(s_path, interface='tiff') # make gif with tiffs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.tiff'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)
        os.rmdir(s_path)

    ## make_imgsubs jpeg ##
    def test_mcds_make_imgsubs_jpeg(self, mcds=mcds):
        s_path = mcds.make_imgsubs(focus='oxygen')
        assert os.path.exists(s_path)

    ## make_gif substrate jpeg ##
    def test_mcds_make_gif_subs_jpeg(self, mcds=mcds):
        s_path = f'{s_path_2d}/substrate_oxygen_z0'
        s_gifout = mcds.make_gif(s_path) # make gif with jpegs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.jpeg'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)

    ## make_imgsubs png ##
    def test_mcds_make_imgsubs_png(self, mcds=mcds):
        s_path = mcds.make_imgsubs(focus='oxygen', ext='png')
        assert os.path.exists(s_path)

    ## make_gif substrate png ##
    def test_mcds_make_gif_subs_png(self, mcds=mcds):
        s_path = f'{s_path_2d}/substrate_oxygen_z0'
        s_gifout = mcds.make_gif(s_path, interface='png') # make gif with pngs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.png'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)

    ## make_imgsubs tiff ##
    def test_mcds_make_imgsubs_tiff(self, mcds=mcds):
        s_path = mcds.make_imgsubs(focus='oxygen', ext='tiff')
        assert os.path.exists(s_path)

    ## make_gif substrate tiff ##
    def test_mcds_make_gif_subs_tiff(self, mcds=mcds):
        s_path = f'{s_path_2d}/substrate_oxygen_z0'
        s_gifout = mcds.make_gif(s_path, interface='tiff') # make gif with tiffs
        
        assert os.path.exists(s_gifout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.tiff'):
                os.remove(f'{s_path}/{s_file}')
        os.remove(s_gifout)
        os.rmdir(s_path)