from logzero import logger
import redis
import requests

logger.info('starting...')

r = redis.StrictRedis(host='redis', port=6379)
keys = r.keys('*')
for key in keys:
    type = r.type(key)
    logger.info('type: %s' % type)

    if type == b'list':
        val = r.lrange(key, 0, -1)
    elif type == b'set':
        val = r.smembers(key)
    else:
        raise BaseException('FIXME: unhandled redis type!')

    logger.info('val: %s' % val)

logger.info('done.')
