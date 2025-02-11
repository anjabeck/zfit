#  Copyright (c) 2024 zfit
"""..

todo:: Add module docstring.
"""
from .core.serialmixin import NumpyArrayNotSerializableError
from .util.checks import NONE
from .util.deprecation import deprecated
from .util.exception import (
    AnalyticIntegralNotImplemented,
    AnalyticNotImplemented,
    AnalyticSamplingNotImplemented,
    FunctionNotImplemented,
    IllegalInGraphModeError,
    InitNotImplemented,
    MaximumIterationReached,
    MinimizerSubclassingError,
    MultipleLimitsNotImplemented,
    NormRangeNotImplemented,
    SpecificFunctionNotImplemented,
    VectorizedLimitsNotImplemented,
    ShapeIncompatibleError,
    LogicalUndefinedOperationError,
    ParamNameNotUniqueError,
    BreakingAPIChangeError,
    AnalyticGradientNotAvailable,
)

__all__ = [
    "NameAlreadyTakenError",
    "ParamNameNotUniqueError",
    "IllegalInGraphModeError",
    "NormRangeNotImplemented",
    "MultipleLimitsNotImplemented",
    "VectorizedLimitsNotImplemented",
    "AnalyticNotImplemented",
    "FunctionNotImplemented",
    "AnalyticSamplingNotImplemented",
    "AnalyticIntegralNotImplemented",
    "SpecificFunctionNotImplemented",
    "MinimizerSubclassingError",
    "MaximumIterationReached",
    "ShapeIncompatibleError",
    "InitNotImplemented",
    "LogicalUndefinedOperationError",
    "NumpyArrayNotSerializableError",
    "AnalyticGradientNotAvailable",
    "NONE",
]


class VectorizedLimitsNotImplementedError(VectorizedLimitsNotImplemented):
    @deprecated(None, "Use VectorizedLimitsNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SpecificFunctionNotImplementedError(SpecificFunctionNotImplemented):
    @deprecated(None, "Use SpecificFunctionNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NormRangeNotImplementedError(NormRangeNotImplemented):
    @deprecated(None, "Use NormRangeNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MultipleLimitsNotImplementedError(MultipleLimitsNotImplemented):
    @deprecated(None, "Use MultipleLimitsNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class FunctionNotImplementedError(FunctionNotImplemented):
    @deprecated(None, "Use FunctionNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AnalyticSamplingNotImplementedError(AnalyticSamplingNotImplemented):
    @deprecated(None, "Use AnalyticSamplingNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AnalyticIntegralNotImplementedError(AnalyticIntegralNotImplemented):
    @deprecated(None, "Use AnalyticIntegralNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AnalyticNotImplementedError(AnalyticNotImplemented):
    @deprecated(None, "Use AnalyticNotImplemented instead.")
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NameAlreadyTakenError(Exception):

    def __init__(self, *args: object) -> None:
        raise BreakingAPIChangeError(
            msg="NameAlreadyTakenError has been removed and the behavior has substantially changed:"
            "parameters are now allowed to exist with the same as long as they are not within the same PDF/loss/func."
        )
