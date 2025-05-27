from dataclasses import dataclass


@dataclass
class VarianceFactorAnalysisOptions:
    target_year: str
    target_period: str
    source_year: str
    source_period: str


@dataclass
class TrendAnalysisOptions:
    mejor_name: str
    product_category: str
    product_name: str
    item: str
    devision_name: str
    channel_name: str


@dataclass
class ItemOptions:
    mejor_name: str
    product_category: str
    product_name: str
    item: str
    devision_name: str
    channel_name: str
