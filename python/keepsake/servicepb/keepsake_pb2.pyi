# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CreateExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    disableHeartbeat: builtin___bool = ...
    quiet: builtin___bool = ...

    @property
    def experiment(self) -> type___Experiment: ...

    def __init__(self,
        *,
        experiment : typing___Optional[type___Experiment] = None,
        disableHeartbeat : typing___Optional[builtin___bool] = None,
        quiet : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"disableHeartbeat",b"disableHeartbeat",u"experiment",b"experiment",u"quiet",b"quiet"]) -> None: ...
type___CreateExperimentRequest = CreateExperimentRequest

class CreateExperimentReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def experiment(self) -> type___Experiment: ...

    def __init__(self,
        *,
        experiment : typing___Optional[type___Experiment] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> None: ...
type___CreateExperimentReply = CreateExperimentReply

class CreateCheckpointRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    quiet: builtin___bool = ...

    @property
    def checkpoint(self) -> type___Checkpoint: ...

    def __init__(self,
        *,
        checkpoint : typing___Optional[type___Checkpoint] = None,
        quiet : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"checkpoint",b"checkpoint"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"checkpoint",b"checkpoint",u"quiet",b"quiet"]) -> None: ...
type___CreateCheckpointRequest = CreateCheckpointRequest

class CreateCheckpointReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def checkpoint(self) -> type___Checkpoint: ...

    def __init__(self,
        *,
        checkpoint : typing___Optional[type___Checkpoint] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"checkpoint",b"checkpoint"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"checkpoint",b"checkpoint"]) -> None: ...
type___CreateCheckpointReply = CreateCheckpointReply

class SaveExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    quiet: builtin___bool = ...

    @property
    def experiment(self) -> type___Experiment: ...

    def __init__(self,
        *,
        experiment : typing___Optional[type___Experiment] = None,
        quiet : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment",u"quiet",b"quiet"]) -> None: ...
type___SaveExperimentRequest = SaveExperimentRequest

class SaveExperimentReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def experiment(self) -> type___Experiment: ...

    def __init__(self,
        *,
        experiment : typing___Optional[type___Experiment] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> None: ...
type___SaveExperimentReply = SaveExperimentReply

class StopExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    experimentID: typing___Text = ...

    def __init__(self,
        *,
        experimentID : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experimentID",b"experimentID"]) -> None: ...
type___StopExperimentRequest = StopExperimentRequest

class StopExperimentReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___StopExperimentReply = StopExperimentReply

class GetExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    experimentIDPrefix: typing___Text = ...

    def __init__(self,
        *,
        experimentIDPrefix : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experimentIDPrefix",b"experimentIDPrefix"]) -> None: ...
type___GetExperimentRequest = GetExperimentRequest

class GetExperimentReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def experiment(self) -> type___Experiment: ...

    def __init__(self,
        *,
        experiment : typing___Optional[type___Experiment] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experiment",b"experiment"]) -> None: ...
type___GetExperimentReply = GetExperimentReply

class ListExperimentsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___ListExperimentsRequest = ListExperimentsRequest

class ListExperimentsReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def experiments(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Experiment]: ...

    def __init__(self,
        *,
        experiments : typing___Optional[typing___Iterable[type___Experiment]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experiments",b"experiments"]) -> None: ...
type___ListExperimentsReply = ListExperimentsReply

class DeleteExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    experimentID: typing___Text = ...

    def __init__(self,
        *,
        experimentID : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experimentID",b"experimentID"]) -> None: ...
type___DeleteExperimentRequest = DeleteExperimentRequest

class DeleteExperimentReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___DeleteExperimentReply = DeleteExperimentReply

class CheckoutCheckpointRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    checkpointIDPrefix: typing___Text = ...
    outputDirectory: typing___Text = ...
    quiet: builtin___bool = ...

    def __init__(self,
        *,
        checkpointIDPrefix : typing___Optional[typing___Text] = None,
        outputDirectory : typing___Optional[typing___Text] = None,
        quiet : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"checkpointIDPrefix",b"checkpointIDPrefix",u"outputDirectory",b"outputDirectory",u"quiet",b"quiet"]) -> None: ...
type___CheckoutCheckpointRequest = CheckoutCheckpointRequest

class CheckoutCheckpointReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___CheckoutCheckpointReply = CheckoutCheckpointReply

class GetExperimentStatusRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    experimentID: typing___Text = ...

    def __init__(self,
        *,
        experimentID : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"experimentID",b"experimentID"]) -> None: ...
type___GetExperimentStatusRequest = GetExperimentStatusRequest

class GetExperimentStatusReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    StatusValue = typing___NewType('StatusValue', builtin___int)
    type___StatusValue = StatusValue
    Status: _Status
    class _Status(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[GetExperimentStatusReply.StatusValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        RUNNING = typing___cast(GetExperimentStatusReply.StatusValue, 0)
        STOPPED = typing___cast(GetExperimentStatusReply.StatusValue, 1)
    RUNNING = typing___cast(GetExperimentStatusReply.StatusValue, 0)
    STOPPED = typing___cast(GetExperimentStatusReply.StatusValue, 1)
    type___Status = Status

    status: type___GetExperimentStatusReply.StatusValue = ...

    def __init__(self,
        *,
        status : typing___Optional[type___GetExperimentStatusReply.StatusValue] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"status",b"status"]) -> None: ...
type___GetExperimentStatusReply = GetExperimentStatusReply

class Experiment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ParamsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___ParamType: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___ParamType] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ParamsEntry = ParamsEntry

    class PythonPackagesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___PythonPackagesEntry = PythonPackagesEntry

    id: typing___Text = ...
    host: typing___Text = ...
    user: typing___Text = ...
    command: typing___Text = ...
    path: typing___Text = ...
    pythonVersion: typing___Text = ...
    keepsakeVersion: typing___Text = ...

    @property
    def created(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def params(self) -> typing___MutableMapping[typing___Text, type___ParamType]: ...

    @property
    def config(self) -> type___Config: ...

    @property
    def pythonPackages(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def checkpoints(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Checkpoint]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        created : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        params : typing___Optional[typing___Mapping[typing___Text, type___ParamType]] = None,
        host : typing___Optional[typing___Text] = None,
        user : typing___Optional[typing___Text] = None,
        config : typing___Optional[type___Config] = None,
        command : typing___Optional[typing___Text] = None,
        path : typing___Optional[typing___Text] = None,
        pythonPackages : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        pythonVersion : typing___Optional[typing___Text] = None,
        checkpoints : typing___Optional[typing___Iterable[type___Checkpoint]] = None,
        keepsakeVersion : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"created",b"created"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"checkpoints",b"checkpoints",u"command",b"command",u"config",b"config",u"created",b"created",u"host",b"host",u"id",b"id",u"keepsakeVersion",b"keepsakeVersion",u"params",b"params",u"path",b"path",u"pythonPackages",b"pythonPackages",u"pythonVersion",b"pythonVersion",u"user",b"user"]) -> None: ...
type___Experiment = Experiment

class Config(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    repository: typing___Text = ...
    storage: typing___Text = ...

    def __init__(self,
        *,
        repository : typing___Optional[typing___Text] = None,
        storage : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"repository",b"repository",u"storage",b"storage"]) -> None: ...
type___Config = Config

class Checkpoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MetricsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___ParamType: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___ParamType] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___MetricsEntry = MetricsEntry

    id: typing___Text = ...
    step: builtin___int = ...
    path: typing___Text = ...

    @property
    def created(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def metrics(self) -> typing___MutableMapping[typing___Text, type___ParamType]: ...

    @property
    def primaryMetric(self) -> type___PrimaryMetric: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        created : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        metrics : typing___Optional[typing___Mapping[typing___Text, type___ParamType]] = None,
        step : typing___Optional[builtin___int] = None,
        path : typing___Optional[typing___Text] = None,
        primaryMetric : typing___Optional[type___PrimaryMetric] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"created",b"created",u"primaryMetric",b"primaryMetric"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"created",b"created",u"id",b"id",u"metrics",b"metrics",u"path",b"path",u"primaryMetric",b"primaryMetric",u"step",b"step"]) -> None: ...
type___Checkpoint = Checkpoint

class PrimaryMetric(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    GoalValue = typing___NewType('GoalValue', builtin___int)
    type___GoalValue = GoalValue
    Goal: _Goal
    class _Goal(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[PrimaryMetric.GoalValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        MAXIMIZE = typing___cast(PrimaryMetric.GoalValue, 0)
        MINIMIZE = typing___cast(PrimaryMetric.GoalValue, 1)
    MAXIMIZE = typing___cast(PrimaryMetric.GoalValue, 0)
    MINIMIZE = typing___cast(PrimaryMetric.GoalValue, 1)
    type___Goal = Goal

    name: typing___Text = ...
    goal: type___PrimaryMetric.GoalValue = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        goal : typing___Optional[type___PrimaryMetric.GoalValue] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"goal",b"goal",u"name",b"name"]) -> None: ...
type___PrimaryMetric = PrimaryMetric

class ParamType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    boolValue: builtin___bool = ...
    intValue: builtin___int = ...
    floatValue: builtin___float = ...
    stringValue: typing___Text = ...
    objectValueJson: typing___Text = ...

    def __init__(self,
        *,
        boolValue : typing___Optional[builtin___bool] = None,
        intValue : typing___Optional[builtin___int] = None,
        floatValue : typing___Optional[builtin___float] = None,
        stringValue : typing___Optional[typing___Text] = None,
        objectValueJson : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"boolValue",b"boolValue",u"floatValue",b"floatValue",u"intValue",b"intValue",u"objectValueJson",b"objectValueJson",u"stringValue",b"stringValue",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"boolValue",b"boolValue",u"floatValue",b"floatValue",u"intValue",b"intValue",u"objectValueJson",b"objectValueJson",u"stringValue",b"stringValue",u"value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["boolValue","intValue","floatValue","stringValue","objectValueJson"]: ...
type___ParamType = ParamType