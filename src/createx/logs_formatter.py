import json_log_formatter


class JSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        extra.update({
            "level": record.levelname,
            "pathname": record.pathname,
            "funcName": record.funcName
        })
        return super().json_record(message, extra, record)
