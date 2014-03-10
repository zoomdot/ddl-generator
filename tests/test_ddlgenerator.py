"""
test_ddlgenerator
----------------------------------

Tests for `ddlgenerator` module.
"""

import glob
import sys
import unittest
try:
    from ddlgenerator.ddlgenerator import Table
except ImportError:
    from ddlgenerator import Table

class TestFiles(unittest.TestCase):
    
    def test_files(self):
        for sql_fname in glob.glob('*.sql'):
            (fname, ext) = sql_fname.split('.')
            with open(sql_fname) as infile:
                expected = infile.read().strip()
            for source_fname in glob.glob('%s.*' % fname):
                (fname, ext) = source_fname.split('.')
                if ext != 'sql':
                    tbl = Table(source_fname)
                    generated = tbl.sql('postgresql', inserts=True)
                    self.assertEqual(generated.strip(), expected.strip())
            
if __name__ == '__main__':
    unittest.main()