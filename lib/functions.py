import pickle
import quandl
import logging


def getLogger():  # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('debug.log', mode='w')
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_quandl_data(quandl_id, start_date, end_date):
    quandl.ApiConfig.api_key = 'd_jsQqcJjQKxx1TDsvhP'

    # Download and cache Quandl dataseries
    cache_path = 'api_data/' + '{}_{}.pkl'.format(quandl_id, end_date).replace(
        '/', '_')
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
        LOGGER.info('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        LOGGER.info('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(
            quandl_id,
            start_date=start_date,
            end_date=end_date,
            returns="pandas")
        df.to_pickle(cache_path)
        LOGGER.info('Cached {} at {}'.format(quandl_id, cache_path))
    return df


LOGGER = getLogger()
