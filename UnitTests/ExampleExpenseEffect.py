from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Optional


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
