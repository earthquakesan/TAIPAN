import unittest
import numpy as np

from taipan.T2D.Sampler import T2DSampler
from taipan.T2D.Table import T2DTable
from taipan.Learning.SubjectColumnIdentification.SimpleIdentifier import SimpleIdentifier
from taipan.Learning.SubjectColumnIdentification.ConnectivityIdentifier import ConnectivityIdentifier

from taipan.Logging.Logger import Logger

class ConnectivityIdentifierTestCase(unittest.TestCase):
    def setUp(self):
        sampler = T2DSampler()
        self.testTable = sampler.getTestTable()
        self.scIdentifier = ConnectivityIdentifier()
        #self.testTables = sampler.getTablesSubjectIdentificationGoldStandard()
        self.testTables = sampler.getTablesDbpediaWhitelistDataset()

    def testConnectivityIdentifier(self):
        """
            0.409836065574
        """
        connectivityCeil = 0.32
        connectivityFloors = np.arange(0,1.0,0.1)
        for connectivityFloor in connectivityFloors:
            correctly = 0
            for table in self.testTables:
                subjectColumn = self.scIdentifier.identifySubjectColumn(table, applyWeights=False, connectivityFloor=connectivityFloor, connectivityCeil=connectivityCeil)
                if table.isSubjectColumn(subjectColumn):
                    correctly += 1
            print "connectivity floor: %s" % connectivityFloor
            print "connectivity ceil: %s" % connectivityCeil
            print correctly
            print float(correctly) / len(self.testTables)
