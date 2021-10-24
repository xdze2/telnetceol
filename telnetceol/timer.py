

from dataclasses import dataclass
from enum import Enum, auto
import re

class TimerType(Enum):
    ONCE = auto()
    EVERY = auto()


class HourFormat(Enum):
    AM = 'A'
    PM = 'P'
    twentyfour = '2'


@dataclass
class TimeValue:
    hour: int
    minute: int

    @classmethod
    def from_response_str(cls, time_str: str):
        if len(time_str) != 5:
            raise ValueError(time_str)
        format_type = time_str[0]
        if format_type != HourFormat.twentyfour.value:
            raise NotImplementedError('Other than 24hour format not implemented')
        
        hour_str, minute_str = time_str[1:3], time_str[3:5]
        hour, minute = int(hour_str), int(minute_str)
        return cls(hour, minute)

    def to_command(self, hour_format: HourFormat = HourFormat.twentyfour):
        """Encode hour to Telnet command format."""
        if hour_format == HourFormat.twentyfour:
            return hour_format.value + f"{self.hour:02d}{self.minute:02d}"
        else:
            raise NotImplementedError('Other than 24hour format not implemented')

    def __repr__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    @classmethod
    def from_user_str(cls, input_str: str):
        hour_str, minute_str = re.split(r":|h", input_str.strip())
        hour, minute = int(hour_str), int(minute_str)
        return cls(hour, minute)


def test_time_value():
    tv = TimeValue.from_response_str('20830')
    assert tv.hour == 8
    assert tv.minute == 30
    assert tv.to_command() == '20830', "Encode back"
    assert TimeValue.from_user_str('08h20') == TimeValue(8, 20)
    assert TimeValue.from_user_str('09:12') == TimeValue(9, 12)


@dataclass
class Timer:
    type: TimerType
    hour_format: HourFormat
    start_time: TimeValue
    stop_time: TimeValue


    @classmethod
    def from_response(cls, response_line: str):
        """
        Parse Timer status response

        TSONCE 20800-FFFFF FA01 09 1
        TSEVERY 20700-FFFFF FA01 08 1
        """
        # timer_type, startstop_time, 
        pass

