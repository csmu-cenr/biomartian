# first line: 10
@memory.cache()
def _get_timestamped_data(in_out_tuple, dataset, mart):

    intype, outtype = in_out_tuple

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = _get_data(intype, outtype, dataset, mart)

    return timestamp, data
