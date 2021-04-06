from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
import io
from typing import Optional

from Utils import CSVDataclassTableWriter, WriteDataclassList


class ExpenseType(Enum):
    UnsetExpenseType = 0
    OfflineExpense = 1
    ExpenseOnEbaySale = 2
    ExpenseOnAmazonSale = 3


@dataclass
class ExampleExpenseEffect:
    Month: int
    OrderNumber: Optional[str]
    ItemId: Optional[str]
    EffectType: ExpenseType
    Advertising: Optional[Decimal]
    CommissionsAndFees: Optional[Decimal]
    LegalAndProfSvcs: Optional[Decimal]
    OfficeExpenses: Optional[Decimal]
    RepairsAndMaint: Optional[Decimal]
    Supplies: Optional[Decimal]
    TaxesAndLicenses: Optional[Decimal]
    Utilities: Optional[Decimal]


class Test_01_CSVDataclassTableWriter():

    def test_Basic(self):
        expenses = [
            ExampleExpenseEffect(
                Month=202100+i,
                OrderNumber='05-06652-59131',
                ItemId='293985538348',
                EffectType=ExpenseType.ExpenseOnEbaySale,
                Advertising=None,
                CommissionsAndFees=(
                    Decimal('-0.3') +  # Final Value Fee - fixed
                    Decimal('-0.79') +  # Final Value Fee - variable
                    Decimal('-0.07')),  # International fee
                LegalAndProfSvcs=None,
                OfficeExpenses=None,
                RepairsAndMaint=None,
                Supplies=None,
                TaxesAndLicenses=None,
                Utilities=None,
            ) for i in range(1, 2+1)
        ]
        expected = """
Month,OrderNumber,ItemId,EffectType,Advertising,CommissionsAndFees,LegalAndProfSvcs,OfficeExpenses,RepairsAndMaint,Supplies,TaxesAndLicenses,Utilities
202101,05-06652-59131,293985538348,ExpenseType.ExpenseOnEbaySale,,-1.16,,,,,,
202102,05-06652-59131,293985538348,ExpenseType.ExpenseOnEbaySale,,-1.16,,,,,,
""".strip().replace("\n", "\r\n")
        with io.StringIO() as testFile:
            CSVDataclassTableWriter[ExampleExpenseEffect](
                expenses).write_file(testFile)
            testFileText = testFile.getvalue().strip()
            assert(testFileText == expected)


class Test_02_WriteDataclassList():
    def test_Basic(self):
        expenses = [
            ExampleExpenseEffect(
                Month=202100+i,
                OrderNumber='05-06652-59131',
                ItemId='293985538348',
                EffectType=ExpenseType.ExpenseOnEbaySale,
                Advertising=None,
                CommissionsAndFees=(
                    Decimal('-0.3') +  # Final Value Fee - fixed
                    Decimal('-0.79') +  # Final Value Fee - variable
                    Decimal('-0.07')),  # International fee
                LegalAndProfSvcs=None,
                OfficeExpenses=None,
                RepairsAndMaint=None,
                Supplies=None,
                TaxesAndLicenses=None,
                Utilities=None,
            ) for i in range(1, 2+1)
        ]
        expected = """
Month,OrderNumber,ItemId,EffectType,Advertising,CommissionsAndFees,LegalAndProfSvcs,OfficeExpenses,RepairsAndMaint,Supplies,TaxesAndLicenses,Utilities
202101,05-06652-59131,293985538348,ExpenseType.ExpenseOnEbaySale,,-1.16,,,,,,
202102,05-06652-59131,293985538348,ExpenseType.ExpenseOnEbaySale,,-1.16,,,,,,
""".strip().replace("\n", "\r\n")
        with io.StringIO() as testFile:
            WriteDataclassList(testFile, expenses, ExampleExpenseEffect)
            testFileText = testFile.getvalue().strip()
            assert(testFileText == expected)


if __name__ == '__main__':
    Test_01_CSVDataclassTableWriter().test_Basic()
