from dataclasses import dataclass


@dataclass
class VarianceFactorAnalysisOptions:
    mejor_name: str
    product_category: str
    product_name: str
    item: str
    devision_name: str
    channel_name: str


@dataclass
class TrendAnalysisOptions:
    mejor_name: str
    product_category: str
    product_name: str
    item: str
    devision_name: str
    channel_name: str
