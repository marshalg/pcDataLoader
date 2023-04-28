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

    def test_mcds_get_xmlfile_list(self, mcds=mcds):
        ls_xmlfile = mcds.get_xmlfile_list()
        assert len(ls_xmlfile) == 25

    def test_mcds_get_xmlfile_list_read_mcds(self, mcds=mcds):
        ls_xmlfile = mcds.get_xmlfile_list()
        ls_xmlfile = ls_xmlfile[-3:]
        ls_mcds = mcds.read_mcds(ls_xmlfile)
        assert len(ls_xmlfile) == 3 and \
               len(ls_mcds) == 3 and \
               ls_mcds[2].get_time() == 1440

    def test_mcds_read_mcds(self, mcds=mcds):
        ls_mcds = mcds.read_mcds()
        assert len(ls_mcds) == 25 and \
               ls_mcds[-1].get_time() == 1440