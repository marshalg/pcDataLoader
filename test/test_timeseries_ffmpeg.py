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

# const
s_path_2d = str(pathlib.Path(pc.__file__).parent.resolve()/'data_timeseries_2d')

# load physicell data time series
class TestPyMcdsTs(object):
    ''' test for pc.pyMCDSts data loader. '''
    mcds = pc.pyMCDSts(s_path_2d, verbose=False)

    ### ffmpeg command ###
    def test_ffmpeg(self):
        b_ok = (os.system('ffmpeg -version') == 0)
        if not b_ok:
            print('Warning @ pcDataLoader : ffmpeg is not installed!')
        assert b_ok

    ## making movies with jpeg as interface ##
    def test_mcds_make_movie_jpeg(self, mcds=mcds):
        # generate jpeg interface images
        mcds.make_imgcell()
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        # generate movie
        s_movieout = mcds.make_movie(path=s_path)
        assert os.path.exists(s_movieout) and (os.path.getsize(s_movieout) > 0)
        # clean up
        os.remove(s_movieout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.jpeg'):
                os.remove(f'{s_path}/{s_file}')

    ## making movies with png as interface ##
    def test_mcds_make_movie_png(self, mcds=mcds):
        # generate jpeg interface images
        mcds.make_imgcell(ext='png')
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        # generate movie
        s_movieout = mcds.make_movie(path=s_path, interface='png')
        assert os.path.exists(s_movieout) and (os.path.getsize(s_movieout) > 0)
        # clean up
        os.remove(s_movieout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.png'):
                os.remove(f'{s_path}/{s_file}')

    ## making movies with tiff as interface ##
    def test_mcds_make_movie_tiff(self, mcds=mcds):
        # generate jpeg interface images
        mcds.make_imgcell(ext='tiff')
        s_path = f'{s_path_2d}/cell_cell_type_z0'
        # generate movie
        s_movieout = mcds.make_movie(path=s_path, interface='tiff')
        assert os.path.exists(s_movieout) and (os.path.getsize(s_movieout) > 0)
        # clean up
        os.remove(s_movieout)
        for s_file in os.listdir(s_path):
            if s_file.endswith('.tiff'):
                os.remove(f'{s_path}/{s_file}')
        os.rmdir(s_path)