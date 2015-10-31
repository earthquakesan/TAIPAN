from taipan.Learning.SubjectColumnIdentification.SVM.Features.FeatureInterface import FeatureInterface

class CellsWithUniqueContentFraction(FeatureInterface):
    def calculate(self, column, columnIndex, table):
        return float(len(set(column))) / len(column)
