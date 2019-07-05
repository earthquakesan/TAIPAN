from .CellsWithUniqueContentFraction import CellsWithUniqueContentFraction
from .CellsWithNumericContentFraction import CellsWithNumericContentFraction
from .NumberOfWordsAverage import NumberOfWordsAverage
from .NumberOfDigitsAverage import NumberOfDigitsAverage
from .NumberOfLettersAverage import NumberOfLettersAverage
from .Connectivity import Connectivity
from .Support import Support
from .VarianceInDateTokens import VarianceInDateTokens

#FeatureList = [CellsWithUniqueContentFraction(), CellsWithNumericContentFraction(), NumberOfWordsAverage(), NumberOfDigitsAverage(), NumberOfLettersAverage(), Connectivity(), Support(), VarianceInDateTokens()]

#Original (SVM-O)
#FeatureList = [CellsWithUniqueContentFraction(), CellsWithNumericContentFraction(), VarianceInDateTokens(), NumberOfWordsAverage()] #+column index

FeatureList = [Connectivity(), Support(), CellsWithUniqueContentFraction(), CellsWithNumericContentFraction(), VarianceInDateTokens(), NumberOfWordsAverage()]