import logging
from datetime import datetime
from typing import Tuple, List


class DateFormatter:
    def format_date(date_str: str, date_formats: List[str]) -> Tuple[str,
                                                                     str,
                                                                     str,
                                                                     str]:
        for date_format in date_formats:
            try:
                date_obj = datetime.strptime(date_str, date_format)

                year_str = str(date_obj.year)
                month_str = str(date_obj.month).zfill(2)
                day_str = str(date_obj.day).zfill(2)
                date_formatted = f'{year_str}-{month_str}-{day_str}'

                return year_str, month_str, day_str, date_formatted
            except ValueError:
                continue

        error_message = (
            f"Invalid date format. Expected formats are "
            f"{', '.join(date_formats)}."
            f" Got {date_str}"
        )
        logging.error(error_message)
        raise ValueError(error_message)
