__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    dd = int(seconds) // (60 * 60 * 24)
    hh = (seconds % (60 * 60 * 24)) // (60 * 60)
    mm = (seconds % (60 * 60)) // 60
    ss = f'{seconds % 60:02}s'
    if dd:
        return f'{dd:02}d{hh:02}h{mm:02}m' + ss
    if hh:
        return f'{hh:02}h{mm:02}m' + ss
    if mm:
        return f'{mm:02}m' + ss
    return ss
